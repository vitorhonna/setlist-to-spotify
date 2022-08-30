import requests
from dotenv import load_dotenv
import os

load_dotenv()

endpoint_url = "https://api.spotify.com/v1/recommendations?"

# OUR FILTERS
limit=10
market="US"
seed_genres="indie"
target_danceability=0.9

query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'

response =requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {os.environ['SPOTIFY_API_KEY']}"})

json_response = response.json()

uris = []

for i in json_response['tracks']:
            uris.append(i)
            print(f"\"{i['name']}\" by {i['artists'][0]['name']}")