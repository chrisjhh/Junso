"--Class to parse a records file--
import re
from .Record import Record

def parse(lines):
    records = []
    record = None
    for line in lines:
        match = re.match(r"MCH:\s+(\d{3})", line)
        if match:
            record = Record(match.group(1))
        match = re.match(r"Record Date:\s+(\d{4}-\d{2}-\d{2})", line)
        if match:
            record.setDate(match.group(1))
        match = re.search(r"Split\d+:\s+(\d:\d{2}'\d{2}.\d{2})", line)
        if match:
            record.addSplit(match.group(1))
        match = re.search(r"End Time:\s+(\d:\d{2}'\d{2}.\d{2})", line)
        if match:
            record.setTotalTime(match.group(1))
            records.append(record)
            record = None
    return records

if __name__ == "__main__":
    import os
    import os.path
    path = os.path.join(os.path.dirname(__file__),"data","test.txt")
    f = open(path)
    records = parse(f)
    for r in records:
        print(r)
