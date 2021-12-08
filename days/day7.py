from utils.aoc_utils import AOCDay, day
import math

@day(7)
class Day7(AOCDay):
    def common(self):
        self.crabPositions = [int(x) for x in self.inputData[0].split(',')]
        self.crabPositions.sort()
        return 0

    def part1(self):
        # Find median
        medianValue = self.crabPositions[math.floor(len(self.crabPositions)/2)]

        fuelRequired = 0
        for crabPos in self.crabPositions:
            # Get total 'distance' from median crab
            fuelRequired += abs(crabPos - medianValue)

        return fuelRequired
    
    def part2(self):
        # Tip to self : Target might not be in current positions

        lowestFuel = float('inf')
        for target in range(min(self.crabPositions), max(self.crabPositions) + 1):
            fuel = 0
            for crabPos in self.crabPositions:
                distance = abs(crabPos - target)
                fuel += math.floor(distance*(distance+1)/2)
            
            if fuel < lowestFuel:
                lowestFuel = fuel

        return lowestFuel