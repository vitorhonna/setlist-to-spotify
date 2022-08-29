import requests
import json
from dotenv import load_dotenv
import os
from tabulate import tabulate

load_dotenv()

domain = 'api.setlist.fm/rest'

headers = {
    'Accept': 'application/json',
    'x-api-key': os.environ['SETLISTFM_API_KEY'],
}


def get_setlists(numberOfSetlists, minSetlistSize, artistMbid, artistName='', cityName=''):
    path = '/1.0/search/setlists'

    payload = {
        'artistMbid': artistMbid,
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
        numberOfSetlists = numberOfSetlists if numberOfSetlists < len(
            setlists_json) else len(setlists_json)

        setlists = []

        for i in range(numberOfSetlists):
            setlist = setlists_json[int(i)]

            if len(setlist['sets']['set']) > 0 and len(setlist['sets']['set'][0]['song']) > minSetlistSize:
                if len(setlist['sets']['set']) == 1:
                    songs = setlist['sets']['set'][0]['song']
                else:
                    songs = setlist['sets']['set'][0]['song'] + \
                        setlist['sets']['set'][1]['song']

                for song in songs:
                    songs.insert(0, songs.pop()['name'])

                setlists.append(songs)

        return setlists

    else:
        print(f'\nError: {r.status_code}')


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
        numberOfResultsToShow = 3
        numberOfResults = response['total'] if response['total'] < numberOfResultsToShow else numberOfResultsToShow
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

        table = tabulate(artists,
                         headers='keys',
                         tablefmt='fancy_grid'
                         )
        print(table)

        return artists

    else:
        print(f'\nError: {r.status_code}')
