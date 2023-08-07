############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Used the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def deal_card(): 
    '''Return a random card from the deck of cards'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []
is_game_over = False

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    

while not is_game_over:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  print(f"Your cards : {user_cards}, Current Score: {user_score}.")
  print(f"Computer first cards : {computer_cards[0]},")

  if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
  else:
      user_should_deal = input("Type 'y' to get another cards, type 'n' to pass: ")
      if user_should_deal == 'y':
          user_cards.append(deal_card())
      else:
          is_game_over = True


while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

