from random import randint

scores = {"computer" : 0, "player": 0}


class Board:

    def __init__(self, num_ships, name, user, size):
        self.num_ships = num_ships
        self.name = name
        self.user = user
        self.size = size
        self.board = [[ "." for x in range(size)] for y in range(size)]
        self.guesses = []
        self.ships = []


    

    def print(self):
        for row in self.board:
            print("".join(row))
        
        def guess(self, x, y):
            self.guesses.append((x, y))
            self.board[x][y]= "X"

            if (x, y) in self.ships:
                self.board[x][y] = "*"
                return "Hit"
            else:
                return "Miss"
        
        def add_ship(self, x, y, user= "computer"):
            if len(self.ships) >= self.num_ships:
                print("Error: you cannot add more ships!")
            else:
                self.ships.append((x, y))
                if self.user =="player":
                    self.board[x] [y]= "@"