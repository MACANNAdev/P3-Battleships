from random import randint


class Board:
    """
    Creates a claass from which both boards are created
    """

    def __init__(self, size,  num_ships, name, user):
        self.num_ships = num_ships
        self.name = name
        self.user = user
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.guesses = []
        self.ships = []
        self.hits = []

    def print(self):
        """
        Creates a two dimesional array from list's and prints it each round
        """
        for row in self.board:
            print(" ".join(row))
        print(self.name)
        return ""

    def guess(self, x, y):
        """
        Processes whether their have been hits,updates the board and hits list
        x= row and y = column
        """
        self.guesses.append((x, y))

        if (x, y) in self.guesses:
            self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            self.hits.append("H")
            return "Hit"
        else:
            return "Miss"

    def already_guessed(self, x, y):
        if (x, y) in self.guesses:
            return True
        else:
            return False


def random_point(size):
    """
    helper function to return random interger between 0 and size
    """
    return randint(0, size - 1)


def populate_board(board):
    """
     place ship in random row + random column
    """
    random_row = random_point(board.size)
    random_col = random_point(board.size)
    if board.user == "player":
        board.ships.append((random_row, random_col))
        board.board[random_row][random_col] = "@"
    else:
        board.ships.append((random_row, random_col))


def make_guess(board):
    """
    Validates user input
    """

    if board.user == "computer":

        while True:
            while True:
                try:
                    x = int(input("Enter row \n"))
                except ValueError:
                    print("enter a number between 0-4")
                    continue
                if x >= 5 or x <= -1:
                    print("Out of bounds must be within 0-4")
                    continue
                else:
                    break

            while True:
                try:
                    y = int(input("Enter column \n"))
                except ValueError:
                    print("Enter a number between 0-4")
                    continue
                if y >= 5 or y <= -1:
                    print("Out of bounds must be within 0-4")
                    continue
                else:
                    break

            if not board.already_guessed(x, y):
                board.guess(x, y)
                print(f'players guesses row {x} column {y}')
                break
            else:
                print(f'You have already entered co-oridinates: {x}, {y}')
                print('Try again, numbers from 0-4')
                continue
    elif board.user == "player":
        x = random_point(board.size)
        y = random_point(board.size)
        board.guess(x, y)
        print(f'computer guesses row {x} column {y}')


def play_game(computer_board, player_board):
    """
    Plays game and print boards until game_over is True
    """
    print("Game initializing")
    print(player_board.print())
    print(computer_board.print())

    while not game_over(computer_board, player_board):

        make_guess(computer_board)
        make_guess(player_board)

        print(player_board.print())
        print(computer_board.print())
        if game_over(computer_board, player_board):
            if len(player_board.hits) == 8:
                print("COMPUTER WINS! \n")
            else:
                print(f'{player_board.name} WINS!')
            break

    print("-" * 35)
    print("RESTARTING GAME PLEASE PLAY AGAIN!!!!")
    new_game()


def game_over(computer_board, player_board):
    """
    Checks hits list to determine winner
    """

    if len(computer_board.hits) == 8 or len(player_board.hits) == 8:
        return True
    else:
        return False


def new_game():
    """
    Starts new game
    """

    size = 5
    num_ships = 4
    print("-" * 35)
    print("WELCOME TO BATTLESHIPS!\n")
    print("-" * 35)
    print('INSTRUCTIONS\n')
    print("-" * 35)
    print("GUESS WHERE THE ENEMIES SHIPS ARE ")
    print('THIS BOARD IS A GRID WITH DIMENSIONS OF 5x5 WITH 5 SHIPS TO ATTACK')
    print("CHOOSE A ROW AND COLUMN FROM THE NUMBERS BETWEEN 0-4")
    print("SINK YOUR ENEMIES SHIPS BEFORE THEY SINK YOURS!")
    print("-" * 35)
    player_name = input("Please enter your name \n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "Computer", user="computer")
    player_board = Board(size, num_ships, player_name, user="player")

    for _ in range(num_ships):

        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)


new_game()
