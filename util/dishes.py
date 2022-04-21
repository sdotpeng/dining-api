import requests
import json
from util import emojis

def get_dishes(hall_num):
    STATION_DATA = {1445: ["comforts", "American grill"],
            1447: ["home", "grill"]}
    url = f"https://legacy.cafebonappetit.com/api/2/menus?cafe={hall_num}"
    data = json.loads(requests.get(url).content)
    days_data, dishes_data = data['days'], data['items']
    times = days_data[0]["cafes"][str(hall_num)]['dayparts'][0]

    # Get special dishes
    # {'Breakfast': ['19218027', '15362508'], 'Lunch': ['18488809', '18488810', '18488811', '6232264', '6230584', '6231150', '6230968', '6230969', '6230970', '6231877', '6231861', '6300286', '7372121', '5717843', '6230578', '6230974', '6230985', '6230986', '6230978', '6230972', '6230957', '6231948', '6231878', '6300298', '6300287', '6300288', '15362508'], 'Dinner': ['18488811', '18488812', '18488813', '6232264', '6230584', '6231150', '6230968', '6230969', '6230970', '6231877', '6231861', '6300286', '7372121', '5717843', '6230578', '6230974', '6230985', '6230986', '6230978', '6230972', '6230957', '6231948', '6231878', '6300298', '6300287', '6300288', '15362508']}

    special_dishes = {}
    for time in times:
        label = time['label']
        stations = time['stations']
        for station in stations:
            if station["label"] in STATION_DATA[hall_num]:
                special_dishes[label] = special_dishes.get(label, []) + station["items"]

    output = {}
    for time, dishes in special_dishes.items():
        for dish_id in dishes:
            if dishes_data[dish_id]['special'] == 1:
                dishes_name = dishes_data[dish_id]['label']
                output[time] = output.get(time, '') +  emojis.get_emoji(dishes_name.lower()) + " " + dishes_name.title() + "\n"

    return output

if __name__ == "__main__":
    pass