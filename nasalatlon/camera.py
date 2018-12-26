import requests
import json


def get_photo(lat, lon, date='2014-02-01', api_key='DEMO_KEY'):
    return json.loads(
        requests.get(
            'https://api.nasa.gov/planetary/earth/imagery/?'
            'lon={}&lat={}&date={}&cloud_score=True&api_key={}'
            .format(str(lon), str(lat), str(date), api_key)
        ).text
    )
