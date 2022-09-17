# hello world
import random
import re
from unittest import result

INFINITE = 9999


class TicTacToe:

    def __init__(self):
        self.board = []
        self.sizeBoard = 3
        self.movesTaken = 0
        self.seriToWin = 3
        self.playerO = AIPlayer(self, 'O')

    def create_board(self):
        for i in range(self.sizeBoard):
            row = []
            for j in range(self.sizeBoard):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player
        self.movesTaken = self.movesTaken+1

    def is_player_win(self, player):
        countSeries = 0

        n = len(self.board)

        # checking rows
        for i in range(n):
            countSeries = 0
            for j in range(n):
                if self.board[i][j] == player:
                    countSeries += 1
                else:
                    countSeries = 0
                if countSeries == self.seriToWin:
                    return True

        # checking columns
        for i in range(n):
            countSeries = 0
            for j in range(n):
                if self.board[j][i] == player:
                    countSeries += 1
                else:
                    countSeries = 0
                if countSeries == self.seriToWin:
                    return True

        # checking diagonals
        numDiag = self.sizeBoard - self.seriToWin
        for diff in range(-numDiag, numDiag+1):
            countSeries = 0
            if (diff < 0):
                for i in range(n + diff):
                    if self.board[i][i - diff] == player:
                        countSeries += 1
                    else:
                        countSeries = 0
                    if countSeries == self.seriToWin:
                        return True
            else:  # k >= 0
                for i in range(diff, n):
                    if self.board[i][i - diff] == player:
                        countSeries += 1
                    else:
                        countSeries = 0
                    if countSeries == self.seriToWin:
                        return True

        # dialog
        for sumIndex in range(numDiag-1, n+numDiag - 1):
            if sumIndex < n:
                for i in range(sumIndex+1):
                    if self.board[i][sumIndex - i] == player:
                        countSeries += 1
                    else:
                        countSeries = 0
                    if countSeries == self.seriToWin:
                        return True
            else:  # sumIndex >= n
                for i in range(sumIndex-n, n):
                    if self.board[i][sumIndex - i-1] == player:
                        countSeries += 1
                    else:
                        countSeries = 0
                    if countSeries == self.seriToWin:
                        return True
        return False

    def is_board_filled(self):
        return self.movesTaken == self.sizeBoard*self.sizeBoard

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        print("  | ", end="")
        for i in range(self.sizeBoard):
            print(i, end=" ")
        print()
        i = 0
        for row in self.board:
            print(f"{i} | ", end="")
            i += 1
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            if (player == 'X'):
                # taking user input
                row, col = list(
                    map(int, input("Enter row and column numbers to fix spot: ").split()))
                while (row < 0 or row >= self.sizeBoard or col < 0 or col >= self.sizeBoard or self.board[row][col] != '-'):
                    print("Invalid turn, try again")
                    row, col = list(
                        map(int, input("Enter row and column numbers to fix spot: ").split()))
                print()
            else:
                row, col = self.playerO.findBestMove()
            # fixing the spot
            self.fix_spot(row, col, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            point = self.pointOfcurrentState(player)
            print(f"Point: {point}.")
            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()

    def pointCountSeries(self, countSeries):
        if countSeries == self.seriToWin:
            return INFINITE
        if countSeries == self.seriToWin - 1:
            return 2
        if countSeries == self.seriToWin - 2:
            return 1
        return 0

    def pointOfcurrentState(self, player):
        result = 0
        countSeries = 0

        n = len(self.board)

        # checking rows
        for i in range(n):
            countSeries = 0
            for j in range(n):
                if self.board[i][j] == player:
                    countSeries += 1
                    if countSeries == self.seriToWin:
                        return INFINITE
                    else:
                        result += self.pointCountSeries(countSeries)
                else:
                    countSeries = 0

        # checking columns
        for i in range(n):
            countSeries = 0
            for j in range(n):
                if self.board[j][i] == player:
                    countSeries += 1
                    if countSeries == self.seriToWin:
                        return INFINITE
                    else:
                        result += self.pointCountSeries(countSeries)
                else:
                    countSeries = 0

        # checking diagonals
        numDiag = self.sizeBoard - self.seriToWin
        for diff in range(-numDiag, numDiag+1):
            countSeries = 0
            if (diff < 0):
                for i in range(n + diff):
                    if self.board[i][i - diff] == player:
                        countSeries += 1
                        if countSeries == self.seriToWin:
                            return INFINITE
                        else:
                            result += self.pointCountSeries(countSeries)
                    else:
                        countSeries = 0
            else:  # k >= 0
                for i in range(diff, n):
                    if self.board[i][i - diff] == player:
                        countSeries += 1
                        if countSeries == self.seriToWin:
                            return INFINITE
                        else:
                            result += self.pointCountSeries(countSeries)
                    else:
                        countSeries = 0

        # dialog
        for sumIndex in range(numDiag-1, n+numDiag - 1):
            if sumIndex < n:
                for i in range(sumIndex+1):
                    if self.board[i][sumIndex - i] == player:
                        countSeries += 1
                        if countSeries == self.seriToWin:
                            return INFINITE
                        else:
                            result += self.pointCountSeries(countSeries)
                    else:
                        countSeries = 0
            else:  # sumIndex >= n
                for i in range(sumIndex-n, n):
                    if self.board[i][sumIndex - i - 1] == player:
                        countSeries += 1
                        if countSeries == self.seriToWin:
                            return INFINITE
                        else:
                            result += self.pointCountSeries(countSeries)
                    else:
                        countSeries = 0
        return result


class AIPlayer:
    def __init__(self, game, player) -> None:
        self.game = game
        self.player = player
        self.opponent = 'X'
        self.infinite = 999

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
                point = 0;
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


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
