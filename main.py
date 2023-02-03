from LastRequester import LastRequester

import csv, requests, json

user_agent = 'dj1vs'

def get_api_key():
    with open('api_key.txt') as key_file:
        return key_file.readline()

def main():
    requester = LastRequester(get_api_key())
    scrobbles = requester.get_scrobbles('scrobbles.csv')

    for x in scrobbles:
        artist = x[1]
        track = x[3]
        print(artist, track, requester.get_track_tags(track, artist))

if __name__ == "__main__":
    main()