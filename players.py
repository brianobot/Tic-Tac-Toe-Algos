import random


class ComputerPlayer:
    def __init__(self, id, game):
        self.id = id
        self.game = game

    def make_decision(self):
        open_spots = self.game.get_open_spots()
        return random.choice(open_spots)

    def make_move(self):
        r, c = self.make_decision()
        return r, c

    @property
    def name(self):
        return f"{self.__class__.__name__}:{self.id}"


class FirstSpotPickerPlayer(ComputerPlayer):
    def make_decision(self):
        open_spots = self.game.get_open_spots()
        return open_spots[0]
    

class LastSpotPickerPlayer(ComputerPlayer):
    def make_decision(self):
        open_spots = self.game.get_open_spots()
        return open_spots[-1]
    
class MiddleSpotPickerPlayer(ComputerPlayer):
    def make_decision(self):
        open_spots = self.game.get_open_spots()
        return open_spots[len(open_spots)// 2]

