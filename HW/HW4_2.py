
from HW4_1 import *

# A deck is a list of cards


### NEEDS IMPLEMENTATION!
# The deck is a list of cards. You should remove the _first_ card
# from the deck and return that card. Return None if the deck is empty
# Hint: look at the list.pop() function:
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
def draw_card(deck):
  return Card("Spades", "A")


### NEEDS IMPLEMENTATION!
# This function should draw n cards from the deck and return them
# in a list. If there aren't at least n cards left, then draw as many cards 
# as possible and return those (if there are 0 cards in the deck, an empty list is returned)
def deal_cards(deck, n):
  return []


### NEEDS IMPLEMENTATION!
# This function returns the suit of the hand if the hand is a flush (all cards are of the same suit)
# If this hand isn't a flush it returns None
# The deck parameter is a list of cards
def flush(hand):
  return None


### NEEDS IMPLEMENTATION!
# This function detects if there is a straight in the deck. A straight must be at least 5 consecutive
# values. For this function, simply treat "A" as greater than "K", but never less than "2"
# If a straight is detected, this function returns the maximum value in that straight.
# If no straight is detected, this function returns None
def straight(deck):
  return None


# This function returns a dictionary which maps suits to the number of times that suit appears
# in the input deck
def count_suits(deck):
  suit_counts = {}
  for suit in Card.SUITS:
    suit_counts[suit] = 0

  for card in deck:
    suit_counts[card.suit] += 1
  return suit_counts

### NEEDS IMPLEMENTATION!
# This function returns a dictionary which maps values to the number of times that value appears
# in the input deck
def count_values(deck):
  return {}