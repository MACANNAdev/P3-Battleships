from random import randint

scores = {"computer" : 0, "player": 0}


class Board:

    def __init__(self, num_ships, name, user, size):
        self.num_ships = num_ships
        self.name = name
        self.user = user
        self.size = size
        self.board = [[ "." for x in range(size)] for y in range(size)]
        self.guesses= []
        self.ships = []