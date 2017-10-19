import shutil, os, time

relevantPath = "SourcePath"
destDir = "DestPath"
includedExtenstions = ['csv', 'txt', 'xls', 'xlsx']
numberOfFileSizeChecks = 3
timeBetweenSearches = 10
print("Searching for files with extensions: " + str(includedExtenstions))
fileNames = [fn for fn in os.listdir(relevantPath)
             if any(fn.endswith("." + ext) for ext in includedExtenstions)]

if not fileNames:
    print("No file is matching the search...exiting with code 99")
    exit(99)
else:
    fileNames.sort(key=lambda x: os.path.getctime(os.path.join(relevantPath, x)))
    print("The following files were found matching the extension: ")
    for file in fileNames:
        print(file)
    oldestFile = fileNames[0]
    print("\n\nThe oldest file is : " + oldestFile)
    fileSize = os.path.getsize(relevantPath + oldestFile)
    print("File size is : " + str(fileSize))
    numberOfSuccessSizeChecks = 0
    for i in range(numberOfFileSizeChecks):
        print("Sleeping for " + str(timeBetweenSearches) + " seconds...")
        time.sleep(timeBetweenSearches)
        prevFileSize = fileSize
        fileSize = os.path.getsize(relevantPath + oldestFile)

        if fileSize == prevFileSize:
            numberOfSuccessSizeChecks += 1
            print("File size is still static")
            continue
        else:
            print("ERROR: File size isn't static...current size is  " + str(
                fileSize) + " While the last size was : " + prevFileSize + "\nWill be checked again on next job run...")
            exit(99)

    print("\n\nThe size is static for " + str(
        numberOfFileSizeChecks * timeBetweenSearches) + " seconds\nThe file is going to be moved to " + destDir)

    destDirContent = os.listdir(destDir)
    if destDirContent:
        print("ERROR : Destination folder isn't empty!!! cannot continue")
        exit(2)

    try:
        shutil.copy(relevantPath + oldestFile, destDir)
        print("file " + oldestFile + " Moved to " + destDir)
        try:
            shutil.move(relevantPath + oldestFile, relevantPath + "Done\\")
            print("file " + oldestFile + " BackedUp to " + relevantPath + "Done\\")
        except:
            print("ERROR: Failed To BackUp the file")
            exit(5)
    except:
        print("ERROR: Failed to copy the file to " + destDir + "...  Try again")
        exit(3)
