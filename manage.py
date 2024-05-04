#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time
from kasa import SmartPlug
import pyrebase
import asyncio
import threading

config = {
    "apiKey": "AIzaSyBdcLwFXzc83muy640gi1UxxHFefNK7hSQ",
    "authDomain": "pythonintegrated.firebaseapp.com",
    "databaseURL": "https://pythonintegrated-default-rtdb.firebaseio.com",
    "projectId": "pythonintegrated",
    "storageBucket": "pythonintegrated.appspot.com",
    "messagingSenderId": "575671784729",
    "appId": "1:575671784729:web:2a9693afb35e0046dda188",
    "measurementId": "G-H8GZRD6Z3Y"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

ip = "192.168.137.131"
plug = SmartPlug(ip)



async def turn_on_off_smart_device():
    while True:
        endpoint = "tekken"
        dist = database.child(endpoint).get().val()
        print("dist->", dist)

        if dist == "ON":
            await plug.update()
            if (plug.is_off):
                await plug.turn_on()
                time.sleep(1)
            database.child(endpoint).set("OFF")
            time.sleep(5)


def between_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(turn_on_off_smart_device())
    loop.close()

async def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'khushiproject.settings')
    try:
        from django.core.management import execute_from_command_line
        t = threading.Thread(target=between_callback)
        t.setDaemon(True)
        t.start()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())