import main
import random
INFINITE = 9999
class AIPlayer:
    def __init__(self, game, player) -> None:
        self.game = game
        self.player = player
        self.opponent = 'X'

    def findRandMove(self):
        row = random.randint(0, self.game.sizeBoard - 1)
        col = random.randint(0, self.game.sizeBoard - 1)
        while (self.game.board[row][col] != '-'):
            row = random.randint(0, self.game.sizeBoard - 1)
            col = random.randint(0, self.game.sizeBoard - 1)
        return (row, col)

    def bestPoint(self, player):
        n = len(self.game.board)
        maxPoint = 0
        for i in range(n):
            for j in range(n):
                if self.game.board[i][j] == '-':
                    self.game.board[i][j] = player

                    point = self.game.pointOfcurrentState(self.player)
                    if (point >= INFINITE):
                        self.game.board[i][j] = '-'
                        return INFINITE
                    if (point > maxPoint):
                        maxPoint = point
                    self.game.board[i][j] = '-'

        return maxPoint

    def findBestMove(self):
        result = self.findRandMove()
        maxPoint = 0
        n = len(self.game.board)
        if (self.game.movesTaken == 0):
            return (n // 2, n // 2)
        for i in range(n):
            for j in range(n):
                if self.game.board[i][j] != '-':
                    continue
                # if self.game.board[i][j] == '-':
                self.game.board[i][j] = self.player
                point = 0
                point = self.bestPoint(self.player)

                if (point >= INFINITE):
                    self.game.board[i][j] = '-'
                    return (i, j)

                if (point < maxPoint):
                    continue
                point -= self.bestPoint(self.opponent)
                if (point >= maxPoint):

                    maxPoint = point
                    result = (i, j)
                self.game.board[i][j] = '-'

        return result

