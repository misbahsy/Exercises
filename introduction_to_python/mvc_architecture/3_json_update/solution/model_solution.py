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
    sport_list = data["sports"]
    sport_list.append(sport)
    country_list = data["country"]
    country_list.append(country)
    data_a = [sport_list, country_list]
    return(data_a)
