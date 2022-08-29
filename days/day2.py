from operator import countOf
from utils.aoc_utils import AOCDay, day


@day(2)
class Day2(AOCDay):
    def common(self):
        return 0

    def part1(self):
        twoCount = 0
        threeCount = 0
        for line in self.inputData:
            charList = set(line)
            charDict = dict.fromkeys(charList, 0)

            for charPos in range(len(line)):
                char = line[charPos]
                charDict[char] += 1

            if 2 in charDict.values():
                twoCount += 1

            if 3 in charDict.values():
                threeCount += 1

        return twoCount * threeCount

    def part2(self):
        for line1 in self.inputData:
            for line2 in self.inputData:
                sameChars = ''.join(x for x, y in zip(line1, line2) if x == y)

                if len(sameChars) == len(line1) - 1:
                    return sameChars
        return 0
