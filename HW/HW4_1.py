# Hello World
# You need to implement, is_red(), matches(), and beats() for this class
# Don't forget to keep all of the necessary indentation for each function!

class Card:

  SUITS = ["Spades", "Diamonds", "Hearts", "Clubs"]
  VALUES = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def __repr__(self):
    return "<{} of {}>".format(self.value, self.suit)

  def get_int_value(self):
    if self.value == "A":
      return 11
    if self.value == "K" or self.value == "Q" or self.value == "J":
      return 10
    return int(self.value)

  @classmethod
  def get_full_deck(cls):
    deck = []
    for suit in cls.SUITS:
      for value in cls.VALUES:
        deck.append(Card(suit,value))
    return deck

  def __eq__(self,other):
    return self.suit == other.suit and self.value == other.value

  # Card.is_red() should return True if the Card is red (Diamonds or Hearts)
  def is_red(self):
    return False

  # This function should return True if this card (self) matches suit or value of
  # the card passed in as a parameter (other_card). Think "playable in Uno" 
  # For example:
  # Card("Diamonds","A").matches(Card("Diamonds","6")) -> True # These are both Diamonds
  # Card("Spades","K").matches(Card("Spades","4")) -> True # These are both Spades
  # Card("Spades","7").matches(Card("Clubs","7")) -> True # These are both 7
  # Card("Hearts","K").matches(Card("Spades","4")) -> False # These match neither in suit or in value
  def matches(self, other_card):
    return False

  # This function should return True if this card (self) "beats" the other card.
  # For the purposes of this function "beats" means the following:
  # - This card's value is higher than the other card's value
  # OR
  # - This card's value is equal to the other card's value AND this card's suit is Spades, but the other card's is not Spades
  # Examples:
  # Card("Diamonds","A").beats(Card("Diamonds","6")) -> True # Value of "A" (11) is higher than value of "6" (6)
  # Card("Hearts","A").beats(Card("Diamonds","K")) -> True # Value of "A" (11) is higher than value of "K" (10)
  # Card("Spades","J").beats(Card("Diamonds","K")) -> True # Value of "J" (10) is equal to that of "K" (10) and self is Spades
  # Card("Spades","J").beats(Card("Spades","K")) -> False # Value of "J" (10) is equal to that of "K" (10) and self is Spades BUT the suit of the other card is Spades
  # Card("Hearts","J").beats(Card("Clubs","K")) -> False # Value of "J" (10) is equal to that of "K" (10) and self is not Spades
  # Card("Hearts","3").beats(Card("Clubs","5")) -> False # Value of "3" (3) is less than that of "5" (5)
  def beats(self, other_card):
    return False


