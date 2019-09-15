class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
		
	def equals(self, card):
		return self.suit == card.suit and self.value == card.value
		
	def show(self):
		print("{} of {}".format(self.value,self.suit))