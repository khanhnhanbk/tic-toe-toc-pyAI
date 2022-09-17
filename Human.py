import main


class Human:
    def __init__(self, game, player) -> None:
        self.game = game
        self.player = player

    def takeTurn(self):
        row, col = list(
            map(int, input("Enter row and column numbers to fix spot: ").split()))
        while not (self.game.checkCoorValid(row, col)):
            print("Invalid move!")
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
        return (row, col)