import csv, requests, json
from http.client import responses

class LastRequester:

    def __init__(self, api_key):
        self._api_key = api_key
    
    def get_scrobbles(self, csvfile_name):
        scrobbles = []
        with open(csvfile_name, newline='') as csvfile:
            scrobbles_reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
            for row in scrobbles_reader:
                scrobbles.append(row)
        return scrobbles
    def get_track_tags(self, track, artist, tracks_amount = 5):
        payload = {
            'method': 'track.getTopTags',
            'api_key': self._api_key,
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
            return ''

        return tags_names[0:tracks_amount]