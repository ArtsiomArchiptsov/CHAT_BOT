import requests

def get_dogs():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        message = data.get('message')
        return message