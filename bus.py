import json
with open("stops.json", encoding="utf-8") as stops_info:
    json = json.loads(stops_info.read())

all = json["Stops"]
all.update(json["Sections"])

class Location:
    def __init__(self, location, status, time, direction):
        self.location = location
        self.status = status
        self.time = time
        self.direction = direction

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.location, self.status, self.time, self.direction)

    def getLocation(self):
        return self.location

    def getLocationId(self):
        return all[self.location]["id"]

    def getStatus(self):
        return self.status

    def getTime(self):
        return self.time

    def printString(self):
        print(self.location, self.status, self.time)


class Bus:
    CW = 1
    CCW = 2
    def __init__(self, id):
        self.id = id
        self.locations = []
        self.direction = 0

    def getId(self):
        return self.id

    def getDirection(self):
        return self.direction

    def getMostRecentLocation(self):
        if len(self.locations) != 0:
            return self.locations[len(self.locations) - 1].getLocation()
        return ""

    def getLocationLog(self):
        return self.locations

    def addLog(self, location, status = None, time = None, direction = None):
        if (status == None):
            self.locations.append(location)
        else:
            log = Location(location, status, time, direction)
            self.locations.append(log)

    def checkDirection(self):
        if len(self.locations) > 1:
            MRT = self.locations[len(self.locations) - 1].getLocationId()
            SMRT = self.locations[len(self.locations) - 2].getLocationId()
            if MRT - SMRT > 0:
                self.direction = 2
            elif MRT - SMRT < 0:
                self.direction = 1
            else:
                pass

    def printReport(self):
        print("Bus ID " + str(self.id))
        for location in self.locations:
            print(location, end = "")

    def printLogs(self):
        for location in self.locations:
            print(location, end = "")
