import bus

file = open("loop_log_2017_05_17", "r")
buses = {}
for line in file:
    aline = line.split(" ")
    if aline[0] not in buses:
        new = bus.Bus(aline[0])
        buses.update({aline[0]:new})
    if "Home" not in aline[1] and aline[1] != buses[aline[0]].getMostRecentLocation():
        buses[aline[0]].addLog(aline[1], aline[2], aline[3], aline[4])
        buses[aline[0]].checkDirection()
        buses[aline[0]].getMostRecentLocationObj().direction = buses[aline[0]].getDirection()
    
for key, bus in buses.items():
    bus.printReport()
    #bus.printLogs()