import random as r
import math


""""""""""""""" KYLE SECTION (test.py) """""""""""""""
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







""""""""""""""" BEREKET SECTION (score.py) """""""""""""""
def shootmoon(sb):
    """
    A players that has all 'heart' cards and the 'Q' of 'spade' in their hand.
    
    This function basically takes in the scoreboard for the game and check whether any player meets the condition.
        - Player hand MUST have a 'Q' of 'spade'
        - Player hand MUST have ALL 'heart' cards
    
                  
    Args:
        sb : (dict)
            This container contains each players name (str) as the key and hand (lists in list) as a value
            
    Returns:   
        scoreboard : (dict)
            A key value pair of the players name and the score that have with their hand.
                  
    Side Effect:
        N/A
     
    """
    for player, score in sb.items():
        if score != 26:
            score += 26
            sb[player] = score
        else:
            score = 0
            sb[player] = score
        
    return sb





def score(players):
    """
    Calculates a players hand.
    
    This function iterates through a dict container of players hand. Hand being a list of cards, It iterates through each card and evaluates it based on the condition to each point value.
        - If any card within a hand has the club of 'hearts' it would equal (1pt)
        - If a hand has a 'Q' of 'spade' it would equal (13pt).
    
                  
    Args:
        players : (dict)
            This container contains each players name (str) as the key and hand (lists in list) as a value
            
    Returns:   
        scoreboard : (dict)
            A key value pair of the players name and the score that have with their hand.
                  
    Side Effect:
        N/A
     
    """
    scoreboard = {}
    score = 0 
    
    for player,hand in players.items():
        
        cardcount = 0
    
        for card in hand:
            suit = card[0]
            value = card[1]
            
    
            if suit == 'heart':
                score += 1
                cardcount += 1               
            elif suit == 'spade' and value == 'Q':
                score += 13
                cardcount += 1
            else:
                continue
            
        #print(cardcount)
        scoreboard[player] = score
        score = 0
        
        if cardcount == 14:
            scoreboard = shootmoon(scoreboard)

    return scoreboard




""""""""""""""" MELAT SECTION (turn.py) """""""""""""""
class Turn():
    # This function is responsible for keeping track of turns during the card
    # game. This function is also responsible for making sure that turn taken
    # is legal (i.e., the player doesn’t break any rules of the game)


    def __init__(self, player_list: list):
        self.player_list = player_list
        self.played = []

    def current_player(self, player, round):
        current = ""
        self.round = 1

        # What it does: 
            # 1. takes in a list of the players
            # 2. identifies which round it's currently on
            # 3. identifies the player who have not played this round and 
            # declares them the current player, if no player has gone, 
            # it prompts the player with the beginning card "2 of spades" to
            #  play and goes through the list from there

        if self.round > 1:
            for player in self.player_list:
                if player not in self.played:
                    current += player
                    self.played.append(player) 
                    return player
                
        elif round == 1 and len(self.played) == 0: 
            for player in self.player_list:
                if deck[2, 'spades'] in player.deck: 
                    current += player 
                    self.played.append(player)
                    return player
                
        if self.played == len(self.player_list):
            round += 1

    # Card  -- What card is the player playing?

    def current_suit(self, suit, number):
        for card in current.deck: 




        
    # 1. takes in the what the cards are currently in the player's deck
    # 2. takes in user input for what card that player wants to play
    
    # Current Play -- What cards are currently in play? 
    
    # 1. takes in the cards in the 'pile', specifically the shapes 
    # 2. also checks if hearts are in play (hearts are only allowed to be player
    #  if, in a previous round, a player put down a heart as the first card 
    #  in the round)
    
    # Rules -- Validates that the card is legal
    
    # 1. validates that the card that the players put down matches with the 
    # shape that is currently in play or, if it's a heart, that hearts 
    # are allowed the be in play
    
    # 2. if the card that is played is not matching the shape, it can only be 
    # allowed if the player doesn't have the shape in their own deck 
    
    
    
    
    
""""""""""""""" HAMZA SECTION (hamza.py) """""""""""""""
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