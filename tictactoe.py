import random

class TicTacToegame:

    def __init__(self):
        self.board_game = []

    def make_board(self):
        for i in range(3):
            rows = []
            for j in range(3):
                rows.append('-')
            self.board_game.append(rows)

    def random_player(self):
        return random.randint(0, 1)

    def print_spot(self, rows, cols, turn):
        self.board_game[rows][cols] = turn

    def check_player_win(self, player):
        win_game = None

        n = len(self.board_game)

        for i in range(n):
            win_game = True
            for j in range(n):
                if self.board_game[i][j] != player:
                    win_game = False
                    break
            if win_game:
                return win_game

        for i in range(n):
            win_game = True
            for j in range(n):
                if self.board_game[j][i] != player:
                    win_game = False
                    break
            if win_game:
                return win_game
        win_game = True
        for i in range(n):
            if self.board_game[i][i] != player:
                win_game = False
                break
        if win_game:
            return win_game

        win_game = True
        for i in range(n):
            if self.board_game[i][n - 1 - i] != player:
                win_game = False
                break
        if win_game:
            return win_game
        return False

        for rows in self.board_game:
            for item in rows:
                if item == '-':
                    return False
        return True

    def check_board_filled(self):
        for rows in self.board_game:
            for item in rows:
                if item == '-':
                    return False
        return True

    def next_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def display_board(self):
        for rows in self.board_game:
            for item in rows:
                print(item, end=" ")
            print()

    def start(self):
        self.make_board()

        player = 'X' if self.random_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.display_board()

            # taking user input
            rows, cols = list(
                map(int, input("Enter the row and column number to make your move : ").split()))
            print()

            # fixing the spot
            self.print_spot(rows - 1, cols - 1, player)

            # checking whether current player is won or not
            if self.check_player_win(player):
                print(f"YAYY Player {player} won the game!")
                break

            # checking whether the game is draw or not
            if self.check_board_filled():
                print("HAHA! Game Draw!")
                break

            # swapping the turn
            player = self.next_player_turn(player)

        # showing the final view of board
        print()
        self.display_board()


# starting the game
tic_tac_toe_game = TicTacToegame()
tic_tac_toe_game.start()
