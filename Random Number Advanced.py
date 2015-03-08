## Init - Imports and Variables
from random import randrange
from time import sleep
import datetime
import os
import logging
run = "y"
hadToCreateDir = False
hadToCreateLog = False
hadToCreateDebug = False
hadToCreateResults = False
paths = []
kbint = False

## Init - File Paths
# AppData Paths Location
paths.append(os.path.expanduser("~user"))
paths.append(os.path.join(paths[-1], "AppData"))
paths.append(os.path.join(paths[-1], "Roaming"))
paths.append(os.path.join(paths[-1], "Internet's Programs"))
paths.append(os.path.join(paths[-1], "RandomNumber"))
# File Paths
logfilepath = paths[-1] + "/randnum.log"
debugfilepath = paths[-1] + "/randnumdebug.log"
resultsfilepath = paths[-1] + "/randnumresults.txt"
templog = paths[-1] + "/templog.temp"

## Function - Error Catching
def toIntRetry(value):
    try:
        value = int(value)
    except ValueError:
        print("The value you just entered cannot be changed into a number.")
        value = toIntRetry(input("Please enter a numerical value: "))
    finally:
        return(value)
print("Preparing Program...")
sleep(1)
## Checking and Creation of files and folders.
# AppData Folder.
for i in paths:
    if not os.path.exists(i):
        os.mkdir(i)
        hadToCreateDir = True
# Logging File - Update if there.
if not os.path.exists(logfilepath):
    hadToCreateLog = True
    log = open(logfilepath, "w")
    log.close()
if not hadToCreateLog:
    log = open(logfilepath, "a")
    log.write("\n")
    log.close()
# Debug Log File - Update if there.
if not os.path.exists(debugfilepath):
    hadToCreateDebug = True
    debug = open(debugfilepath, "w")
    debug.close()
if not hadToCreateDebug:
    debug = open(debugfilepath, "a")
    debug.write("\n")
    debug.close()
# Results File - Open if there.
if not os.path.exists(resultsfilepath):
    hadToCreateResults = True
resultsfile = open(resultsfilepath, "w")

## Setup Logging.
# Basic Setup.
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                datefmt='%m-%d %H:%M',
                filename=templog,
                filemode='w')
# Setup Handlers.
debugfile = logging.FileHandler(filename = debugfilepath)
debugfile.setLevel(logging.DEBUG)
logfile = logging.FileHandler(filename = logfilepath)
logfile.setLevel(logging.INFO)
# Formatters.
fileformatter = logging.Formatter("%(levelname)s:%(name)s:%(asctime)s: %(message)s", datefmt = '%y-%m-%d %H:%M:%S')
consoleformatter = logging.Formatter("%(levelname)s: %(message)s")
# Set Formatter to Handler.
logfile.setFormatter(fileformatter)
debugfile.setFormatter(fileformatter)
# Add Handlers to Root Logger.
logging.getLogger("").addHandler(logfile)
logging.getLogger("").addHandler(debugfile)
# Preparing Loggers.
log_prep = logging.getLogger("Preparation")
log_running = logging.getLogger("Application")

## File Preperation Logs.
log_prep.info("Program Started")
log_prep.info("Logging Started")
if hadToCreateDir:
    log_prep.warning("AppData Folder Created @ "+folder)
    sleep(0.2)
if hadToCreateLog:
    log_prep.warning("Log File Created @ "+logfilepath)
    sleep(0.3)
if hadToCreateDebug:
    log_prep.warning("Debug File Created @ "+debugfilepath)
    sleep(0.2)
if hadToCreateResults:
    log_prep.warning("Results File Created @ "+resultsfilepath)
    sleep(0.4)

log_prep.debug("Locating Directories / Folders")
sleep(1)
log_prep.debug("AppData Folder Located @ "+folder)
sleep(0.2)
log_prep.debug("Log File Located @ "+logfilepath)
sleep(0.2)
log_prep.debug("Temp Log File Located @ "+templog)
sleep(0.2)
log_prep.debug("Debug File Located @ "+debugfilepath)
sleep(0.2)
log_prep.debug("Results File Located @ "+resultsfilepath)
sleep(0.2)
log_prep.debug("All Directories / Folders Found.")

## Code Startup
try:
    print("Random Number Generator")
    run = input("Do you wish to start? (Y/N) ").lower()
    while run == "y":
        log_running.info("User Ran Program")
        log_running.debug("Setting Variables")
        resultsfile = open(resultsfilepath, "w")
        results = []
        runconf = "n"
        printconf = "n"
        log_running.debug("Results File Opened in Write Mode.")
        log_running.debug("Results List Emptied.")
        log_running.debug("Run Confirmation set to ""No""")
        log_running.debug("Print Confirmation set to ""No""")
        log_running.debug("Variables Set")
        log_running.info("All Variables Set. Ready to Run.")
        number = toIntRetry(input("Enter Number of Results: "))
        log_running.debug("User Input Checked - Is Number.")
        log_running.info("User Input: "+str(number))
        while number > 20000001 or number < 1:
            log_running.warning("Value Error: Value Above 20,000,000 or below 1.")
            if number > 20000001:
                prenum = number
                number = toIntRetry(input("Enter a number under 20,000,000: "))
                log_running.debug("User Input Changed from "+str(prenum)+" to "+str(number))
                del prenum
            if number < 1:
                prenum = number
                number = toIntRetry(input("Enter a positive number: "))
                log_running.debug("User Input Changed from "+str(prenum)+" to "+str(number))
                del prenum
        log_running.info("User Input Fixed / Was Correct.")
        minimum = toIntRetry(input("Enter a Minimum Value: "))
        maximum = toIntRetry(input("Enter a Maxmimum Value: "))
        while minimum > maximum:
            log_running.warning("Value Error: Minimum Larger than Maximum.")
            print("Minimum value must be less than the maximum value.")
            minimum = toIntRetry(input("Minimum Value: "))
            maximum = toIntRetry(input("Maximum Value: "))
        if number > 1000001:
            print("There are a large number of results to calculate, which can take time and system resources.")
            runconf = input("Are you sure you wish to continue? (Y/N) ").lower()
            log_running.warning("Large Number of Results to Calculate.")
        else:
            runconf = "y"
            log_running.info("Small / Normal Number of Results to Calculate.")
        if runconf == "y":
            if number > 1000001:
                log_running.info("User Confirmed Calculation - Number Greater than 1,000,000.")
            else:
                log_running.info("Auto Confirmed Calculation - Number Less than 1,000,000.")
            for i in range(0, number):
                result = randrange(minimum, maximum+1)
                log_running.debug("Result "+str(i+1)+": "+str(result))
                results.append(result)
            if number > 191:
                print("There are a large number of resuts.")
                printconf = input("Do you wish to view the results? (Y/N) ").lower()
                log_running.warning("Large Number of Results to View.")
            else:
                printconf = "y"
                log_running.info("Small / Normal Number of Results to View.")
            if printconf == "y":
                if number > 191:
                    log_running.info("User Confirmed Viewing - Number Greater than 190.")
                else:
                    log_running.info("Auto Confirmed Viewing - Number Less than 191.")
                x = len(results)
                for i in range(0, x):
                    print("Result "+str(i+1)+": "+str(results[i]))
                input("Press Enter to Exit.")
            x = len(results)
            log_running.info("Printing Results")
            for i in range(0, x):
                resultsfile.write("Result "+str(i+1)+": "+str(results[i])+"\n")
                log_running.debug("Writing Result "+str(i+1)+" to file: "+str(results[i]))
            resultsfile.write("\n--[Summary]--")
            resultsfile.write("\nResults: "+str(number))
            resultsfile.write("\nMinimum: "+str(minimum))
            resultsfile.write("\nMaximum: "+str(maximum))
            resultsfile.close()
            log_running.info("Results File Closed.")
        run = "n"
finally:
    log_prep.warning("Shutting Down Logging.")
    log_running.warning("Application Shutting Down.")
    log_prep.warning("Application Shut Down.")
    log_prep.warning("Deleting Temp Log File.")
    log_prep.warning("Logging Ended.")
    logging.shutdown()
    os.remove(templog)
    resultsfile.close()
