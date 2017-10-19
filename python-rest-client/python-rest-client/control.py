"""
:author: Markus Reichl
:version: 19.10.2017
"""

import sys
from xml.etree import ElementTree

import requests
from PySide.QtGui import QApplication

from model import LANG, KEY
from view import View


class Control(QApplication):
    """
    Controls the application, handles inputs and calculates results
    """
    def __init__(self):
        """
        The GUI's control unit used to update data and process user input
        """
        super().__init__(sys.argv)
        self.view = View()
        # Add Qt Signals
        self.view.button_show.clicked.connect(self.submit)
        self.view.button_reset.clicked.connect(self.reset)
        self.view.button_close.clicked.connect(self.view.close)
        # Process QApplication events
        while self.view.isVisible():
            self.view.update()
            self.processEvents()

        sys.exit()

    def reset(self):
        """
        Clears all fields in the view
        """
        self.view.line_origin.clear()
        self.view.line_target.clear()
        self.view.text_browser.clear()

    def submit(self):
        """
        Submits the form and
        """
        origin = self.view.line_origin.text()
        destination = self.view.line_target.text()
        response_type = "xml" if self.view.radio_xml.isChecked() else "json"

        self.reset()
        self.view.text_browser.append(Control.route(origin, destination, response_type))

    @staticmethod
    def route(origin, destination, response_type="json"):
        """
        Requests the route from the origin to the destination from the google maps api
        :rtype: str
        :param origin: Where to start
        :param destination: Where to go
        :param response_type: json (default) or xml
        :return: Human readable instructions on how to get from the origin to the destination
        """
        url = "https://maps.googleapis.com/maps/api/directions/" + response_type
        params = {
            "origin": origin,
            "destination": destination,
            "language": LANG,
            "key": KEY,
            "sensor": "false"}

        response = requests.get(url, params)

        if response_type == "json":
            return Control.from_json(response)
        if response_type == "xml":
            return Control.from_xml(response)

        return "ERROR: Not a valid response type"

    @staticmethod
    def from_json(response):
        """
        Converts a xml string to human readable instructions
        :rtype: str
        :param response: Response string in xml format
        :return: Human readable instructions on how to get from the origin to the destination
        """
        response = response.json()
        try:
            route = response["routes"][0]["legs"][0]
            # Format route overview
            text = Control.format_route(route["start_address"],
                                        route["end_address"],
                                        route["distance"]["text"],
                                        route["duration"]["text"])
            # Add instructions steps
            for step in route["steps"]:
                text += Control.format_step(step["html_instructions"],
                                            step["distance"]["text"],
                                            step["duration"]["text"])
            return text

        except IndexError:
            return "ERROR: Not a valid result"

    @staticmethod
    def from_xml(response):
        """
        Converts a json string to human readable instructions
        :rtype: str
        :param response: Response string in json format
        :return: Human readable instructions on how to get from the origin to the destination
        """
        response = ElementTree.fromstring(response.text)

        try:
            route = response.find("route").find("leg")
            # Format route overview
            text = Control.format_route(route.find("start_address").text,
                                        route.find("end_address").text,
                                        route.find("distance").find("text").text,
                                        route.find("duration").find("text").text)
            # Add instructions steps
            for step in route.findall("step"):
                text += Control.format_step(step.find("html_instructions").text,
                                            step.find("distance").find("text").text,
                                            step.find("duration").find("text").text)
            return text

        except AttributeError:
            return "ERROR: Not a valid result"

    @staticmethod
    def format_route(origin, destination, distance, duration):
        """
        Returns a human readable (hr), html formatted string using the given contents
        :rtype: str
        :param origin: hr origin
        :param destination: hr destination
        :param distance: hr distance
        :param duration: hr duration
        :return: Human readable html formatted string
        """
        return "Origin: {0}<br>Destination: {1}<br>Distance: {2}<br>Duration: {3}<br>" \
            .format(origin, destination, distance, duration)

    @staticmethod
    def format_step(instruction, distance, duration):
        """
        Returns a human readable (hr), html formatted string using the given contents
        :rtype: str
        :param instruction: hr instruction
        :param distance: hr distance
        :param duration: hr duration
        :return: Human readable html formatted string
        """
        return "<br>{0} | {1} - {2}".format(instruction, distance, duration)
