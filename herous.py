import requests
import json

url = 'https://akabab.github.io/superhero-api/api/all.json'
book = (requests.get(url)).json()

def most_int (list):
    name_int_full = {}
    for t in book:
        name = t.get('name')
        stats = t.get('powerstats')
        intel = stats.get('intelligence')
        name_int_full[name] = intel

    name_int = {}
    name_list = ['Hulk', 'Captain America', 'Thanos']
    for name, int in name_int_full.items():
        if name in name_list:
            name_int[name] = int
        else:
            continue
    
    most_powerfull = sorted(name_int.items(), reverse=True)
    return most_powerfull[0]

print(most_int(book))
