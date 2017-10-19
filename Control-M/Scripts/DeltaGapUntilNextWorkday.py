import sys
import datetime

def calcDelta(firstDate, secondDate):
    if isinstance(firstDate, datetime.date) and isinstance(secondDate, datetime.date):
        datesDiff = abs(firstDate - secondDate)
        return(datesDiff.days)
    else:
        raise ValueError("one or more of the inputs isn't datetime format! exiting with code 2", 2)

def getNextWorkDate(varName):
    import subprocess as subp
    ctmvarCommand = ['ctmvar', '-action', 'list']
    try:
        ctmvarOutput = subp.Popen(ctmvarCommand,stdout=subp.PIPE, shell=True)
        out, err = ctmvarOutput.communicate()
        splittedLines = out.splitlines()[5:-3]
        varsTable = []
        isFound = False
        for line in splittedLines:
            line = line.decode('ascii').split()
            varsTable.append(line)
            # print(line)
            if varName == line[0]:
                isFound = True
                print("Found the following line : " + str(line))
                nextWorkDate = line[1]
                pass
        if not isFound:
            print("Something went wrong! no matching found...\nFollowing the global variables table :\n")
            for line in varsTable:
                print(line)
            raise Exception("Exiting with code 4!", 4)
        else:
            return(nextWorkDate)
    except:
        raise Exception("Error : Something went wrong with ctmvar command...Exiting with code 1 !", 1)


if __name__ == "__main__":
    varName = "%%NextWorkDate"
    today = datetime.date.today()
    print("Today is :" + str(today))
    try:
        print("Going to search for existence of " + varName + " in ctmvar output...")
        nextWorkDate = getNextWorkDate(varName)
        #nextWorkDate = "2017109"
        nextWorkDate = datetime.datetime.strptime(nextWorkDate, '%Y%m%d').date()
        print("Next WorkDate is : " + str(nextWorkDate))
        if nextWorkDate > today:
            dateDiff = calcDelta(today, nextWorkDate)
            print("Number of days until next working date is  : " + str(dateDiff))
            if dateDiff > 5:
                raise ValueError("Error : Dates diff cannot be more than 5! Exiting with code 5", 5)
        else:
            raise ValueError("Error : Next work date should be bigger then today's date! Exiting with code 3", 3)
    except Exception as e:
        exception = e.args[0]
        print(exception)
        if len(e.args) > 1 :
            exitCode = e.args[1]
            exit(exitCode)
        else:
            raise
