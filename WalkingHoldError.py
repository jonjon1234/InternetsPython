import os
import datetime
from time import sleep as slp
scanfile = 0
scanned = []

try:
    start = datetime.datetime.now()
    for i in range(65, 91):
        path = chr(i)+"://"
        if os.path.exists(path):
            scanned.append("Drive Scanned: "+chr(i))
            for dir_, _, files in os.walk(path):
                for file in files:
                    print(os.path.join(dir_, file))
                    slp(0.005)
                    scanfile = scanfile + 1
    end = datetime.datetime.now()
    running = end - start
    print()
    print("Files Scanned: "+str(scanfile))
    print("Time to Complete: "+str(running))
    for a in scanned:
        print(a)
    input("Press Enter to finish")
except BaseError as errored:
    print(errored)
    input()
