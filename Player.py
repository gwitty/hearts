from Card import Card
from Deck import Deck

class Player:

	def __init__(self, name):
		self.name = name
		self.hand = []
		self.points = 0
		
	def draw(self, deck):
		self.hand.append(deck.drawCard())
		# return self
		
	def hasCard(self, card):
		for c in self.hand:
			if c.equals(card):
				return True
		return False
		
	def showScore(self):
		print(self.name + " has " + str(self.points) + " points.")
	
	def showHand(self):
		for card in self.hand:
			card.show()
			
	def sortHand(self):
		self.hand = sorted(self.hand, key=lambda card: (card.suit, card.value))
		
	# def playCard(self, leadCard):
		# legalCards = []
		# if Card('Clubs', 2) in self.hand:
			# legalCards.append(Card('Clubs', 2))
		# else:
			# print("No 2 of clubs")
			
	def legalCards(self, leadCard, heartsBroken):
		legalCards = []
		if self.hasCard(Card("Clubs",2)):
			for c in self.hand:
				if c.equals(Card("Clubs", 2)):
					legalCards = [c]
		else:
			for card in self.hand:
				if card.suit == leadCard.suit:
					legalCards.append(card)
			if not legalCards:
				for card in self.hand:
					if card.suit == 'Hearts':
						if leadCard.suit == "Plops":
							if heartsBroken:
								legalCards.append(card)
						else:
							legalCards.append(card)
					else:
						legalCards.append(card)
			if not legalCards:
				for card in self.hand:
					legalCards.append(card)
		return legalCards
			