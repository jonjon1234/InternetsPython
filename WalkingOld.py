import os # Import OS, for os.walk
import datetime # Import datetime, for datetime.now function.
from time import sleep as slp # Import the sleep function
scanfile = 0 # We haven't scanned any files yet.
scanned = [] # And we havn't scanned any drives.
start = datetime.datetime.now() # Record the start time.

for i in range(65, 91): # A - Z.
    path = chr(i)+"://" # A://
    if os.path.exists(path): # If the path exists.
        scanned.append("Drive Scanned: "+chr(i)) # Yes, we scanned it.
        for dir_, _, files in os.walk(path): # Walk through every file in the directory.
            for file in files: # For each file.
                print(os.path.join(dir_, file)) # Join the file and directory path.
                scanfile = scanfile + 1 # We scanned a file.
                slp(0.005) # Sleep for a split-second.
    end = datetime.datetime.now() # At the end, record the time
    running = end - start # Run time is the ending time take the start time.
    print() # Make a spacer, for some reason.
    print("Files Scanned: "+str(scanfile)) # We scanned THIS many files.
    print("Time to Complete: "+str(running)) # And it took THIS long.

for a in scanned: # Print out the drives scanned.
    print(a) # To make the user feel special.
input("Press Enter to finish") # Nice exit thing.
