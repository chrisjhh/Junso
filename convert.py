"""Script to convert the stopwarch file to csv files that can be imported"""
from .parser import parse
from .Record import Record


def convert(path):
    f = open(path, "r")
    records = parse(f)
    f.close()
    for r in records:
        filename = r.date.isoformat() + "_" + str(r.id) + ".csv"
        print(filename)
        out = open(filename, "w")
        for s in r.splits:
            out.write(str(s).replace("'",":") + "\n")
        s = r.total_time
        out.write(str(s).replace("'",":") + "\n")
        out.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Specify filename to convert")
        exit(1)
    convert(sys.argv[1])
