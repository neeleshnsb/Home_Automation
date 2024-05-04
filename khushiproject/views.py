from django.shortcuts import render

from datetime import datetime

import asyncio
import time
from kasa.discover import Discover
from kasa import SmartPlug, SmartSwitch
import kasa.modules.module as km
from json import dumps
import pyrebase

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

ip = "192.168.216.164"
plug = SmartPlug(ip)

async def turn_on_off_smart_device():
    while True:
        print("fuck")
        endpoint = "tekken"
        dist = database.child(endpoint).get().val()

        if dist == "ON":
            await plug.update()  # Request an update

            # plug_val = ""
            if (plug.is_off):
                await plug.turn_on()
                # plug_val = "ON"
                database.child(endpoint).set("OFF")
            else:
                await plug.turn_off()
                # plug_val = "OFF"
                database.child(endpoint).set("OFF")
        # time.sleep(5)  # Wait for 5 seconds before checking again

# asyncio.run(turn_on_off_smart_device())
# turn_on_off_smart_device()

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
job = None

async def start_job():
    global job
    job = scheduler.add_job(await turn_on_off_smart_device, 'interval', seconds=10)
    try:
        scheduler.start()
    except:
        pass

# start_job()

# Global IP address
# ip = "192.168.116.228"
# plug = SmartPlug(ip)



async def dashboard(request):
    # ip = "192.168.137.255"
    # discover = await Discover.discover(target=ip)
    # a = discover.keys()
    # mylist1 = list(a)
    # print("testing1----------", a)
    # print("discover alias------------", discover.get(mylist1[0]).alias)
    # print("discover is on------------", discover.get(mylist1[0]).is_on)

    # device_status = ""
    # if discover.get(mylist1[0]).is_on == True:
    #     device_status = "ON"
    # else:
    #     device_status = "OFF"

    # params = {}
    # params['device_alias'] = discover.get(mylist1[0]).alias
    # params['device_ison'] = device_status

    plug1_ip = "192.168.216.164"
    plug2_ip = "192.168.137.128"
    switch1_ip = "192.168.137.54"
    switch2_ip = "192.168.137.27"
    switch3_ip = "192.168.137.172"
    switch4_ip = "192.168.137.246"
    switch5_ip = "192.168.137.151"

    params={}
    params['plug1_ip'] = plug1_ip
    params['plug2_ip'] = plug2_ip
    params['switch1_ip'] = switch1_ip
    params['switch2_ip'] = switch2_ip
    params['switch3_ip'] = switch3_ip
    params['switch4_ip'] = switch4_ip
    params['switch5_ip'] = switch5_ip

    return render(request, 'index.html', params)




async def index(request):

    # turn_on_off_smart_device()
    # ip = "127.0.0.1"
    # ip = "192.168.222.228"
    # print("discover------------", await Discover.discover())
    params = {}
    # year = datetime.now().year
    # dev = SmartDevice(ip)
    # plug = SmartPlug(ip)
    # # asyncio.run(dev.update())
    # # while True:
    # await plug.update()  # Request an update
    # print(plug.device_id)
    # await asyncio.sleep(0.5)

    # plug.add_module("Plug1", module=km)

    # print(dev.hw_info)
    # # print(dev.turn_on)
    # # dev.turn_on()
    print("done")
    # # on = asyncio.run(dev.turn_off())
    # await dev.turn_off()
    # plug_status = dev.is_on
    # print(plug_status)
    # time.sleep(5)
    # await dev.turn_off()
    # if plug_status:
    #     params["state"] = "ON"
    # else:
    #     params["state"] = "OFF"
    # has_emeter = dev.has_emeter
    # emeter_val = ""
    # if has_emeter:
    #     params["has_emeter"] = "true"
    #     emeter_realtime = dev.emeter_realtime
    #     params["power_realtime"] = emeter_realtime.power
    #     params["voltage_realtime"] = emeter_realtime.voltage
    #     params["current_realtime"] = emeter_realtime.current
    #     params["total_realtime"] = emeter_realtime.total
    #     emeter_today = dev.emeter_today
    #     emeter_monthly = dev.emeter_this_month
    #     emeter_yearly = asyncio.run(dev.get_emeter_monthly(year=year))
    # else:
    # params["has_emeter"] = "false"
    # params["has_emeter"] = "false"

    # params = {}
    # year = datetime.now().year
    # params["state"] = "ON"
    # has_emeter = True
    # params["has_emeter"] = "true"
    # if has_emeter:
    #     params["power_realtime"] = 0.98
    #     params["voltage_realtime"] = 235.595
    #     params["current_realtime"] = 0.015
    #     params["total_realtime"] = 32.448

    return render(request, 'index.html', params)

async def switch1(request):
    ip = "127.0.0.1"
    # params = {}
    # year = datetime.now().year
    # dev = SmartDevice(ip)
    # asyncio.run(dev.update())
    # plug_status = dev.is_on
    # if plug_status:
    #     params["state"] = "ON"
    # else:
    #     params["state"] = "OFF"
    # has_emeter = dev.has_emeter
    # emeter_val = ""
    # if has_emeter:
    #     params["has_emeter"] = "true"
    #     emeter_realtime = dev.emeter_realtime
    #     params["power_realtime"] = emeter_realtime.power
    #     params["voltage_realtime"] = emeter_realtime.voltage
    #     params["current_realtime"] = emeter_realtime.current
    #     params["total_realtime"] = emeter_realtime.total
    #     emeter_today = dev.emeter_today
    #     emeter_monthly = dev.emeter_this_month
    #     emeter_yearly = asyncio.run(dev.get_emeter_monthly(year=year))
    # else:
    #     params["has_emeter"] = "false"

    params = {}
    year = datetime.now().year
    params["state"] = "ON"
    has_emeter = True
    params["has_emeter"] = "true"
    if has_emeter:
        params["power_realtime"] = 0.98
        params["voltage_realtime"] = 235.595
        params["current_realtime"] = 0.015
        params["total_realtime"] = 32.448

    return render(request, 'switch1.html', params)

async def switch2(request):
    ip = "127.0.0.1"
    # params = {}
    # year = datetime.now().year
    # dev = SmartDevice(ip)
    # asyncio.run(dev.update())
    # plug_status = dev.is_on
    # if plug_status:
    #     params["state"] = "ON"
    # else:
    #     params["state"] = "OFF"
    # has_emeter = dev.has_emeter
    # emeter_val = ""
    # if has_emeter:
    #     params["has_emeter"] = "true"
    #     emeter_realtime = dev.emeter_realtime
    #     params["power_realtime"] = emeter_realtime.power
    #     params["voltage_realtime"] = emeter_realtime.voltage
    #     params["current_realtime"] = emeter_realtime.current
    #     params["total_realtime"] = emeter_realtime.total
    #     emeter_today = dev.emeter_today
    #     emeter_monthly = dev.emeter_this_month
    #     emeter_yearly = asyncio.run(dev.get_emeter_monthly(year=year))
    # else:
    #     params["has_emeter"] = "false"

    params = {}
    year = datetime.now().year
    params["state"] = "ON"
    has_emeter = True
    params["has_emeter"] = "true"
    if has_emeter:
        params["power_realtime"] = 0.98
        params["voltage_realtime"] = 235.595
        params["current_realtime"] = 0.015
        params["total_realtime"] = 32.448

    return render(request, 'switch2.html', params)

async def switch3(request):
    ip = "127.0.0.1"
    # params = {}
    # year = datetime.now().year
    # dev = SmartDevice(ip)
    # asyncio.run(dev.update())
    # plug_status = dev.is_on
    # if plug_status:
    #     params["state"] = "ON"
    # else:
    #     params["state"] = "OFF"
    # has_emeter = dev.has_emeter
    # emeter_val = ""
    # if has_emeter:
    #     params["has_emeter"] = "true"
    #     emeter_realtime = dev.emeter_realtime
    #     params["power_realtime"] = emeter_realtime.power
    #     params["voltage_realtime"] = emeter_realtime.voltage
    #     params["current_realtime"] = emeter_realtime.current
    #     params["total_realtime"] = emeter_realtime.total
    #     emeter_today = dev.emeter_today
    #     emeter_monthly = dev.emeter_this_month
    #     emeter_yearly = asyncio.run(dev.get_emeter_monthly(year=year))
    # else:
    #     params["has_emeter"] = "false"

    params = {}
    year = datetime.now().year
    params["state"] = "ON"
    has_emeter = True
    params["has_emeter"] = "true"
    if has_emeter:
        params["power_realtime"] = 0.98
        params["voltage_realtime"] = 235.595
        params["current_realtime"] = 0.015
        params["total_realtime"] = 32.448

    return render(request, 'switch3.html', params)

async def switch4(request):
    ip = "127.0.0.1"
    # params = {}
    # year = datetime.now().year
    # dev = SmartDevice(ip)
    # asyncio.run(dev.update())
    # plug_status = dev.is_on
    # if plug_status:
    #     params["state"] = "ON"
    # else:
    #     params["state"] = "OFF"
    # has_emeter = dev.has_emeter
    # emeter_val = ""
    # if has_emeter:
    #     params["has_emeter"] = "true"
    #     emeter_realtime = dev.emeter_realtime
    #     params["power_realtime"] = emeter_realtime.power
    #     params["voltage_realtime"] = emeter_realtime.voltage
    #     params["current_realtime"] = emeter_realtime.current
    #     params["total_realtime"] = emeter_realtime.total
    #     emeter_today = dev.emeter_today
    #     emeter_monthly = dev.emeter_this_month
    #     emeter_yearly = asyncio.run(dev.get_emeter_monthly(year=year))
    # else:
    #     params["has_emeter"] = "false"

    params = {}
    year = datetime.now().year
    params["state"] = "ON"
    has_emeter = True
    params["has_emeter"] = "true"
    if has_emeter:
        params["power_realtime"] = 0.98
        params["voltage_realtime"] = 235.595
        params["current_realtime"] = 0.015
        params["total_realtime"] = 32.448

    return render(request, 'switch4.html', params)

async def switch5(request):
    ip = "127.0.0.1"
    # params = {}
    # year = datetime.now().year
    # dev = SmartDevice(ip)
    # asyncio.run(dev.update())
    # plug_status = dev.is_on
    # if plug_status:
    #     params["state"] = "ON"
    # else:
    #     params["state"] = "OFF"
    # has_emeter = dev.has_emeter
    # emeter_val = ""
    # if has_emeter:
    #     params["has_emeter"] = "true"
    #     emeter_realtime = dev.emeter_realtime
    #     params["power_realtime"] = emeter_realtime.power
    #     params["voltage_realtime"] = emeter_realtime.voltage
    #     params["current_realtime"] = emeter_realtime.current
    #     params["total_realtime"] = emeter_realtime.total
    #     emeter_today = dev.emeter_today
    #     emeter_monthly = dev.emeter_this_month
    #     emeter_yearly = asyncio.run(dev.get_emeter_monthly(year=year))
    # else:
    #     params["has_emeter"] = "false"

    params = {}
    year = datetime.now().year
    params["state"] = "ON"
    has_emeter = True
    params["has_emeter"] = "true"
    if has_emeter:
        params["power_realtime"] = 0.98
        params["voltage_realtime"] = 235.595
        params["current_realtime"] = 0.015
        params["total_realtime"] = 32.448

    return render(request, 'switch5.html', params)

async def plug1(request):
    # ip = "127.0.0.1"
    # params = {}
    # year = datetime.now().year
    # dev = SmartDevice(ip)
    # asyncio.run(dev.update())
    # plug_status = dev.is_on
    # if plug_status:
    #     params["state"] = "ON"
    # else:
    #     params["state"] = "OFF"
    # has_emeter = dev.has_emeter
    # emeter_val = ""
    # if has_emeter:
    #     params["has_emeter"] = "true"
    #     emeter_realtime = dev.emeter_realtime
    #     params["power_realtime"] = emeter_realtime.power
    #     params["voltage_realtime"] = emeter_realtime.voltage
    #     params["current_realtime"] = emeter_realtime.current
    #     params["total_realtime"] = emeter_realtime.total
    #     emeter_today = dev.emeter_today
    #     emeter_monthly = dev.emeter_this_month
    #     emeter_yearly = asyncio.run(dev.get_emeter_monthly(year=year))
    # else:
    #     params["has_emeter"] = "false"

    params = {}
    # year = datetime.now().year
    # params["state"] = "ON"
    # has_emeter = True
    # params["has_emeter"] = "true"
    # if has_emeter:
    #     params["power_realtime"] = 0.98
    #     params["voltage_realtime"] = 235.595
    #     params["current_realtime"] = 0.015
    #     params["total_realtime"] = 32.448

    return render(request, 'plug1.html', params)

async def plug2(request):
    ip = "127.0.0.1"
    # params = {}
    # year = datetime.now().year
    # dev = SmartDevice(ip)
    # asyncio.run(dev.update())
    # plug_status = dev.is_on
    # if plug_status:
    #     params["state"] = "ON"
    # else:
    #     params["state"] = "OFF"
    # has_emeter = dev.has_emeter
    # emeter_val = ""
    # if has_emeter:
    #     params["has_emeter"] = "true"
    #     emeter_realtime = dev.emeter_realtime
    #     params["power_realtime"] = emeter_realtime.power
    #     params["voltage_realtime"] = emeter_realtime.voltage
    #     params["current_realtime"] = emeter_realtime.current
    #     params["total_realtime"] = emeter_realtime.total
    #     emeter_today = dev.emeter_today
    #     emeter_monthly = dev.emeter_this_month
    #     emeter_yearly = asyncio.run(dev.get_emeter_monthly(year=year))
    # else:
    #     params["has_emeter"] = "false"

    params = {}
    year = datetime.now().year
    params["state"] = "ON"
    has_emeter = True
    params["has_emeter"] = "true"
    if has_emeter:
        params["power_realtime"] = 0.98
        params["voltage_realtime"] = 235.595
        params["current_realtime"] = 0.015
        params["total_realtime"] = 32.448

    return render(request, 'plug2.html', params)
