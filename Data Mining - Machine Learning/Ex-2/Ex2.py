import csv
import numpy

def randomIntegersUsingRandom(length=2):
    import random
    return [random.randint(2, 20) for i in range(length)]

class OneAndTwo(object):
    def ReadCsv(self, csvFileName):
        with open(csvFileName, 'r') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            data_read = numpy.array([ list(map(int, row)) for row in reader])
        return data_read

    def Calculations(self, data_read):
        for line in data_read:
            maxValue = max(line)
            minValue = min(line)
            avgValue = numpy.mean(line)
            medianValue = numpy.median(line)
            print("Max : " + str(maxValue) + " Min : " + str(minValue) + " Avg : " + str(avgValue) + " Median : " +
                  str(medianValue) + " For line : " + str(line))

if __name__ == "__main__":
    OneAndTwo = OneAndTwo()
    csvFileName = 'C:\\Users\\mmanor\\PycharmProjects\\DataMining\\Ex2File.csv'
    data_read = OneAndTwo.ReadCsv(csvFileName)
    print("The content of the csv file is :\n")
    print(data_read)
    print("\nNow lets calculate some data...\n++++++++++++++++++\n\n")
    OneAndTwo.Calculations(data_read)

