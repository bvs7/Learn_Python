import unittest
import sys

try:
  import HW4_1
except:
  print("Failed to import HW4_1! Check that it runs successfully!")
  sys.exit()

class TestHW4_1(unittest.TestCase):


  def test_Card_init(self):
    
    for suit in HW4_1.Card.SUITS:
      for value in HW4_1.Card.VALUES:
        c = HW4_1.Card(suit,value)
        self.assertEqual(suit, c.suit)
        self.assertEqual(value, c.value)

  def test_Card_get_int_value(self):

    def get_value(card):
      if card.value == "A":
        return 11
      if card.value in ["K","Q","J"]:
        return 10
      return int(card.value)

    for suit in HW4_1.Card.SUITS:
      for value in HW4_1.Card.VALUES:
        c = HW4_1.Card(suit,value)
        self.assertEqual(c.get_int_value(),get_value(c))

  def test_Card_is_red(self):

    self.assertFalse(HW4_1.Card("Clubs","4").is_red())
    self.assertFalse(HW4_1.Card("Clubs","A").is_red())
    self.assertFalse(HW4_1.Card("Spades","10").is_red())
    self.assertFalse(HW4_1.Card("Spades","2").is_red())
    self.assertTrue(HW4_1.Card("Diamonds","4").is_red())
    self.assertTrue(HW4_1.Card("Diamonds","J").is_red())
    self.assertTrue(HW4_1.Card("Hearts","4").is_red())
    self.assertTrue(HW4_1.Card("Hearts","Q").is_red())

  def test_Card_get_full_deck(self):
    deck = HW4_1.Card.get_full_deck()
    for suit in HW4_1.Card.SUITS:
      for value in HW4_1.Card.VALUES:
        c = HW4_1.Card(suit,value)
        self.assertIn(c, deck)

  def test_Card_matches(self):

    cards = [
      HW4_1.Card("Diamonds","4"),
      HW4_1.Card("Hearts","A"),
      HW4_1.Card("Spades","4"),
      HW4_1.Card("Clubs","10"),
      HW4_1.Card("Hearts","Q")
    ]

    match1 = HW4_1.Card("Hearts","4")
    matches = [True, True, True, False, True]

    for i in range(5):
      self.assertEqual(matches[i], match1.matches(cards[i]))

    match2 = HW4_1.Card("Clubs","A")
    matches = [False, True, False, True, False]

    for i in range(5):
      self.assertEqual(matches[i], match2.matches(cards[i]))

  def test_Card_beats(self):

    cards = [
      HW4_1.Card("Diamonds","4"),
      HW4_1.Card("Hearts","A"),
      HW4_1.Card("Spades","4"),
      HW4_1.Card("Clubs","10"),
      HW4_1.Card("Hearts","Q")
    ]

    match1 = HW4_1.Card("Hearts","6")
    matches = [True, False, True, False, False]

    for i in range(5):
      self.assertEqual(matches[i], match1.beats(cards[i]))

    match2 = HW4_1.Card("Spades","A")
    matches = [True, True, True, True, True]

    for i in range(5):
      self.assertEqual(matches[i], match2.beats(cards[i]))

    self.assertFalse(match2.beats(match2))

try:
  import HW4_2
except:
  print("Failed to import HW4_2! Check that it runs successfully!")
  sys.exit()


class Test_HW4_2(unittest.TestCase):

  def test_draw_cards(self):
    deck = HW4_1.Card.get_full_deck()
    
    while len(deck) > 0:
      top_card = deck[0]
      self.assertEqual(top_card, HW4_2.draw_card(deck))
      self.assertNotIn(top_card, deck)
    
    # Deck has been emptied
    self.assertIsNone(HW4_2.draw_card(deck))

  def test_deal_cards(self):

    for i in range(1, 14):
      deck = HW4_1.Card.get_full_deck()
      while len(deck) > 0:
        n_expected = min(i,len(deck))
        top_cards_expected = deck[:n_expected]
        top_cards_actual = HW4_2.deal_cards(deck, i)
        self.assertEqual(len(top_cards_actual), n_expected)
        self.assertListEqual(top_cards_expected, top_cards_actual)
        for card in top_cards_actual:
          self.assertNotIn(card, deck)
    
      l = len(deck)
      self.assertEqual(l, 0)

      self.assertListEqual([], HW4_2.deal_cards(deck))

  def test_flush(self):

    hand1 = [HW4_1.Card("Diamonds", str(i)) for i in range(2,7)]
    hand2 = [HW4_1.Card("Hearts", str(i)) for i in ["9","10","J","Q","K"]]
    hand3 = [HW4_1.Card("Spades", str(i)) for i in ["A","Q","J","K","10"]]
    hand4 = [HW4_1.Card("Clubs", str(i)) for i in ["9","6","5","7","8"]]

    hand5 = hand1[1:5] + hand4[4:5]
    hand6 = hand1[0:3] + hand3[2:3]
    hand7 = hand1[0:3]+ [hand3[0], hand4[2]]
    hand8 = hand1[0:4]

    self.assertEqual("Diamonds", HW4_2.flush(hand1))
    self.assertEqual("Hearts", HW4_2.flush(hand2))
    self.assertEqual("Spades", HW4_2.flush(hand3))
    self.assertEqual("Clubs", HW4_2.flush(hand4))
    self.assertEqual("Diamonds", HW4_2.flush(hand8))

    self.assertIsNone(HW4_2.flush(hand5))
    self.assertIsNone(HW4_2.flush(hand6))
    self.assertIsNone(HW4_2.flush(hand7))

  def test_straight(self):
    hand1 = [HW4_1.Card("Diamonds", str(i)) for i in range(2,7)]
    hand2 = [HW4_1.Card("Hearts", str(i)) for i in ["9","10","J","Q","K"]]
    hand3 = [HW4_1.Card("Spades", str(i)) for i in ["A","Q","J","K","10"]]
    hand4 = [HW4_1.Card("Clubs", str(i)) for i in ["9","6","5","7","8"]]

    hand5 = hand1[1:5] + hand4[4:5]
    hand6 = hand1[0:3] + hand3[2:3]
    hand7 = hand1[0:3]+ [hand3[0], hand4[2]]
    hand8 = hand1[0:4]

    self.assertEqual("6", HW4_2.straight(hand1))
    self.assertEqual("K", HW4_2.straight(hand2))
    self.assertEqual("A", HW4_2.straight(hand3))
    self.assertEqual("9", HW4_2.straight(hand4))

    self.assertEqual("8", HW4_2.straight(hand5))
    self.assertEqual("5", HW4_2.straight(hand7))
    self.assertIsNone(HW4_2.straight(hand6))
    self.assertIsNone(HW4_2.straight(hand8))

  def test_count_suits(self):

    deck = HW4_1.Card.get_full_deck()

    vs = dict([(suit,13) for suit in HW4_1.Card.SUITS])

    count_suits = HW4_2.count_suits(deck)

    for k in vs:
      self.assertIn(k, count_suits)
      self.assertEqual(vs[k], count_suits[k])

  
  def test_count_values(self):

    deck = HW4_1.Card.get_full_deck()

    vs = dict([(v,4) for v in HW4_1.Card.VALUES])

    count_values = HW4_2.count_values(deck)

    for k in vs:
      self.assertIn(k, count_values)
      self.assertEqual(vs[k], count_values[k])
    
      
      

    

  