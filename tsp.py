import numpy as np

# d should be an integer. d=0 means that the function will find the closest point at each iteration.
# d=1 means the function will find the second closest point, etc.
def solveTSP(arr,d):
    visitedIndices = []
    distanceSum = 0
    rowNum = 0
    while len(visitedIndices) <= len(arr) - 2:
        visitedIndices.append(rowNum)

        # create dictionary from active row, with column index as keys
        rowDict = {k:v for k,v in enumerate(arr[rowNum]) if k not in visitedIndices}

        # pull key value pair of d-lowest value (zero has already been excluded by appending rowNum to visitedIndices)
        # l is computed as d, until the length of the available points drops below d.
        remainingIndexCount = len(rowDict)
        l = min(d,remainingIndexCount-1)
        lowestValue = sorted(rowDict.items(),key=lambda x: x[1])[l]

        distanceSum += lowestValue[1]
        rowNum = lowestValue[0]

    distanceSum += arr[rowNum][0]
    
    return visitedIndices