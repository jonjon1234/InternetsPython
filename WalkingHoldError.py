import os # Import OS, for os.walk
import datetime # Import datetime, for datetime.now function.
from time import sleep as slp # Import the sleep function
scanfile = 0 # We haven't scanned any files yet.
scanned = [] # And we havn't scanned any drives.
start = datetime.datetime.now() # Record the start time.

try: # Yay for error catching.
    start = datetime.datetime.now() # Record the start time, again?
    for i in range(65, 91): # Find the drives.
        path = chr(i)+"://" # Make them real paths.
        if os.path.exists(path): # Check for media.
            scanned.append("Drive Scanned: "+chr(i)) # Add it to the scanned drive list.
            for dir_, _, files in os.walk(path): # Then walk through the drive.
                for file in files: # For every file.
                    print(os.path.join(dir_, file)) # Print to the screen.
                    slp(0.005) # Then sleep for a split second.
                    scanfile = scanfile + 1 # And we scanned another file.
    end = datetime.datetime.now() # Record the end time.
    running = end - start # And therefore the time taken.
    print() # Make a nice new line.
    print("Files Scanned: "+str(scanfile)) # We scanned XYZ files.
    print("Time to Complete: "+str(running)) # And it took ABC minutes.
    for a in scanned: # Finally, make a nice drives scanned listing.
        print(a) # As above.
    input("Press Enter to finish") # Then make an input to finish.
except BaseError as errored: # BUT, if we error.
    print(errored) # Catch and print the error for me.
    input() # Then call an input to keep the console up.
