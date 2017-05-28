import timeline
import bus
import datetime


class Map:
    def __init__(self, mode):
        self.school = []
        self.mode = mode
        for i in range(65):
            tl = timeline.timeline()
            tl.setMode(mode)
            self.school.append(tl)

    def insert(self, location_A, location_B):
        # info about two locations
        start = location_A.getLocationId()
        end = location_B.getLocationId()
        location_difference = abs(start - end)
        if location_difference > 60:
            location_difference = abs(64 - location_difference)
        # find duration
        time_A = location_A.getTime()
        time_B = location_B.getTime()
        time_num_A = datetime.datetime.strptime(time_A, "%H:%M:%S")
        time_num_B = datetime.datetime.strptime(time_B, "%H:%M:%S")
        duration = (time_num_B - time_num_A).seconds
        duration /= location_difference
        if duration > 8 * 60:
            return 0
        # find the timeslot
        second = (time_num_B - datetime.datetime(1970, 1, 1)).seconds
        # find the direction
        direction = location_B.getDirection()
        # insert!
        #print(second, duration, direction)
        if direction != 0:
            for i in range(location_difference):
                if direction == 1:
                    offset = end + i
                    if offset > 64:
                        offset -= 64
                    self.school[offset].insert(second, duration, direction)
                elif direction == 2:
                    offset = start - i
                    if offset < 1:
                        offset += 64
                    self.school[offset].insert(second, duration, direction)
                else:
                    pass

    def estimate(self, second, start_id, end_id, direction):
        est = 0
        #difference = abs(start_id - end_id)
        #if difference > 60:
            #difference = abs(64 - difference)
        while start_id != end_id:
            if direction == 1:
                est += self.school[start_id - 1].count(second, direction)
                start_id -= 1
                if start_id < 1:
                    start_id = 64
            elif direction == 2:
                est += self.school[start_id].count(second, direction)
                start_id += 1
                if start_id > 64:
                    start_id = 1
        return est

    def allEstimate(self, stop_id, running_buses, second=None):
        result = {}
        if second == None:
            second = datetime.datetime.now(
            ).hour * 60 * 60 + datetime.datetime.now(
            ).minute * 60 + datetime.datetime.now().second

        for location in running_buses:
            direction = location.getDirection()
            id = location.getLocationId()
            if stop_id == id:
                result.update({id: -1})
                continue
            if direction == 1 and stop_id > id:
                continue
            elif direction == 2 and stop_id < id:
                continue
            duration = self.estimate(second, id, stop_id, direction)
            result.update({id: duration})
        return result

    def clear(self, mode):
        self.school = []
        self.mode = mode
        for i in range(65):
            tl = timeline.timeline()
            tl.setMode(mode)
            self.school.append(tl)