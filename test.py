import json

with open("i:/repos/src/rnrepo/rnrepo/resolution_cards.json") as read_file:
    card_data = json.load(read_file)

print(card_data["cards"][0]["id"])