import requests
import json
import os
import matplotlib.pyplot as plt
import math

# 1-pitstopTimes:         verilen pilotlarin belli sezon belli yaristaki toplam pitstop surelerini kiyasla
# 2-lapTimes:             verilen pilotlarin belli sezon belli yaris belli turdaki tur sureleri kiyasla
# 3-sessionEnd:           verilen yarisin ilk ucu gorsellestir (race results)
# 4-pilotStandings:       verien yaristan sonra pilotlarin puan durumlarını gorsellestir
# 5-constructorStandings: verien yaristan sonra takimlarin puan durumlarını gorsellestir


colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

fullPath=os.getcwd()
imgName='default'
imgType='png'

#verilen yil ve yaris icin istenen pilotlarin yaris icerisinde pitstopta kaldiklari toplam sureyi gorsellestirir ve istenen path'e kaydeder
def pitstopTimes(params):
    year = params['year'];round = params['round'];pilotsRaw = params['pilots'];
    pilots = pilotsRaw.split("%")
    url = "http://ergast.com/api/f1/"+str(year)+"/"+str(round)+"/pitstops"+".json"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    dict = json.loads(response.text)
    pitstops = dict['MRData']['RaceTable']['Races'][0]['PitStops']

    times = {}
    for pitstop in pitstops:
        driver = pitstop['driverId']
        if driver in pilots:
            if(driver in times): #increment
                times[driver] += float(pitstop['duration'])
            else: #initialize
                times[driver] = float(pitstop['duration'])

    fig = plt.figure(dpi=100, figsize=(14, 7))
    ax = fig.add_subplot(111)
    ax.set_title("Year: " + year + " Round: " + round + " Pitstop Times")
    sortedNames = times.keys()
    pitstopTimes= list(times.values())
    low = min(pitstopTimes)
    high = max(pitstopTimes)
    plt.ylim([math.ceil(low - 0.5 * (high - low))-3, math.ceil(high + 0.5 * (high - low))])
    bars = ax.bar(sortedNames, pitstopTimes, color=colors)
    for bar, time in zip(bars, pitstopTimes) :
        height = bar.get_height()
        plt.text((bar.get_x() + bar.get_width() / 2.0), height, f'{time:.3f}', ha='center', va='bottom')
    imgPath = fullPath + "/" + imgName + "." + imgType
    fig.savefig(imgPath)
    params['imgPath'] = imgPath

    return params

#verilen yil ve yaris ve belirli tur icin istenen pilotlarin tur surelerini gorsellestirir ve istenen path'e kaydeder
def lapTimes(params):
    year = params['year'];round = params['round'];pilotsRaw = params['pilots'];lapNumber = params['lapNumber'];
    pilots = pilotsRaw.split("%")
    url = "http://ergast.com/api/f1/"+str(year)+"/"+str(round)+"/laps/"+str(lapNumber)+".json"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    dict = json.loads(response.text)
    laps = dict['MRData']['RaceTable']['Races'][0]['Laps'][0]['Timings']

    times = {}
    for lap in laps:
        driver = lap['driverId']
        if driver in pilots:
            minute, sec = lap['time'].split(":")
            times[driver] = float(minute)*60+float(sec)

    fig = plt.figure(dpi=100, figsize=(14, 7))
    ax = fig.add_subplot(111)
    ax.set_title("Year: " + year + " Round: " + round + "Lap Number: "+lapNumber+" Lap Times")
    sortedNames = times.keys()
    lapTimes_ = list(times.values())
    low = min(lapTimes_)
    high = max(lapTimes_)
    plt.ylim([math.ceil(low - 0.5 * (high - low)) - 3, math.ceil(high + 0.5 * (high - low))])
    bars = ax.bar(sortedNames, lapTimes_, color=colors)
    for bar, time in zip(bars, lapTimes_) :
        height = bar.get_height()
        plt.text((bar.get_x() + bar.get_width() / 2.0), height, f'{time:.3f}', ha='center', va='bottom')
    imgPath = fullPath + "/" + imgName + "." + imgType
    fig.savefig(imgPath)
    params['imgPath'] = imgPath

    return params

#verilen sezon ve yarisin ilk ucunu gorsellestir
def sessionEnd(params):
    year = params['year'];round = params['round'];
    url = "http://ergast.com/api/f1/"+str(year)+"/"+str(round)+"/results"+".json"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    dict = json.loads(response.text)
    topThree = dict['MRData']['RaceTable']['Races'][0]['Results'][0:3]
    names = []
    for driver in topThree:
        name = driver['Driver']['driverId']
        names.append(name)

    fig = plt.figure(dpi=100, figsize=(14, 7))
    ax = fig.add_subplot(111)
    ax.set_title("Year: "+year+" Round: "+round+" Top Three")
    sortedNames =[names[1],names[0],names[2]]
    bars = ax.bar(sortedNames, [2,3,1], color=["silver","gold","#b08d57"])
    for bar in bars:
        height = bar.get_height()
        plt.text((bar.get_x() + bar.get_width() / 2.0), height, f'{4-height:.0f}', ha='center', va='bottom')
    plt.tick_params(left=False, labelleft=False)
    imgPath = fullPath+"/"+imgName+"."+imgType
    fig.savefig(imgPath)
    params['imgPath'] = imgPath

    return params

#verilen yaristan sonra ilk x pilotun puan durumlarini gorsellestir
def pilotStandings(params):
    year = params['year'];round = params['round'];limit = int(params['limit']);
    if limit > 20:#there are 20 drivers
        limit = 20
    elif limit < 1:
        limit = 1
    url = "http://ergast.com/api/f1/"+str(year)+"/"+str(round)+"/driverStandings"+".json"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    dict = json.loads(response.text)
    pilots = dict['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

    counter = 0
    standings = {}
    for pilot in pilots:
        counter += 1
        name = pilot['Driver']['driverId']
        standings[name] = int(pilot['points'])
        if (counter == limit):
            break

    fig = plt.figure(dpi=100, figsize=(14, 7))
    ax = fig.add_subplot(111)
    ax.set_title("Year: " + year + " Round: " + round + " Pilot Standings")
    sortedNames = standings.keys()
    points = list(standings.values())
    low = min(points)
    high = max(points)
    plt.ylim([max(math.ceil(low - 0.5 * (high - low)) - 3, 0), math.ceil(high + 0.5 * (high - low))])
    bars = ax.bar(sortedNames, points, color=colors)
    for bar, point in zip(bars, points) :
        height = bar.get_height()
        plt.text((bar.get_x() + bar.get_width() / 2.0), height, f'{point:.0f}', ha='center', va='bottom')
    imgPath = fullPath + "/" + imgName + "." + imgType
    fig.savefig(imgPath)
    params['imgPath'] = imgPath

    return params

#verilen yaristan sonra ilk x takimin puan durumlarini gorsellestir
def constructorStandings(params):
    year = params['year'];round = params['round'];limit = int(params['limit']);
    if limit > 10:#there are 10 teams
        limit = 10
    elif limit < 1:
        limit = 1
    url = "http://ergast.com/api/f1/"+str(year)+"/"+str(round)+"/constructorStandings"+".json"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    dict = json.loads(response.text)
    teams = dict['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    counter = 0
    standings = {}
    for team in teams:
        counter += 1
        name = team['Constructor']['constructorId']
        standings[name] = int(team['points'])
        if (counter == limit):
            break

    fig = plt.figure(dpi=100, figsize=(14, 7))
    ax = fig.add_subplot(111)
    ax.set_title("Year: " + year + " Round: " + round + " Constructor Standings")
    sortedNames = standings.keys()
    points = list(standings.values())
    low = min(points)
    high = max(points)
    plt.ylim([max(math.ceil(low - 0.5 * (high - low)) - 3, 0), math.ceil(high + 0.5 * (high - low))])
    bars = ax.bar(sortedNames, points, color=colors)
    for bar, point in zip(bars, points) :
        height = bar.get_height()
        plt.text((bar.get_x() + bar.get_width() / 2.0), height, f'{point:.0f}', ha='center', va='bottom')
    imgPath = fullPath + "/" + imgName + "." + imgType
    fig.savefig(imgPath)
    params['imgPath'] = imgPath

    return params