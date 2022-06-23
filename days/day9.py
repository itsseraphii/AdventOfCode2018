from utils.aoc_utils import AOCDay, day

@day(9)
class Day9(AOCDay):
    # (y, x) Left, Up, Right, Down
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
    lowPoints = {}

    def common(self):
        # Build lowpoint dictionnary
        for y in range(len(self.inputData)):
            for x in range(len(self.inputData[0])):
                self.isLowPoint([y, x])

        return 0

    def part1(self):
        sum = len(self.lowPoints)
        for point in self.lowPoints.values():
            sum += point.get('height')

        return sum
    
    def part2(self):
        basinSizeArray = []
        for point in self.lowPoints.values():
            basinDict = {}
            self.getBasinSize([point.get('y'), point.get('x')], basinDict)
            basinSizeArray.append(len(basinDict))
            
        basinSizeArray.sort(reverse=True)

        return basinSizeArray[0] * basinSizeArray[1] * basinSizeArray[2]

    def isLowPoint(self, position):
        for direction in self.directions:
            hasLowerHeight = self.hasLowerHeight(position, direction)

            if hasLowerHeight == None:
                continue
            elif hasLowerHeight == True:
                return 0

        # Is a low point, add to low dictionnary
        self.lowPoints[str(position)] = {
            'height': int(self.inputData[position[0]][position[1]]),
            'y': position[0],
            'x': position[1]
        }

        return 0

    def getDirectionCoords(self, position, direction):
        return [position[0] + direction[0], position[1] + direction[1]]

    def getHeightValue(self, position):
        return int(self.inputData[position[0]][position[1]])

    # Check if the position has a lower neighboor in a direction
    def hasLowerHeight(self, position, direction):
        # y, x
        directionCoords = self.getDirectionCoords(position, direction)

        # Neighboor is a low point
        if (str(directionCoords) in self.lowPoints):
            return True

        # Catch out of bounds
        if (direction == self.directions[0] and directionCoords[1] < 0
        or direction == self.directions[1] and directionCoords[0] >= len(self.inputData) 
        or direction == self.directions[2] and directionCoords[1] >= len(self.inputData[0]) 
        or direction == self.directions[3] and directionCoords[0] < 0):
            return None

        positionValue = self.getHeightValue(position)
        directionValue = self.getHeightValue(directionCoords)

        return positionValue >= directionValue


    def getBasinSize(self, point, basinDict):
        
        if (str(point) in basinDict):
            return 0
        else:
            basinDict[str(point)] = True

        for direction in self.directions:
            hasLowerHeight = self.hasLowerHeight(point, direction)
            if hasLowerHeight == None:
                continue
            elif hasLowerHeight == False:
                directionCoords = self.getDirectionCoords(point, direction)
                
                if (self.getHeightValue(directionCoords) < 9):
                    self.getBasinSize(directionCoords, basinDict)

        return 0