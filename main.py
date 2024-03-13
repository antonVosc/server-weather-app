import requests
import datetime
from fastapi import FastAPI, Request
from datetime import datetime

ip_geo_API = ''  # Please enter your api key
x_api_key = ''  # get from headers

app = FastAPI()


def get_city(ip):
    r = requests.get('http://ip-api.com/json/' + ip)
    response = r.json()

    if r.status_code == requests.codes.ok:
        if response['status'] == "success":
            return response['city']
    else:
        return "Error:", r.status_code, r.json()


def get_timestamp(ip):
    api_url = 'https://api.ipgeolocation.io/ipgeo?apiKey={}&ip={}'.format(ip_geo_API, ip)
    response = requests.get(api_url, headers={'X-Api-Key': x_api_key})

    if response.status_code == requests.codes.ok:
        response = response.json()
        timestamp = response["time_zone"]["current_time_unix"]
        dt_object = datetime.fromtimestamp(timestamp)
        day_of_week = dt_object.strftime("%A")

        return day_of_week
    else:
        return "Error:", response.status_code, response.json()


def get_weather(user_ip):
    city = get_city(user_ip)

    if city is None:
        return 'The provided IP is invalid'
    else:
        city = city.lower()
        api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
        response = requests.get(api_url, headers={'X-Api-Key': x_api_key})

        if response.status_code == requests.codes.ok:
            response = response.json()
            response['DOW'] = get_timestamp(user_ip)
            response['City'] = city

            return response
        else:
            return "Error:", response.status_code, response.json()


@app.get('/forecast')
def get_user_ip(request: Request):
    real_ip = request.headers.get("X-Real-IP")

    if real_ip:
        user_ip = real_ip
    else:
        forwarded_for = request.headers.get("X-Forwarded-For")

        if forwarded_for:
            user_ip = forwarded_for.split(",")[0]
        else:
            user_ip = request.client.host

    return get_weather(user_ip)
