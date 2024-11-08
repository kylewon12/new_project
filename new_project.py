import random as r
import math


game_board = {"kyle":[{"number":1,"suit":"hearts","player":"kyle"},{"number":3,"suit":"hearts","player":"kyle"},{"number":5,"suit":"spades","player":"kyle"}],
               "bill":[{"number":3,"suit":"hearts","player":"bill"},{"number":2,"suit":"hearts","player":"bill"},{"number":10,"suit":"diamonds","player":"bill"}],
               "tim":[{"number":3,"suit":"spades","player":"tim"},{"number":4,"suit":"clubs","player":"tim"},{"number":9,"suit":"diamonds","player":"tim"}]}

# Kyle Won's method

def display(game_board):
    """
        Function that goes through each hand and displays them 
        Args: game_board: Basically a list of all players' hands
        Side effects: Prints each players deck
        Returns: none
    """
    for player,cards in game_board.items():
        print(player,"\'s deck:")
        for card in cards:
            print(f"{card["number"]} of {card["suit"]}")

display(game_board)
            
        