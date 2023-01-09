from gd.api import Editor as E
from gd.api import Object as Obj
from gd.api import *
from player import Player

class Editor:
    def __init__(self, players: list[Player]):
        self.editor = E()
        self.players = players
        self.placed = {}

    def place_block(self, player: Player, object: Obj):
        self.editor.add_objects(object)
        self.placed[object] = player

    def remove_block(self, player: Player, object: Obj):
        pass
