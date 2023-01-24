import csv
import requests
import json
from http.client import responses

api_key = None
user_agent = 'dj1vs'

def get_api_key():
    with open('api_key.txt') as key_file:
        return key_file.readline()

def get_scrobbles():
    scrobbles = []
    with open('scrobbles.csv', newline='') as csvfile:
        scrobbles_reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in scrobbles_reader:
            scrobbles.append(row)
    return scrobbles

def get_track_tags(track, artist):
    global api_key

    payload = {
        'method': 'track.getTopTags',
        'api_key': api_key,
        'artist': artist,
        'track': track,
        'format': 'json',
        'autocorrect': 1
    }


    r = requests.get('https://ws.audioscrobbler.com/2.0/', params=payload)

    if r.status_code != 200:
        print(responses[r.status_code])
        return []

    
    json_data = json.loads(json.dumps(r.json()))

    try:
        tags_names = [x['name'] for x in json_data['toptags']['tag']]
    except KeyError:
        print(artist, track)
        print(r.url)
        print()
        print()
        print()
        print()
        print()
        return ''
    
    if len(tags_names) == 0:
        print(r.url)
        print()
        print()
        print()
        print()
        print()

    return tags_names[0:5]

def main():
    global api_key
    api_key = get_api_key()
    scrobbles = get_scrobbles()

    for x in scrobbles:
        artist = x[1]
        track = x[3]
        print(artist, track, get_track_tags(track, artist))

    #print(get_track_tags('I\'d Rather Sleep', 'Kero Kero Bonito'))

if __name__ == "__main__":
    main()