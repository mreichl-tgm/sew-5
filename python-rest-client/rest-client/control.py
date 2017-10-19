"""
author: Burak Tekin :)
version: 19.10.2017
"""
import requests
from PySide.QtGui import QWidget

from src.view import View

KEY = "AIzaSyCFv2CAcVfQ-not4fVuj7nCOfhC8tctjFw"
LANG = "de"


class Control(QWidget):
    def __init__(self):
        """
        The GUI's control unit used to update data and process user input
        """
        super().__init__()
        self.view = View()
        # Add Qt Signals
        self.view.button_show.clicked.connect(self.submit)
        self.view.button_reset.clicked.connect(self.reset)
        self.view.button_close.clicked.connect(self.view.close)

    def reset(self):
        self.view.text_browser.clear()

    def submit(self):
        origin = self.view.line_origin.text()
        destination = self.view.line_target.text()

        self.reset()

        try:
            response_type = "json"
            url = "https://maps.googleapis.com/maps/api/directions/" + response_type

            params = {
                "origin": origin,
                "destination": destination,
                "language": LANG,
                "key": KEY,
                "sensor": "false"}

            response = requests.get(url, params).json()

            origin_text = "Origin: " + response["routes"][0]["legs"][0]["start_address"]
            destination_text = "Destination: " + response["routes"][0]["legs"][0]["end_address"]
            distance_text = "Distance: " + response["routes"][0]["legs"][0]["distance"]["text"]
            duration_text = "Duration: " + response["routes"][0]["legs"][0]["duration"]["text"]

            text = "{0}<br>{1}<br>{2}<br>{3}<br>".format(origin_text, destination_text, distance_text, duration_text)

            for step in response["routes"][0]["legs"][0]["steps"]:
                instruction_subtext = step["html_instructions"]
                distance_subtext = step["distance"]["text"]
                duration_subtext = step["duration"]["text"]

                text += "<br>{0} | {1} - {2}".format(instruction_subtext, distance_subtext, duration_subtext)

            self.view.text_browser.append(text)
        except IndexError:
            self.view.text_browser.append("ERROR: Not a valid result")
