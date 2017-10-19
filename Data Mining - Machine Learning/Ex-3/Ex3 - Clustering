import math
import numpy
from itertools import chain

def randomIntegersUsingRandom(length=2):
    import random
    randTuple = [random.randint(2, 20) for i in range(length)]
    return randTuple

class point(object):
    def __init__(self, pointCords):
        self.pointCords = pointCords

    def GetDimensionOfPoint(self):
        self.DimenstionOfPoint = len(self.pointCords)
        #print(self.DimenstionOfPoint)

    @classmethod
    def distance_from_origin(self, P1, P2):
        #print("P1 : " + str(P1.pointCords))
        #print("P2 : " + str(P2.pointCords))
        numOfPointsInP1 = sum(1 for x in P1.pointCords if isinstance(x, list))
        numOfPointsInP2 = sum(1 for x in P2.pointCords if isinstance(x, list))
        distance = math.inf
        if numOfPointsInP1 > 0:
            if numOfPointsInP2 > 1:
                for point1 in P1.pointCords:
                    for point2 in P2.pointCords:
                        tempDist = 0
                        for cord1, cord2 in zip(point1, point2):
                            #print("[" + str(cord1) + " , " + str(cord2) + "]")
                            tempDist += (cord2 - cord1) ** 2
                        distance = min(distance, tempDist)
            else:
                #print("Only P1")
                for point1 in P1.pointCords:
                    tempDist = 0
                    for cord1, cord2 in zip(point1, P2.pointCords):
                        #print("[" + str(cord1) + " , " + str(cord2) + "]")
                        tempDist += (cord2 - cord1) ** 2
                    distance = min(distance, tempDist)

        elif numOfPointsInP2 > 0:
            #rint("Only P2")
            for point2 in P2.pointCords:
                tempDist = 0
                for cord1, cord2 in zip(P1.pointCords, point2):
                    #print("[" + str(cord1) + " , " + str(cord2) + "]")
                    tempDist += (cord2 - cord1) ** 2
                distance = min(distance, tempDist)
        else:
            tempDist = 0
            for cord1, cord2 in zip(P1.pointCords, P2.pointCords):
                # print("[" + str(cord1) + " , " + str(cord2) + "]")
                tempDist += (cord2 - cord1) ** 2
            distance = tempDist
        return(math.sqrt(distance))


def printMatrix(matrix):
    if len(matrix) > 1:
        print("\nThe Distances Matrix is :")
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))

def distanceMatrixMaker(points, newCluster = None):
    numberOfPoints = len(points)
    distMatrix = numpy.zeros((numberOfPoints, numberOfPoints))
    numpy.fill_diagonal(distMatrix, numpy.inf)
    for i, pointCords in enumerate(points):
        curPoint = point(pointCords)
        otherPoints = points[i + 1:]
        for j, rowPointCords in enumerate(otherPoints):
            otherPointInRow = point(rowPointCords)
            #print("Checking between : " + str(curPoint.pointCords) + " and " + str(otherPointInRow.pointCords))
            distance = point.distance_from_origin(curPoint, otherPointInRow)
            distance = format(distance, '.2f')
            distMatrix[i][j + i + 1] = distMatrix[j + i + 1][i] = distance
            #printMatrix(distMatrix)
    print("++++++++++++++++++")
    return distMatrix

def clustering(clusteredMatrix, points, numberOfPoints):
    while (len(points) > 1):
        print("+++++++++++++++++++\n" + str(points))
        minIndex = numpy.argmin(clusteredMatrix)
        minRowIndex = int(minIndex / numberOfPoints)
        minColIndex = (minIndex - (minRowIndex * numberOfPoints))
        print("\nMin Value is at position : [" + str(minRowIndex) + "][" + str(minColIndex) + "] = " + str(
            clusteredMatrix[minRowIndex, minColIndex]))
        print("combining  " + str(points[minRowIndex]) + " With " + str(points[minColIndex]))
        clustersList[minRowIndex] = (clustersList[minRowIndex], clustersList[minColIndex])
        numOfListsInPoint1 = sum(1 for x in points[minRowIndex] if isinstance(x, list))
        numOfListsInPoint2 = sum(1 for x in points[minColIndex] if isinstance(x, list))
        if numOfListsInPoint1 == 0 :
            points[minRowIndex] = [points[minRowIndex][i:i + 2] for i in range(0, len(points[minRowIndex]), 2)]
            if numOfListsInPoint2 == 0:
                points[minRowIndex].append(points[minColIndex])
            else:
                points[minRowIndex] += points[minColIndex]
        elif numOfListsInPoint2 == 0:
            points[minRowIndex].append(points[minColIndex])
        else:
            points[minRowIndex] += points[minColIndex]
        print("New content is : " + str(points[minRowIndex]))
        del points[minColIndex]
        del clustersList[minColIndex]
        numberOfPoints -= 1
        # print(points)
        clusteredMatrix = distanceMatrixMaker(points, points[minRowIndex])
        printMatrix(clusteredMatrix)
    return clustersList

if __name__ == "__main__":
    numberOfPoints = 100
    points = [list(randomIntegersUsingRandom()) for i in range(numberOfPoints)]
    #for i, point in enumerate(points):
    #    points[i] = [points[i][j:j + 2] for j in range(0, len(points[i]), 2)]
    #new_list = [points[i:i + 2] for i in range(0, len(points), 2)]
    clustersList = list(points)
    print (points)
    distMatrix = distanceMatrixMaker(points)
    printMatrix(distMatrix)
    print("+++++++++++\n")
    clusteredMatrix = distMatrix
    print("The Final Cluster is : " + str(clustering(clusteredMatrix, points, numberOfPoints)))


