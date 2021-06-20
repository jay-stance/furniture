#! python 3.7

# Write a python program for tic-tac-toe and display the board
"""
Functional requirements for the application:
- displayBoard() : to display the games current state on the console.
- getAvailaiblePos() : to return the availaible positions in the board
- setPos() : set the users position
"""

class Game:
    x, y = '', ''
    def __init__(self):
        self.board = [
            [1, 0, 0],
            [0, 1, 2],
            [2, 0, 0]
        ]
        
    def makeX(self, val):
        self.x = val
        
    def makeY(self, val):
        self.y = val
        
    def displayBoard(self):
        for row in self.board:
            for col in row:
                if col == 1:
                    print('| x |')
                elif col == 2:
                    print('| o |')
                else:
                    print('|  |')
            print('____')
        
        
        
game = Game()
game.makeX('Promise')
game.makeY('Sheggsmann')
game.displayBoard()
        
        