import random

from players import ComputerPlayer


class TicTacToe:
    def __init__(self, computer_player=False, computer_player_2=False):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.player = 1
        self.computer_player = (
            computer_player(random.randint(1, 1), game=self)
            if computer_player
            else None
        )
        available_id = 1 if self.computer_player.id == 2 else 2
        self.computer_player_2 = (
            computer_player(available_id, game=self) if computer_player_2 else None
        )

    def get_open_spots(self):
        return [[r, c] for r in range(3) for c in range(3) if self.board[r][c] == 0]

    def is_valid_move(self, r, c):
        if 0 <= r <= 2 and 0 <= c <= 2 and self.board[r][c] == 0:
            return True
        return False

    def make_move(self, r, c):
        if self.is_valid_move(r, c):
            self.board[r][c] = self.player
            self.player = (self.player + 2) % 2 + 1

    def check_for_winner(self):
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] != 0:
                return self.board[0][c]
        for r in range(3):
            if self.board[r][0] == self.board[r][1] == self.board[r][2] != 0:
                return self.board[r][0]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        if self.get_open_spots() == []:
            return 0
        return -1
    
    def get_computer_player(self, id):
        if self.computer_player.id == id:
            return self.computer_player
        elif self.computer_player_2.id == id:
            return self.computer_player_2
        else:
            return None


def print_board(game):
    chars = ["-", "X", "O"]
    for r in range(3):
        for c in range(3):
            print(chars[game.board[r][c]], end=" ")
        print()


def main():
    game = TicTacToe(computer_player=ComputerPlayer, computer_player_2=ComputerPlayer)

    while game.check_for_winner() == -1:
        print_board(game)
        if game.computer_player and (game.player == game.computer_player.id):
            r, c = game.computer_player.make_move()
            print(f"Computer player {game.computer_player.id} plays {r, c}")
            game.make_move(r, c)
        elif game.computer_player_2 and (game.player == game.computer_player_2.id):
            r, c = game.computer_player.make_move()
            print(f"Computer player {game.computer_player_2.id} plays {r, c}")
            game.make_move(r, c)
        else:
            r, c = eval(input("Enter spot, player " + str(game.player) + ": "))
            game.make_move(r, c)

    print_board(game)
    x = game.check_for_winner()
    if x == 0:
        print("It's a draw.")
    else:
        print("Player", x, "wins!")


if __name__ == "__main__":
    main()
