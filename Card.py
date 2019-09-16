class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
		
	def equals(self, card):
		return self.suit == card.suit and self.value == card.value
		
	def show(self):
		print("{} of {}".format(self.names[self.value],self.suit))
		
	def name(self):
		return ("{} of {}").format(self.names[self.value],self.suit)
		
	names = {
	    2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace"
	}