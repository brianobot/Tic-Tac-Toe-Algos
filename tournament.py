"""
After Implementing an algorithm for the computer player
"""

import environ
import players
import importlib

from app import TicTacToe
from collections import Counter

env = environ.Env()
environ.Env.read_env()

ITERATIONS = env("ITERATIONS", default=500)
PLAYER_MODULE = importlib.import_module("players")

# list of default dummy players for reference, if you algorithm loses to this players
players_list = [
    players.ComputerPlayer,
    players.LastSpotPickerPlayer,
    players.FirstSpotPickerPlayer,
    players.MiddleSpotPickerPlayer,
]

with open("players_list.txt") as player_data:
    for player in player_data.readlines():
        player: str
        if player.isspace():
            continue
        try:
            player = getattr(PLAYER_MODULE, player)
        except AttributeError as err:
            print(f"Error while adding player: {player}")
            continue
        else:
            players_list.append(player)
            print(f"Successfully Added player: {player}")


input("sdfsdfsdf")

league_wins = []


def compare_players(a, b, iterations=ITERATIONS):
    results = []
    for run in range(iterations):
        game = TicTacToe(a, b)
        while game.check_for_winner() == -1:
            # print_board(game)
            if game.computer_player and (game.player == game.computer_player.id):
                r, c = game.computer_player.make_move()
                # print(f"Computer player {game.computer_player.id} plays {r, c}")
                game.make_move(r, c)
            elif game.computer_player_2 and (game.player == game.computer_player_2.id):
                r, c = game.computer_player.make_move()
                # print(f"Computer player {game.computer_player_2.id} plays {r, c}")
                game.make_move(r, c)
            else:
                pass

        # print_board(game)
        x = game.check_for_winner()
        results.append(x)

    most_wins = Counter(results).most_common()
    win_ratio = most_wins[0][1] / iterations
    winner_id = most_wins[0][0]
    loser_id = 1 if winner_id == 2 else 2
    winner_name = game.get_computer_player(winner_id).name
    loser_name = game.get_computer_player(loser_id).name
    league_wins.append([winner_name, win_ratio, loser_name])


def main():
    for player_a in players_list:
        for player_b in players_list:
            print(f"Game: {player_a.__name__} vs {player_b.__name__}")
            compare_players(player_a, player_b)

    for win in league_wins:
        print("WINS: ", win)


if __name__ == "__main__":
    main()
