"""
After Implementing an algorithm for the computer player
"""

import environ
import players

from app import TicTacToe
from utils import load_players
from collections import Counter

env = environ.Env()
environ.Env.read_env()

ITERATIONS = env("ITERATIONS", default=500)

# list of default dummy players for reference, if you algorithm loses to this players
players_list = [
    players.ComputerPlayer,
    players.LastSpotPickerPlayer,
    players.FirstSpotPickerPlayer,
    players.MiddleSpotPickerPlayer,
]


players_list += load_players()
input("sdfsdfsdf")

league_wins = []


def compare_players(a, b, iterations=ITERATIONS):
    """
    Run an Nth number of tic tac toe games between two players and record the win ratio.
    """
    results = []
    for run in range(iterations):
        game = TicTacToe(a, b)
        while game.check_for_winner() == -1:
            if game.computer_player and (game.player == game.computer_player.id):
                r, c = game.computer_player.make_move()
                game.make_move(r, c)
            elif game.computer_player_2 and (game.player == game.computer_player_2.id):
                r, c = game.computer_player.make_move()
                game.make_move(r, c)
            else:
                pass

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
