from utils.aoc_utils import AOCDay, day

@day(4)
class Day4(AOCDay):
    def common(self):
        self.picks = [int(x) for x in self.inputData[0].split(',')]
        self.boards = []

        self.markers = []
        # Loop on all boards, we assume boards are 5x5 martix
        for board in range(2, len(self.inputData), 6):
            # Generate this board's markers, 5x5 matrix of booleans
            newMarker = []
            for i in range(5):
                row = []
                for j in range(5): row.append(False)
                newMarker.append(row)
            
            self.markers.append(newMarker)

            # Parse this board's numbers
            newBoard = []
            for i in range(5):
                currentLine = self.inputData[board + i]
                row = []

                for j in range(0, 14, 3): # Board is 5 numbers that are 2 chars seperated by a space
                    row.append(int(currentLine[j:j+2]))
                
                newBoard.append(row)

            self.boards.append(newBoard)

        return 0

    def part1(self):

        gameWon = False
        winningBoardIndex = -1
        winningTurn = -1

        for turn in range(len(self.picks)):
            for boardIndex in range(len(self.boards)):
                updateStatus = self.updateBoard(boardIndex, self.picks[turn])

                if (turn > 4 and updateStatus[0]):
                    gameWon = self.checkWin(boardIndex, updateStatus[1])
                    
                    if (gameWon): 
                        winningBoardIndex = boardIndex
                        winningTurn = turn
                        break

            if (gameWon):
                break

        totalUnmarked = self.totalUnmarked(winningBoardIndex)

        return totalUnmarked * self.picks[winningTurn]
    
    def part2(self):
        gameOver = False
        numberOfBoards = len(self.boards)
        wonBoards = 0
        hasBoardWon = []
        lastWinningTurn = -1
        lastWinningBoardIndex = -1
        for i in range(numberOfBoards): hasBoardWon.append(False)

        for turn in range(len(self.picks)):
            for boardIndex in range(len(self.boards)):
                if (turn > 4 and hasBoardWon[boardIndex]): continue # Board is won, don't compute

                updateStatus = self.updateBoard(boardIndex, self.picks[turn])

                if (turn > 4 and updateStatus[0]):
                    boardWon = self.checkWin(boardIndex, updateStatus[1])
                    
                    if (boardWon):
                        wonBoards += 1
                        hasBoardWon[boardIndex] = True

                        if (wonBoards == numberOfBoards):
                            lastWinningTurn = turn
                            lastWinningBoardIndex = boardIndex
                            gameOver = True
                            break

            if (gameOver):
                break

        totalUnmarked = self.totalUnmarked(lastWinningBoardIndex)

        return totalUnmarked * self.picks[lastWinningTurn]

    # Calculate the total of all unmarked tiles on the board
    def totalUnmarked(self, boardIndex):
        totalUnmarked = 0
        for i in range(5):
            for j in range(5):
                if (not self.markers[boardIndex][i][j]): 
                    totalUnmarked += self.boards[boardIndex][i][j]

        return totalUnmarked

    # Updates the given board and returns tuple (updated, coords)
    def updateBoard(self, boardIndex, number):
        for i in range(5):
            for j in range(5):
                if self.boards[boardIndex][i][j] == number:
                    self.markers[boardIndex][i][j] = True
                    return (True, [i, j])
        
        return (False, [0, 0])
        

    def checkWin(self, markerIndex, latestMarkerPos):
        isWinner = False
        # Check row
        if (self.markers[markerIndex][latestMarkerPos[0]][0] and
            self.markers[markerIndex][latestMarkerPos[0]][1] and
            self.markers[markerIndex][latestMarkerPos[0]][2] and
            self.markers[markerIndex][latestMarkerPos[0]][3] and
            self.markers[markerIndex][latestMarkerPos[0]][4]):

            isWinner = True

        # Check column
        if(not isWinner and
            self.markers[markerIndex][0][latestMarkerPos[1]] and
            self.markers[markerIndex][1][latestMarkerPos[1]] and
            self.markers[markerIndex][2][latestMarkerPos[1]] and
            self.markers[markerIndex][3][latestMarkerPos[1]] and
            self.markers[markerIndex][4][latestMarkerPos[1]]):

            isWinner = True

        return isWinner
