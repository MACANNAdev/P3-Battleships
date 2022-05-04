from random import randint

scores = {"computer" : 0, "player": 0}


class Board:

    def __init__(self, size,  num_ships, name, user):
        self.num_ships = num_ships
        self.name = name
        self.user = user
        self.size = size
        self.board = [[ "." for x in range(size)] for y in range(size)]
        self.guesses = []
        self.ships = []    

    def print(self):
        """
        creates a two dimesional array from list's
        """
        for row in self.board:
            print(" ".join(row))
        
    def guess(self, x, y):
        """

        x= row and y = column
        """
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


def random_point(size):
    """
    helper function to return random interger between 0 and size
    """
    return randint(0, size -1)

def valid_cooardinates(x , y, board):
    """
    make sure guess is within board and has not been addeed to guess list []
    """
def populate_board(board):
    """
     place ship in random row + random column
    """
    random_row = random_point(board.size)
    random_col= random_point(board.size)
    
    if board.user ==  "player":
        board.ships.append((random_row, random_col))
        board.board[random_row][random_col]= "@"
    else:
        board.ships.append((random_row, random_col))

def make_guess(board):
    """
    computer reandom rpw + random column
    player prompt for input
    """
    if board.user == "player":
        x = int(input("Enter row"))
        y = int(input("Enter column"))
        board.guess(x, y)
        
    elif board.user== "computer":
        x = random_point(board.size)
        y = random_point(board.size)
        board.guess(x, y)
  

def play_game(computer_board, player_board):
    """
    """
    print("Game initializing")
    print(player_board.print())
    print(computer_board.print())
    make_guess(player_board)
    make_guess(computer_board)
    
    

def new_game():

    size = 10
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" *35)
    print("Welcome to Battleships!")
    print("-" *35)
    player_name = input("Please enter your name \n")
    print("-" *35)

    computer_board = Board(size, num_ships, "Computer", user= "computer")
    player_board = Board(size, num_ships, player_name, user= "player")
    
    for _ in range(num_ships):
     
        populate_board(player_board)
        populate_board(computer_board)
    

    play_game(computer_board, player_board)

new_game()