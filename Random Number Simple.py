## Init - Imports and Variables
from random import randrange
from time import sleep
resultsfilepath = "results.txt"
resultsfile = open(resultsfilepath, "w")

## Function - Error Catching
def toIntRetry(value):
    try:
        value = int(value)
    except ValueError:
        print("The value you just entered cannot be changed into a number.")
        value = toIntRetry(input("Please enter a numerical value: "))
    finally:
        return(value)

## Code Startup
print("Random Number Generator")
run = input("Do you wish to start? (Y/N) ").lower()
while run == "y":
    results = []
    runconf = "n"
    printconf = "n"
    number = toIntRetry(input("Enter Number of Results: "))
    while number > 20000001 or number < 1:
        if number > 20000001:
            number = toIntRetry(input("Enter a number under 20,000,000: "))
        if number < 1:
            number = toIntRetry(input("Enter a positive number: "))
    minimum = toIntRetry(input("Enter a Minimum Value: "))
    maximum = toIntRetry(input("Enter a Maxmimum Value: "))
    while minimum > maximum:
        print("Minimum value must be less than the maximum value.")
        minimum = toIntRetry(input("Minimum Value: "))
        maximum = toIntRetry(input("Maximum Value: "))
    if number > 1000001:
        print("There are a large number of results to calculate, which can take time and system resources.")
        runconf = input("Are you sure you wish to continue? (Y/N) ").lower()
    else:
        runconf = "y"
    if runconf == "y":
        for i in range(0, number):
            result = randrange(minimum, maximum+1)
            results.append(result)
        if number > 191:
            print("There are a large number of resuts.")
            printconf = input("Do you wish to view the results? (Y/N) ").lower()
        else:
            printconf = "y"
        if printconf == "y":
            x = len(results)
            for i in range(0, x):
                print("Result "+str(i+1)+": "+str(results[i]))
            input("Press Enter to Exit.")
        x = len(results)
        for i in range(0, x):
            resultsfile.write("Result "+str(i+1)+": "+str(results[i])+"\n")
        resultsfile.write("\n--[Summary]--")
        resultsfile.write("\nResults: "+str(number))
        resultsfile.write("\nMinimum: "+str(minimum))
        resultsfile.write("\nMaximum: "+str(maximum))
        resultsfile.close()
    run = "n"
resultsfile.close()
