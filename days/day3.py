from utils.aoc_utils import AOCDay, day

@day(3) # Binary Diagnostic
class Day3(AOCDay):
    def common(self):
        # Array with 2 length array corresponding to the times
        # 0 was the bit's value, 1 was the bit's value
        self.timesBitValue = []


        # Create a list for each bit
        for i in range(len(self.inputData[0])):
            self.timesBitValue.append([0, 0])

        for i in range(len(self.inputData)):
            line = self.inputData[i]
            for bit in range(len(line)):
                self.timesBitValue[bit][int(line[bit])] += 1

        self.gammaRateList = []
        self.epsilonRateList = []

        # Construct binary array (of strings)
        for i in range(len(self.timesBitValue)):
            bit = self.timesBitValue[i]
            dominantBit = bit[0] < bit[1]
            self.gammaRateList.append(str(int(dominantBit)))
            self.epsilonRateList.append(str(int(not dominantBit)))

        # Convert to binary string
        self.gammaRate = ''.join(self.gammaRateList)
        self.epsilonRate = ''.join(self.epsilonRateList)

        return 0

    def part1(self):
        return int(self.gammaRate, 2) * int(self.epsilonRate, 2)
    
    def part2(self):       
        return 0

        