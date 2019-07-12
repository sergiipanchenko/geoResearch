import json
import requests


def geo_data_loader():
    google_url = 'https://storage.googleapis.com/mapsdevsite/json/google.json'
    db_api_url = 'http://localhost:8000/api/v1/polygons/'

    data = requests.get(google_url)

    for each in data.json()['features']:
        type_shape = 'Polygon'

        properties = each['properties']
        letter = properties['letter']
        color = properties['color']
        rank = properties['rank']
        ascii_code = properties['ascii']

        geometry = each['geometry']
        coordinates = geometry['coordinates']

        headers = {'content-type': 'application/json'}
        payload = {
            'geometry': {
                'type': type_shape,
                'coordinates': coordinates
                },
            'letter': letter,
            'color': color,
            'rank': rank,
            'ascii': ascii_code,
            }

        data_upload = requests.post(db_api_url, headers=headers, data=json.dumps(payload))

        if data_upload.status_code == 201:
            print(color, letter, 'is uploaded')


if __name__ == '__main__':
    geo_data_loader()
