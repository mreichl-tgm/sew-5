import requests

key = "AIzaSyCFv2CAcVfQ-not4fVuj7nCOfhC8tctjFw"


def get_route(origin: str, target: str, response_type="json"):
    payload = {"origin": origin,
               "destination": target.replace(" ", "+"),
               "key": key}

    response = requests.get("https://maps.googleapis.com/maps/api/directions/" + response_type, payload)

    if response_type == "json":
        pass

    if response_type == "xml":
        pass
