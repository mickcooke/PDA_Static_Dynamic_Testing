import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

  def setUp(self):
    self.cardGame = CardGame()
 
  def test_can_check_for_ace(self):
    self.card = Card("Spades", 1)
    self.assertEqual(True, self.cardGame.check_for_ace(self.card))

  def test_highest_card(self):
    self.card1 = Card("Hearts", 10)
    self.card2 = Card("Diamonds", 7)
    self.assertEqual(self.card1, self.cardGame.highest_card(self.card1, self.card2))


  def test_cards_total(self):
    self.card1 = Card("Hearts", 10)
    self.card2 = Card("Diamonds", 7)
    self.cards = [self.card1, self.card2]
    self.assertEqual("You have a total of 17", self.cardGame.cards_total(self.cards))


