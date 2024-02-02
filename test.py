import utils

class TestUtils:
    def test_load_players(self):
        players = utils.load_players()
        assert isinstance(players, list | tuple)
