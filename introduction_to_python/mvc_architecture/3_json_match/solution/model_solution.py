import json

match_data = {
    "sports": ["football", "tennis", "cricket", "hockey"],
    "country": ["USA", "swiss", "india", "canada"],
}

data_match = json.dumps(match_data)

def get_list():
    return(data_match)

def retrive_match(sport, country):
    data = json.loads(data_match)
    data_a = [sport for sport in data["sports"]]
    data_b = [country for country in data["country"]]
    return data_a, data_b
