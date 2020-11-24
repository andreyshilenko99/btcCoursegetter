import os
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from celery import shared_task
import sqlite3
from django.utils.timezone import localtime, now

@shared_task()
def btc():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': 'BTC',
        'convert': 'RUB',
    }
    key = os.environ.get('API_KEY')
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        temp = data.get('data').get('BTC').get('quote').get('RUB').get('price')
        date = localtime(now())
        current_time = date.strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        sql = "INSERT INTO response(course, get_time) VALUES(?,?)"
        cursor.execute(sql, (round(temp), current_time))
        conn.commit()
        conn.close()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
