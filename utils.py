import environ
import importlib

env = environ.Env()
environ.Env.read_env()

PLAYER_MODULE = env("PLAYER_MODULE", default="players")
PLAYER_MODULE = importlib.import_module(PLAYER_MODULE)


def load_players() -> list:
    """
    Read and Load Players classes from the players_list.txt file
    invalid players are indicated, and are not added to the returned list
    """
    players = []
    with open("players_list.txt") as players_data:
        for player in players_data.readlines():
            player: str
            if player.isspace():
                continue
            try:
                player_class = getattr(PLAYER_MODULE, player)
            except AttributeError as err:
                print(f"Error while adding player: {player}")
                continue
            else:
                players.append(player_class)
                print(f"Successfully Added player: {player}")
    return players