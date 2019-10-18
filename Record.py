"""A class representing a timer record"""
import datetime
from .Timestamp import Timestamp

next_counter = 1

class Record:

    def __init__(self, id=None, date=None):
        global next_counter
        if id is not None:
            self.id = int(id)
        else:
            self.id = next_counter
            next_counter += 1
        if date is not None:
            self.setDate(date)
        else:
            self.date = datetime.date.today()
        self.total_time = Timestamp(0)
        self.splits = []

    def setDate(self,date):
        if type(date) is str:
            (year,month,day) = date.split("-")
            self.date = datetime.date(int(year),int(month),int(day))
        elif type(date) is datetime.date:
            self.date = date
        else:
            raise ValueError("date is not a string or a datetime.date")
         
    def addSplit(self,tstamp):
        t = Timestamp(tstamp)
        if len(self.splits) > 0:
            last = self.splits[-1]
            if t < last:
                raise ValueError("Split time is before previous split")
        self.splits.append(t)
        if t > self.total_time:
            self.total_time = t

    def setTotalTime(self,tstamp):
        self.total_time = Timestamp(tstamp)

    def laps(self):
        last = 0
        for t in self.splits:
            v = t.value - last
            last = t.value
            yield Timestamp(v)

    def lapsAndSplits(self):
        last = 0
        for t in self.splits:
            v = t.value - last
            last = t.value
            yield (Timestamp(v), t)

    def fastestLap(self):
        return min(self.laps())

    def slowestLap(self):
        return max(self.laps())

    def averageLap(self):
        n = 0
        total = 0
        for l in self.laps():
            n += 1
            total += l.value
        if n == 0:
            return None
        return Timestamp(total/n) 

    def __str__(self):
        value = []
        value.append("MCH:       	{:03d}".format(self.id))
        value.append("")
        value.append("Record Date:\t{0}\t{1}".format(
            self.date.isoformat(), self.date.strftime("%A")
        ))
        value.append("")
        n = 0
        for (l,s) in self.lapsAndSplits():
            n += 1
            value.append("Lap{0}:\t{1}\tSplit{0}:\t{2}".format(
                n, l, s
            ))
            value.append("")
        value.append("Average Lap Time:   	{0}".format(self.averageLap()))
        value.append("Fastest Lap Time:   	{0}".format(self.fastestLap()))
        value.append("Slowest Lap Time:   	{0}".format(self.slowestLap()))
        value.append("")
        value.append("End Time:       	{0}".format(self.total_time))
        value.append("------------------------------------------------------------------------")
        value.append("")
        return "\n".join(value)
        
if __name__ == "__main__":
    r = Record()
    r.addSplit("0:00'10.54")
    r.addSplit("0:00'50.71")
    r.addSplit("0:01'12.06")
    r.setTotalTime("0:01'30.25")
    print(r)

    r2 = Record(date="2019-10-17")
    r2.addSplit("0:00'17.56")
    r2.addSplit("0:00'44.01")
    r2.addSplit("0:01'11.06")
    r2.addSplit("0:01'25.28")
    r2.setTotalTime("0:01'30.18")
    print(r2)

