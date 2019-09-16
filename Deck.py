from Card import Card
import random

class Deck:

	def __init__(self):
		self.cards = []
		self.build()
		
	def build(self):
		for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
			for v in range(2,15):
				self.cards.append(Card(s,v))
				
	def drawCard(self):
		return self.cards.pop()
				
	def show(self):
		for c in self.cards:
		 c.show()
		 
	def shuffle(self):
		random.shuffle(self.cards)