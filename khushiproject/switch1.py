from django.shortcuts import render

from datetime import datetime

import asyncio
from kasa import SmartSwitch
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

# Global IP address
ip = "192.168.137.54"
plug = SmartSwitch(ip)

async def toggle_switch1(request):
    params = {}
    await plug.update()  # Request an update

    plug_val = ""
    if (plug.is_off):
        await plug.turn_on()
        plug_val = "ON"
    else:
        await plug.turn_off()
        plug_val = "OFF"

    usage_today = 0
    print("is on ----- ", plug.is_on)
    await plug.update()
    uptime = await usage_tot()

    usage = plug.modules["usage"]
    # w += f"{usage.daily_data}"
    b = usage.usage_today
    usage_today = b*6/60000.0

    info = plug.hw_info
    sw_ver = info['sw_ver']
    hw_ver = info['hw_ver']
    mac = info['mac']
    # typeV = info['type']
    hwId = info['hwId']
    fwId = info['fwId']
    oemId = info['oemId']
    dev_name = info['dev_name']
    print(plug.hw_info)
    await asyncio.sleep(0.5)

    result_daily = await daily_stats()
    print("res_daily----", result_daily)

    freq_daily = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    freq_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(31):
        pass

    for i in range(len(result_daily)):
        print(result_daily[i])
        if i % 2 == 0:
            temp = result_daily[i][0:2]
            if '.' in temp:
                temp = int(result_daily[i][0:1])
            else:
                temp = int(result_daily[i][0:2])
            freq_daily[temp] = result_daily[i+1]

    print("freq_daily-----", freq_daily)

    result_monthly = await monthly_stats()
    print("res_monthly----", result_monthly)

    for i in range(len(result_monthly)):
        print(result_monthly[i])
        if i % 2 == 0:
            temp = result_monthly[i][0:2]
            if '.' in temp:
                temp = int(result_monthly[i][0:1])
            else:
                temp = int(result_monthly[i][0:2])
            freq_month[temp] = result_monthly[i+1]

    print("freq_month----------", freq_month)

    res1 = await daily_stats()
    res2 = await monthly_stats()
    res3 = await total_this_month()

    print("res1----", res1)
    print("res2----", res2)
    print("res3----", res3)

    res4 = await usage_curr()
    print("res4----", res4)

    current_date = datetime.now().strftime("%d")
    res5 = float(res3/float(current_date))
    res5 = float("{0:.2f}".format(res5))

    res6 = uptime/12.0
    res6 = res6*6/1000.0
    res6 = float("{0:.2f}".format(res6))

    xaxis = []
    yaxis = []

    if database.child('Coordinates(Switch1)').get().val() == None:
        print("hi")
        # abhi ka value get karke firebase push then plot
        res = await usage_curr()

        # using now() to get current time
        current_time = datetime.now()

        curr_hour = float(current_time.hour + current_time.minute /
                          60.0 + current_time.second/3600.0)

        xaxis.append(curr_hour)
        yaxis.append(res)

        task = database.child("Coordinates(Switch1)").child(
            "Coordinate 1").set({"x_axis": curr_hour, "y_axis": res})
    else:
        print("ho")
        cnt = 0
        coll = database.child('Coordinates(Switch1)').get().val()
        for cordinate in coll.items():
            cnt = cnt+1
            xaxis.append(cordinate[1]['x_axis'])
            yaxis.append(cordinate[1]['y_axis'])

        res = await usage_curr()

        # using now() to get current time
        current_time = datetime.now()

        curr_hour = float(current_time.hour + current_time.minute /
                          60.0 + current_time.second/3600.0)

        xaxis.append(curr_hour)
        yaxis.append(res)

        cnt = cnt+1
        print("cnt---", cnt)
        task = database.child("Coordinates(Switch1)").child(
            "Coordinate " + f"{cnt}").set({"x_axis": curr_hour, "y_axis": res})

    dataDictionary = {
        'daily_stats_result_usage': freq_daily[1:],
        'monthly_stats_result_usage': freq_month[1:],
        'xaxis': xaxis,
        'yaxis': yaxis,
    }

    dataHTML = {
        'plug_status': plug_val,
        'daily_stats': res1,
        'monthly_stats': res2,
        'total_this_month': res3,
        'sw_ver': sw_ver,
        'hw_ver': hw_ver,
        'mac': mac,
        # 'type': typeV,
        'hwId': hwId,
        'fwId': fwId,
        'oemId': oemId,
        'dev_name': dev_name,
        'uptime': uptime,
        'usage_today': usage_today,
        'monthly_avg': res5,
        'yearly_avg': res6
    }

    print('test------', dataHTML)
    # dump data
    dataJSON = dumps(dataDictionary)

    params = {}
    params['plug_status'] = plug_val
    params['total_this_month'] = res3

    return render(request, ['switch1.html'], {'params': params, 'data': dataJSON, 'dataHTML': dataHTML})


async def refresh_switch1(request):
    params = {}
    await plug.turn_on()
    await plug.update()  # Request an update

    plug_val = "ON"

    usage_today = 0
    print("is on ----- ", plug.is_on)
    await plug.update()
    uptime = await usage_tot()

    usage = plug.modules["usage"]
    # w += f"{usage.daily_data}"
    b = usage.usage_today
    usage_today = b*6/60000.0

    info = plug.hw_info
    sw_ver = info['sw_ver']
    hw_ver = info['hw_ver']
    mac = info['mac']
    hwId = info['hwId']
    fwId = info['fwId']
    oemId = info['oemId']
    dev_name = info['dev_name']
    print(plug.hw_info)
    await asyncio.sleep(0.5)

    result_daily = await daily_stats()
    print("res_daily----", result_daily)

    t1 = []

    freq_daily = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    freq_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(31):
        pass

    for i in range(len(result_daily)):
        print(result_daily[i])
        if i % 2 == 0:
            temp = result_daily[i][0:2]
            if '.' in temp:
                temp = int(result_daily[i][0:1])
            else:
                temp = int(result_daily[i][0:2])
            freq_daily[temp] = result_daily[i+1]

    print("freq_daily-----", freq_daily)

    result_monthly = await monthly_stats()
    print("res_monthly----", result_monthly)

    for i in range(len(result_monthly)):
        print(result_monthly[i])
        if i % 2 == 0:
            temp = result_monthly[i][0:2]
            if '.' in temp:
                temp = int(result_monthly[i][0:1])
            else:
                temp = int(result_monthly[i][0:2])
            freq_month[temp] = result_monthly[i+1]

    print("freq_month----------", freq_month)

    res1 = await daily_stats()
    res2 = await monthly_stats()
    res3 = await total_this_month()

    print("res1----", res1)
    print("res2----", res2)
    print("res3----", res3)

    res4 = await usage_curr()
    print("res4----", res4)

    current_date = datetime.now().strftime("%d")
    res5 = float(res3/float(current_date))
    res5 = float("{0:.2f}".format(res5))

    res6 = uptime/12.0
    res6 = res6*6/1000.0
    res6 = float("{0:.2f}".format(res6))

    xaxis = []
    yaxis = []

    if database.child('Coordinates(Switch1)').get().val() == None:
        print("hi")
        # abhi ka value get karke firebase push then plot
        res = await usage_curr()

        # using now() to get current time
        current_time = datetime.now()

        curr_hour = float(current_time.hour + current_time.minute /
                          60.0 + current_time.second/3600.0)

        xaxis.append(curr_hour)
        yaxis.append(res)

        task = database.child("Coordinates(Switch1)").child(
            "Coordinate 1").set({"x_axis": curr_hour, "y_axis": res})
    else:
        cnt = 0
        coll = database.child('Coordinates(Switch1)').get().val()
        for cordinate in coll.items():
            cnt = cnt+1
            xaxis.append(cordinate[1]['x_axis'])
            yaxis.append(cordinate[1]['y_axis'])

        res = await usage_curr()

        # using now() to get current time
        current_time = datetime.now()

        curr_hour = float(current_time.hour + current_time.minute /
                          60.0 + current_time.second/3600.0)

        xaxis.append(curr_hour)
        yaxis.append(res)

        cnt = cnt+1
        print("cnt---", cnt)
        task = database.child("Coordinates(Switch1)").child(
            "Coordinate " + f"{cnt}").set({"x_axis": curr_hour, "y_axis": res})

    dataDictionary = {
        'daily_stats_result_usage': freq_daily[1:],
        'monthly_stats_result_usage': freq_month[1:],
        'xaxis': xaxis,
        'yaxis': yaxis,
    }

    dataHTML = {
        'plug_status': plug_val,
        'daily_stats': res1,
        'monthly_stats': res2,
        'total_this_month': res3,
        'sw_ver': sw_ver,
        'hw_ver': hw_ver,
        'mac': mac,
        'hwId': hwId,
        'fwId': fwId,
        'oemId': oemId,
        'dev_name': dev_name,
        'uptime': uptime,
        'usage_today': usage_today,
        'monthly_avg': res5,
        'yearly_avg': res6
    }

    print('test------', dataHTML)
    # dump data
    dataJSON = dumps(dataDictionary)

    params = {}
    params['plug_status'] = plug_val
    params['total_this_month'] = res3

    return render(request, ['switch1.html'], {'data': dataJSON, 'dataHTML': dataHTML})


async def usage_tot():
    await plug.update()
    usage = plug.modules["usage"]
    w = usage.usage_this_month
    w = (w*60*6)/1000
    NSB = float("{0:.2f}".format(w))
    return NSB


async def daily_stats():
    await plug.update()
    w = ""
    usage = plug.modules["usage"]
    w += f"{usage.daily_data}"
    b = usage.daily_data
    myList = []
    for i in range(len(b)):
        myList.append(str(b[i]["day"]) + "." +
                      str(b[i]["month"]) + "." + str(b[i]["year"]))
        c = (b[i]["time"]*60*6)/1000
        NSB = float("{0:.2f}".format(c))
        myList.append(NSB)
    return myList


async def monthly_stats():
    await plug.update()
    w = ""
    usage = plug.modules["usage"]
    w += f"{usage.monthly_data}"
    b = usage.monthly_data
    myList = []
    for i in range(len(b)):
        myList.append(str(b[i]["month"]) + "." + str(b[i]["year"]))
        c = (b[i]["time"]*60*6)/1000
        NSB = float("{0:.2f}".format(c))
        myList.append(NSB)
    return myList


async def total_this_month():
    await plug.update()
    usage = plug.modules["usage"]
    w = usage.usage_this_month
    w = (w*60*6)/1000
    NSB = float("{0:.2f}".format(w))
    return NSB


async def usage_curr():
    await plug.update()
    a = 2
    if plug.is_on == 0:
        a = 0
    else:
        b = (
            int(plug.on_since.hour) * 3600
            + int(plug.on_since.minute) * 60
            + int(plug.on_since.second)
            - (
                (
                    int(plug.time.hour) * 3600
                    + int(plug.time.minute) * 60
                    + int(plug.time.second)
                )
            )
        )
        b = (b * 6) / 1000
        a = float("{0:.2f}".format(b))

    return a
