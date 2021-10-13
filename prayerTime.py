import requests


def todaytime():

    city = 'tashkent'
    url = f"https://api.pray.zone/v2/times/this_week.json?city={city}"

    response = requests.get(url)
    time = response.json()['results']['datetime'][0]['times']
    nom = ['Saharlik', 'Quyosh chiqishi', 'Fajr', 'Peshin', 'Asr', 'Shom', 'Maghrib', 'Xufton', 'Midnight']
    vaqt = list(time.values())
    date = dict(zip(nom, vaqt))
    del date['Fajr']
    del date['Maghrib']
    del date['Midnight']

    return date

def tomorrowtime():
    city = 'tashkent'
    url = f"https://api.pray.zone/v2/times/this_week.json?city={city}"

    response = requests.get(url)
    time = response.json()['results']['datetime'][1]['times']
    nom = ['Saharlik', 'Quyosh chiqishi', 'Fajr', 'Peshin', 'Asr', 'Shom', 'Maghrib', 'Xufton', 'Midnight']
    vaqt = list(time.values())
    date = dict(zip(nom, vaqt))
    del date['Fajr']
    del date['Maghrib']
    del date['Midnight']

    return date