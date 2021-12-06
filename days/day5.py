from utils.aoc_utils import AOCDay, day

@day(5)
class Day5(AOCDay):
    def common(self):
        self.highestX = self.highestY = 0
        self.hydroVents = []
        # Generate hydrovent containing a tuple for start and end coords
        for i in range(len(self.inputData)):
            points = self.inputData[i].split(' -> ')
            hydroVent = []
            for j in range(2):
                point = points[j].split(',')
                x = int(point[0])
                y = int(point[1])
                if x > self.highestX: self.highestX = x
                if y > self.highestY: self.highestY = y

                hydroVent.append((x, y))
            
            self.hydroVents.append(hydroVent)

        return 0

    def part1(self):
        # Generate map
        oceanMap = []
        for y in range(self.highestY + 1):
            line = []
            for x in range(self.highestX + 1):
                line.append(0)
            oceanMap.append(line)

        # Draw vents
        for vent in range(len(self.hydroVents)):
            self.simpleDrawOnOceanMap(oceanMap, self.hydroVents[vent])

        # Get overlaps        
        overlaps = 0
        for y in range(len(oceanMap)):
            for x in range(len(oceanMap[0])):
                if (oceanMap[y][x] > 1): overlaps += 1

        return overlaps
    
    def part2(self):
        return 0

    def printOceanMap(self, oceanMap):
        for i in range(len(oceanMap)):
            print(oceanMap[i])

    def simpleDrawOnOceanMap(self, oceanMap, vent):
        x1 = vent[0][0]
        y1 = vent[0][1]
        x2 = vent[1][0]
        y2 = vent[1][1]

        if (x1 == x2):
            for y in range(min(y1, y2), max(y1, y2)+1):
                oceanMap[y][x1] += 1

        elif (y1 == y2): # y1 = y2

            for x in range(min(x1, x2), max(x1, x2)+1):
                oceanMap[y1][x] += 1





