from utils.aoc_utils import AOCDay, day

@day(3) # Binary Diagnostic
class Day3(AOCDay):
    def common(self):
        return 0

    def part1(self):
        # Array with 2 length array corresponding to the times
        # 0 was the bit's value, 1 was the bit's value
        timesBitValue = []

        for i in range(len(self.inputData[0])):
            timesBitValue.append(self.getTimesBitValue(self.inputData, i))

        gammaRateList = []
        epsilonRateList = []

        # Construct binary array (of strings)
        for i in range(len(timesBitValue)):
            bit = timesBitValue[i]
            dominantBit = bit[0] < bit[1]
            gammaRateList.append(str(int(dominantBit)))
            epsilonRateList.append(str(int(not dominantBit)))

        # Convert to binary string
        gammaRate = ''.join(gammaRateList)
        epsilonRate = ''.join(epsilonRateList)
        return int(gammaRate, 2) * int(epsilonRate, 2)
    
    def part2(self):
        oxygenGenerator = self.bitCriteria(self.inputData)
        co2Scrubber = self.bitCriteria(self.inputData, False)

        return int(oxygenGenerator, 2) * int(co2Scrubber, 2)

    # Returns amount of times bit was seen [0, 1]
    def getTimesBitValue(self, targetList, targetedBit):
        bitValues = [0, 0]

        for i in range(len(targetList)):
            bitValues[int(targetList[i][targetedBit])] += 1

        return bitValues

    def bitCriteria(self, list, mostCommon = True, targetedBit = 0, currentFilter = ''):
        if (len(list) == 1):
            return list[0]

        bitValues = self.getTimesBitValue(list, targetedBit)
        newFilter = currentFilter

        if (mostCommon):
            newFilter += str(int(bitValues[0] <= bitValues[1])) # If same amount, will be true (bias on 1)
        else:
            newFilter += str(int(bitValues[0] > bitValues[1])) # If same amount, will be false (bias on 0)

        filteredList = [x for x in list if newFilter in x[:len(newFilter)]]
        
        return self.bitCriteria(filteredList, mostCommon, targetedBit + 1, newFilter)