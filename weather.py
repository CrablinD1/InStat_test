import asyncio
import json
import logging
import os
import uuid
from pprint import pformat
from typing import List

import aiohttp
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

BASE_DOMAIN = 'https://api.openweathermap.org/data/2.5'
FILE_NAME = 'data.json'


async def request(method_name: str, url: str) -> dict:
    _uuid = str(uuid.uuid4())
    async with aiohttp.ClientSession() as session:
        logging.info(f'{_uuid} REQUEST: {method_name} | {url}')
        method = getattr(session, method_name)
        async with method(url) as resp:
            if resp.ok:
                data = await resp.json()
                logging.info(f'{_uuid} RESPONSE: {resp.status}')
                return data
            else:
                data = await resp.text()
                logging.info(f'{_uuid} RESPONSE: {resp.status} {pformat(data)}')
                raise Exception


async def get_city_weather(city: str) -> dict:
    weather_url = '{domain}/weather?q={city}&appid={appid}&units=metric'
    weather_data = await request(
        'get', weather_url.format(domain=BASE_DOMAIN, city=city, appid=API_KEY)
    )
    return weather_data


async def create_weather_forecast_file(cities: List[str]):
    logging.info(f'Getting weather forecast for {cities}')
    tasks = [get_city_weather(city) for city in cities]
    weather_data = await asyncio.gather(*tasks)
    data = dict(zip(cities, weather_data))
    with open(FILE_NAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logging.info(f'Weather forecast successfully saved to file "{FILE_NAME}"')
    return


if __name__ == '__main__':
    API_KEY = os.getenv('API_KEY')
    if not API_KEY:
        raise ValueError('API_KEY not found or .env file not exist')
    asyncio.run(create_weather_forecast_file(['Moscow', 'Batumi', 'Marseille']))
