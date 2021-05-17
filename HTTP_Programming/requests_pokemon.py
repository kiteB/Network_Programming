# aiohttp 모듈 : 클라이언트 (동기)
import requests
import time

start_time = time.time()

for number in range(1, 11):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

print("--- %s seconds --" % (time.time() - start_time))