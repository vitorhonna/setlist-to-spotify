from re import A
import requests
import json
from dotenv import load_dotenv
import os
from tabulate import tabulate

print()

# https://api.setlist.fm/rest/1.0/search/setlists?artistName=jao&artistMbid=6797c795-08b4-4da2-a4d8-95a554c2a91c&cityName=araraquara

domain = 'api.setlist.fm/rest'

load_dotenv()

headers = {
    'Accept': 'application/json',
    'x-api-key': os.environ['SETLISTFM_API_KEY'],
}


def get_setlists(numberOfSetlists, artistMbid, artistName='', cityName=''):
    path = '/1.0/search/setlists'

    payload = {
        'artistName': artistName,
        'artistMbid': artistMbid,
        'cityName': cityName,
    }

    r = requests.get(
        f'https://{domain}{path}',
        headers=headers,
        params=payload
    )

    def prettyPrint(response):
        print(json.dumps(response, indent=2))

    if r.ok:
        response = r.json()
        setlists_json = response['setlist']
        # print(setlists_json)
        numberOfSetlists = numberOfSetlists if numberOfSetlists < len(
            setlists_json) else len(setlists_json)

        setlists = []

        for i in range(numberOfSetlists):
            setlist = setlists_json[int(i)]

            if len(setlist['sets']['set']) > 0 and len(setlist['sets']['set'][0]['song']) > 10:
                if len(setlist['sets']['set']) == 1:
                    songs = setlist['sets']['set'][0]['song']
                else:
                    songs = setlist['sets']['set'][0]['song'] + \
                        setlist['sets']['set'][1]['song']
                # print(songs)
                # prettyPrint(songs)

                for song in songs:
                    songs.insert(0, songs.pop()['name'])

                setlists.append(songs)

        return setlists

    else:
        print(f'\nErro {r.status_code}')


def get_artist_info(artistName):
    path = '/1.0/search/artists'

    payload = {
        'artistName': artistName,
        'sort': 'relevance',
    }

    r = requests.get(
        f'https://{domain}{path}',
        headers=headers,
        params=payload
    )

    if r.ok:
        response = r.json()
        numberOfResults = response['total'] if response['total'] < 5 else 5
        artists_raw = response['artist']
        artists = []

        for index, artist in enumerate(artists_raw):
            if index < numberOfResults:
                artists.append({
                    'id': index+1,
                    'name': artist['name'],
                    'mbid': artist['mbid']
                })
            else:
                break

        # print(artists)
        table = tabulate(artists,
                         headers='keys',
                         tablefmt='fancy_grid'
                         )
        print(table)

        return artists

    else:
        print(f'\nErro {r.status_code}')
