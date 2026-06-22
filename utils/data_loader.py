import json


def load_outfits():

    with open("data/outfits.json", "r") as file:
        return json.load(file)