from utils.aoc_utils import AOCDay, day

@day(1)
class Day1(AOCDay):
    def common(self):
        return 0

    def part1(self):
        # We just loop the inputs and compare it to the previous one to see if it was incremented
        return self.countTimesIncremented(self.inputData)
    
    def part2(self):
        # We loop on our input to create ping's "window"
        # then we just do the same thing as in part one
        windowList = []
        for ping in range(1, len(self.inputData) - 1): 
            # ping is the center of the window, so we won't need the first and last entry
            windowList.append(int(self.inputData[ping - 1]) + int(self.inputData[ping]) + int(self.inputData[ping + 1]))

        return self.countTimesIncremented(windowList)

    def countTimesIncremented(self, itemList):
        timesIncremented = 0
        for i in range(len(itemList)):
            if (int(itemList[i]) > int(itemList[i - 1])):
                timesIncremented += 1
        
        return timesIncremented
