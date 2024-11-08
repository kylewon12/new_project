import deck

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
