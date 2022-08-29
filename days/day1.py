from utils.aoc_utils import AOCDay, day


@day(1)
class Day1(AOCDay):
    def common(self):
        self.frequency = 0
        return 0

    def part1(self):
        for val in self.inputData:
            self.changeFrequency(val)
        return self.frequency

    def part2(self):
        self.frequency = 0
        frequencySet = set()
        loopNum = 0
        while(True):
            index = loopNum % len(self.inputData)
            self.changeFrequency(self.inputData[index])
            loopNum += 1

            if self.frequency in frequencySet:
                return self.frequency
            else:
                frequencySet.add(self.frequency)
            pass

    def changeFrequency(self, input):
        if input[0] == '+':
            self.frequency += int(input[1:])
        else:
            self.frequency -= int(input[1:])
