from utils.aoc_utils import AOCDay, day

@day(6)
class Day6(AOCDay):
    def common(self):
        # Array for possible fish internal values
        # Position in index means the # of fish at that value
        self.lampFishSimulation = []
        self.lampFishSimulationP2 = []
        
        for i in range(9):
            self.lampFishSimulation.append(0)
            self.lampFishSimulationP2.append(0)

        lanternFish = self.inputData[0].split(',')

        # Set initial distribution of fish values
        for i in range(len(lanternFish)):
            self.lampFishSimulation[int(lanternFish[i])] += 1
            self.lampFishSimulationP2[int(lanternFish[i])] += 1

        return 0

    def part1(self):
        return sum(self.simulateFish(self.lampFishSimulation, 80))
    
    def part2(self):
        return sum(self.simulateFish(self.lampFishSimulationP2, 256))

    def simulateFish(self, fishArray, daysLeft):
        if (daysLeft == 0):
            return fishArray
        else:
            generatedFish = fishArray[0] # Store all fishes giving birth

            # Decrement all values
            for i in range(len(fishArray)-1):
                fishArray[i] = fishArray[i+1]

            # Fishes born
            fishArray[8] = generatedFish

            # Parents reset at 6 days
            fishArray[6] += generatedFish

            return self.simulateFish(fishArray, daysLeft - 1)

