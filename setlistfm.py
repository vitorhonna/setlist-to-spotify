import requests
import json
from dotenv import load_dotenv
import os

print()

# https://api.setlist.fm/rest/1.0/search/setlists?artistName=jao&artistMbid=6797c795-08b4-4da2-a4d8-95a554c2a91c&cityName=araraquara

def get_setlists(numberOfSetlists, artistMbid, artistName='', cityName=''):
    domain = 'api.setlist.fm'
    path_setlists = '/rest/1.0/search/setlists'

    load_dotenv()

    headers = {
        'Accept': 'application/json',
        'x-api-key': os.environ['SETLISTFM_API_KEY'],
    }

    payload = {
        'artistName': artistName,
        'artistMbid': artistMbid,
        'cityName': cityName,
    }

    r = requests.get(
        f'https://{domain}{path_setlists}',
        headers=headers,
        params=payload
    )

    def prettyPrint(response):
        print(json.dumps(response, indent=2))

    if r.ok:
        response = r.json()
        setlists_json = response['setlist']
        # print(setlists_json)

        setlists = []

        for i in range(numberOfSetlists):
            setlist = setlists_json[int(i)]
            songs = setlist['sets']['set'][0]['song'] + \
                setlist['sets']['set'][1]['song']
            # print(songs)
            # prettyPrint(songs)

            for song in songs:
                songs.insert(0, songs.pop()['name'])

            setlists.append(songs)

        return setlists

    else:
        print(f'\nErro {r.status_code} :(')


def get_artist_info(artistName):
    # TODO
    # Given an artist name, return the n first results with artists names and Mbid
    pass
