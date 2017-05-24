import datetime

class timeline:
    def __init__(self):
        self.timetable = {}

    def setMode(self, mode):
        if "MWF" in mode:
            second = 7 * 60 * 60 + 21 * 60 # 7:21 AM
            while second < 86400:
                t = timeslot()
                self.timetable.update({second: t})
                second += 13 * 60
        elif "TuTh" in mode:
            second = 7 * 60 * 60 + 22 * 60 # 7:21 AM
            while second < 86400:
                t = timeslot()
                self.timetable.update({second: t})
                second += 19 * 60

class timeslot:
    def __init__(self): # CW = 1 CCW = 2
        self.CW = []
        self.CCW = []

    def addCW(self, value):
        self.CW.append(value)

    def addCCW(self, value):
        self.CCW.append(value)

    def getAverage_CW(self):
        return sum(self.CW) / len(self.CW)

    def getAverage_CCW(self):
        return sum(self.CCW) / len(self.CCW)
