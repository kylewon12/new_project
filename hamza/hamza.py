import random
import deck


RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]

class Game:
    
    def __init__(self, players):
        
        self.players = players
        "some other stuff idc yet"
        
    
    def shuffle_deck(self):
        """
        Have to shuffle deck and hand equal amount to each player
        
        """
        
        random.shuffle("some kind of deck") # figure this out
        player_card_size = len("the deck^") / len(self.players)# figure deck out
        
        for player in self.players:
            player.hand = # need to deal cards to each player
            
        #idt anything else needed for this method
    
    def player_turn(self):
        """
        Look at each persons turn. idk how to figure out if each turn is legal
        
        """
        
        for player in self.players:
            print(f"{"need to figure out player name"}'s turn. Current hand: 
                  {player.hand}")
            
            played_card = player. #idk
            print(f"{"player name"} played {played_card}")
            
    
    def reset_scores(self):
        """
        resetting all scores and then starting new game/round
        
        """
        
        for player in self.score:
            self.score[player] = 0
    
    def calculate_scores(self):
        """
        calculating score of each player at end of round/game based on cards 
        in their hand
        
        """
        for player in players:
            player.score = sum(1 for card in "players collected cards" \
                           if "Hearts" in card)
        
        self.score["player name"] += player.score
        print(f"{"player name"} scored {player.score} points this round" \
             " Total score: {self.score[player name]} ")
    
    
    def play_game(self):
        """
        Play full round of a game
        
        """
        self.shuffle_deck()
        self.player_turn()
        self.calculate_scores()
        print(f"End of round scores", self.scores)
        
        

        
class Player:
    
    
    
    
    
    

#set up players

#initialize and play game

# my actual part

def reset_scores(self, reset_total=False):
    """
    Reset all players points at start of new round/game
    
    Args:
        reset_total (bool): if True, reset total score and round points 
                            if False, reset only round points
    """
    
    for player in self.players:
        player.round_points = 0
        
        if reset_total:
            self.scores[player.name] = 0
        
        print(f"{player.name}'s scores have been reset. Round points = " \
             "{player.round_points}.\n", end="")
        
        
    print("\nAll player scores have been reset.\n" + \
    ("Total scores also reset." if reset_total else "Only round scores reset."))

        
        
    #code to shuffle and deal cards to players
    
    
    def shuffle_deck(self):
        
        random.shuffle(self.deck)
        
    def deal_cards(self, num_cards_each):
        
        