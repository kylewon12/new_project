"""
 *** IMPORTANT RULES ***
- player with lowest points wins
- A player that gets to 100 points first will stop the game and evaluate the winner.
- Each heart card is 1pt.
- The queen of spade (KILLER QUEEN) is worth 13 pt.
"""


# TEMP variables for players hand... this isnt official its just a placeholder
h1 = [['club', 4], ['heart', 'Q'], ['club', 10], ['heart', 3], ['heart', 'K'], ['club', 7], ['club', 3], ['club', 'K'], ['diamond', 'A'], ['diamond', 9], ['diamond', 8], ['heart', 6], ['diamond', 5]]

h2 = [['spade', 'Q'], ['spade', 10], ['spade', 'A'], ['diamond', 7], ['spade', 3], ['diamond', 2], ['diamond', 4], ['heart', 'A'], ['diamond', 6], ['heart', 9], ['heart', 7], ['spade', 'J'], ['diamond', 'K']]

h3 = [['club', 'A'], ['heart', 4], ['spade', 6], ['club', 2], ['club', 9], ['heart', 5], ['diamond', 10], ['heart', 'J'], ['club', 'J'], ['spade', 'K'], ['spade', 9], ['spade', 7], ['heart', 10]]

h4 = [['spade', 4], ['heart', 2], ['diamond', 3], ['spade', 5], ['diamond', 'J'], ['club', 5], ['club', 6], ['diamond', 'Q'], ['spade', 8], ['club', 8], ['heart', 8], ['spade', 2], ['club', 'Q']]

#SHOOTING THE MOOO HAND. Special occasions where someone could have all the hearts and the Q of spades.
sm = [['heart', 2], ['heart', 3], ['heart', 4], ['heart', 5], ['heart', 6], ['heart', 7], ['heart', 8], ['heart', 9], ['heart', 10], ['heart', 'J'], ['heart', 'Q'], ['heart', 'K'], ['heart', 'A'], ['spade', 'Q']]

players = {
    'Bk': h1,
    'Melat': h2,
    'Kyle': h3,
    'Hamza': h4,
    
    #'Jerry': sm 
    #This player (Jerry) is an example of someones hand meeting the condition of shootmoon
    
}


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


print(score(players))