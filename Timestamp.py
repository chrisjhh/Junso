"""Class representing a timestamp h:mm'ss.xx"""
import re

pattern = re.compile(r"(\d):(\d{2})'(\d{2}.\d{2})")

class Timestamp:

    def __init__(self, value):
        if type(value) is str:
            self.value = parse(value)
        else:
            self.value = float(value)

    def __float__(self):
        return self.value

    def __str__(self):
        hour = 0
        val = self.value
        if val >= 3600:
            hour = int(val / 3600)
            val -= 3600 * hour
        mins = 0
        if val >= 60:
            mins = int(val / 60)
            val -= 60 * mins
        return "{0:d}:{1:02d}'{2:02.2f}".format(hour,mins,val)

    def __add__(self, other):
        return Timestamp(self.value + float(other))

    def __sub__(self, other):
        return Timestamp(self.value - float(other))

def parse(value):
    """"Parse a timestamp in the format h:mm'ss.xx"""
    global pattern
    match = pattern.match(value)
    if not match:
        raise ValueError("Timestamp must be in h:mm'ss.xx format")
    hour = int(match.group(1))
    mins = int(match.group(2))
    secs = float(match.group(3))
    return  hour * 3600 + mins * 60 + secs

if __name__ == "__main__":
    t = Timestamp("0:01'30.20")
    print(t)
    print(t.value)
    print(float(t))
    print(t - 20.2)
    t2 = Timestamp("0:00'40.30")
    print(t + t2)
    print(t - t2)
    