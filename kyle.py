class Player():
    def __init__(self,hand,score):
        self.hand = hand
        self.score = score

def display(lst):
    for card in lst.items():
        print(card)
def find_winner(game_board,leading_suit):
    best_card = {"number":1,"suit":2,"player":3}
    
    (("number","suite"),"player")
    for player in game_board:
        for card in player:
            if (card["number"] > best_card["number"]) and (card["suit"] == leading_suit):
                best_card = card
    return best_card




def main():
    players = {"kyle":[{"number":1,"suit":"hearts","player":"kyle"},{"number":2,"suit":"spades","player":"kyle"}]}
    display(players)