import gd
from gd.api import *

class Player:
    def __init__(self, username: str, icon: int, player_color:PlayerColor):
        self.username = username
        self.icon = icon
        self.player_color = player_color