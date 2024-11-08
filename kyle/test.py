class Player:
    def __init__(self,hand,score):
        self.hand = hand
        self.score = score

def display(lst):
    for player,cards in lst.items():
        print(player,"\'s deck:")
        for card in cards:
            print(f"{card["number"]} of {card["suit"]}")
def find_winner(game_board,leading_suit):
    top_num = [0,leading_suit]
    for player,cards in game_board.items():
        for card in cards:
            if card["number"] > top_num[0] and card["suit"] == leading_suit:
                top_num[0] = card["number"]
    
    return top_num

def find_first(game_board):
    first = ""
    for player,cards in game_board.items():
        for card in cards:
            if card["number"] == 2  and card["suit"] == "hearts":
                first = player
    return player
                




def main():
    players = {"kyle":[{"number":1,"suit":"hearts","player":"kyle"},{"number":2,"suit":"hearts","player":"kyle"},{"number":5,"suit":"spades","player":"kyle"}],
               "bill":[{"number":3,"suit":"hearts","player":"kyle"},{"number":2,"suit":"clubs","player":"kyle"},{"number":10,"suit":"diamonds","player":"kyle"}],
               "tim":[{"number":3,"suit":"spades","player":"kyle"},{"number":4,"suit":"clubs","player":"kyle"},{"number":9,"suit":"diamonds","player":"kyle"}]}
    display(players)
    print(find_first(players), "is the first player")
    top_card = find_winner(players,"diamonds")
    
    # print(top_card[0],"of",top_card[1] ,"was the top card")
    
main()