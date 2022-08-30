from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

domain = 'api.spotify.com'

headers = {
    "Content-Type": 'application/json',
    "Authorization": f'Bearer {os.environ["SPOTIFY_TOKEN"]}'
}


def get_song_uris(song_names, artist_name):
    endpoint = '/v1/search'

    song_uris = []

    for song_name in song_names:
        payload = {
            'q': f'{song_name} artist:{artist_name}',
            'type': 'track',
            'market': 'br',
            'limit': '1',
        }

        r = requests.get(
            f'https://{domain}{endpoint}',
            headers=headers,
            params=payload
        )

        response = r.json()

        if r.ok and len(response['tracks']['items']) > 0:
            song_name = response['tracks']['items'][0]['name']
            song_id = response['tracks']['items'][0]['uri']
            song_uris.append(song_id)

        elif r.status_code == 200:
            print(
                f'[!] "{song_name}, {artist_name}" was not found. Skipping...')

        else:
            print(
                f"Error {response['error']['status']}: {response['error']['message']}")

    return song_uris


def get_user_id():
    endpoint = '/v1/me'
    r = requests.get(f'https://{domain}{endpoint}', headers=headers)
    response = r.json()
    return response['id']


def create_playlist(playlist_name, user_id):
    endpoint = f'/v1/users/{user_id}/playlists'

    body = {
        "name": playlist_name,
        "public": 'false'
    }

    r = requests.post(
        f'https://{domain}{endpoint}',
        headers=headers,
        json=body
    )

    response = r.json()

    if r.ok:
        playlist_id = response['id']
        playlist_link = response['external_urls']['spotify']
        return [playlist_id, playlist_link]

    else:
        print(
            f"Error {response['error']['status']}: {response['error']['message']}")


def add_songs_to_playlist(song_uris, playlist_id):
    endpoint = f'/v1/playlists/{playlist_id}/tracks'

    body = {
        'uris': song_uris
    }

    r = requests.post(
        f'https://{domain}{endpoint}',
        headers=headers,
        json=body
    )
