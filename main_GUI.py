from GUI import *
from window import *


new_game(250, 300)
if player1.get() == player2.get():
    two_player_game()
else:
    one_player_game()