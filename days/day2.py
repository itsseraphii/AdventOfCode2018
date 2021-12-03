from utils.aoc_utils import AOCDay, day

@day(2)
class Day2(AOCDay):
    def common(self):
        # Array of tuples (bool horizontal, value)
        self.submarineCommands = []
        for i in range(len(self.inputData)):
            # first char determines action
            if (self.inputData[i][0] == 'f'): #forward
                # Last char is single digit containing movement value
                self.submarineCommands.append((True, int(self.inputData[i][-1])))
            elif (self.inputData[i][0] == 'd'): # down
                self.submarineCommands.append((False, int(self.inputData[i][-1])))
            elif (self.inputData[i][0] == 'u'): # up
                self.submarineCommands.append((False, -1*int(self.inputData[i][-1])))

        return 0

    def part1(self):
        horizontalPos = 0
        depth = 0
        for i in range(len(self.submarineCommands)):
            if (self.submarineCommands[i][0]): # Move forward
                horizontalPos += self.submarineCommands[i][1]
            else: # Move depth
                depth += self.submarineCommands[i][1]
        
        return depth*horizontalPos
    
    def part2(self):
        horizontalPos = 0
        depth = 0
        aim = 0
        for i in range(len(self.submarineCommands)):
            if (self.submarineCommands[i][0]): # Move forward
                horizontalPos += self.submarineCommands[i][1]
                depth += aim * self.submarineCommands[i][1]
            else: # Move depth
                aim += self.submarineCommands[i][1]
        
        return depth*horizontalPos