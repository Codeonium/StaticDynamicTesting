import unittest 
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def test_check_for_ace(self):
        ace = Card("clubs", 1)
        self.assertEqual(True, CardGame().check_for_ace(ace))

    def test_highest_card(self):
        ace = Card("clubs", 1)
        two = Card("clubs", 2)
        self.assertEqual(two, CardGame().highest_card(ace, two))

    def test_cards_total(self):
        ace = Card("clubs", 1)
        two = Card("clubs", 2)
        deck = (ace, two)

        self.assertEqual("You have a total of 3", CardGame().cards_total(deck))