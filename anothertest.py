import json
import requests
import time
import datetime
import bus


def findLocation(lat, lon):
    for area in all:
        if (all[area]["north_bound"] > lat):
            if (all[area]["west_bound"] < lon):
                if (all[area]["south_bound"] < lat):
                    if (all[area]["east_bound"] > lon):
                        return area


with open("stops.json", encoding="utf-8") as stops_info:
    json = json.loads(stops_info.read())

all = json["Stops"]
all.update(json["Sections"])
buses = {}

while True:
    try:
        log_name = "loop_log_" + datetime.datetime.now().strftime("%Y_%m_%d")
        log = open(log_name, "a")
        r = requests.get("http://bts.ucsc.edu:8081/location/get")
        real_time_data = r.json()

        for data in real_time_data:
            location = findLocation(data["lat"], data["lon"])
            if location != None:

                id = data["id"]
                type = data["type"].replace(" ", "_")
                if id not in buses:
                    new = bus.Bus(id)
                    buses.update({id: new})
                if location != buses[id].getMostRecentLocation():
                    check = True
                else:
                    check = False
                buses[id].addLog(location, type,
                                 datetime.datetime.now().strftime("%H:%M:%S"),buses[id].getDirection())
                if check:
                    buses[id].checkDirection()
                out = "{} {}".format(id, buses[id].getMostRecentLocationObj())
                log.write(out)
                log.write("\n")
                print(out)
        log.closed
    except Exception as e:
        print(e)
        print("Network Error")
        pass

    time.sleep(8)
