from Card import Card
from Deck import Deck
from Player import Player
import random

class Game:
	
	def __init__(self):
		self.deck = Deck()
		self.players = self.playerSetUp()
		self.cardsPlayed = []
		self.heartsBroken = False
		
	def deal(self):
		while self.deck.cards:
			for player in self.players:
				player.draw(self.deck)
		for player in self.players:
			player.sortHand()
		
	def find2clubs(self):
		for i in range(len(self.players)):
			for c in self.players[i].hand:
				if c.equals(Card("Clubs", 2)):
					return i
					
	def playerSetUp(self):
		players = []
		for i in range(4):
			if i == 0:
				name = input("Please enter YOUR name: ")
				players.append(Player(name))
			else:
				name = input("Please enter a player name: ")
				players.append(Player(name))
		return players
		
	def round(self):
		self.trick(self.startingPlayerIndex)
		
	def trick(self, leadPlayerIndex):
		trick = []
		for i in range(4):
			if i == 0:
				leadCard = Card("Plops", 99)
			else:
				leadCard = trick[0]
			currentPlayerIndex = (leadPlayerIndex + i) % 4
			if currentPlayerIndex == 0:
				print("Your legal cards are: ")
				for c in self.players[0].legalCards(leadCard,self.heartsBroken):
					c.show()
				# self.players[0].legalCards(leadCard,self.heartsBroken).show()
				number = int(input("Input number of card you want: "))
				try:
					card = self.players[0].legalCards(leadCard,self.heartsBroken)[number]
				except:
					print("NOT GOOD")
			else:
				rand = random.randint(0,len(self.players[currentPlayerIndex].legalCards(leadCard,self.heartsBroken))-1)
				card = self.players[currentPlayerIndex].legalCards(leadCard,self.heartsBroken)[rand]
			self.players[currentPlayerIndex].hand.remove(card)
			trick.append(card)
			self.cardsPlayed.append(card)
			if card.suit == "Hearts":
				self.heartsBroken = True
			# print(self.players[currentPlayerIndex].name + " played the " + str(card.value) + " of " + card.suit)
			print(self.players[currentPlayerIndex].name + " played the " + card.name())
		winningValue = 0
		for c in trick:
			if c.suit == leadCard.suit and c.value > winningValue:
				winningCard = c
				winningValue = c.value
		winner = self.players[(self.startingPlayerIndex + trick.index(winningCard)) % 4]
		print(winner.name + " won the trick.")
		for c in trick:
			if c.suit == "Hearts":
				winner.points += 1
			if c.equals(Card("Spades", 12)):
				winner.points += 13
		self.startingPlayerIndex = self.players.index(winner)	
		
	def run(self):
		if self.deck.cards == []:
			self.deck = Deck()
		self.deck.shuffle()
		self.deal()
		self.startingPlayerIndex = self.find2clubs()
		print("Your starting hand is: ")
		self.players[0].showHand()
		while len(self.cardsPlayed) != 52:
			self.round()
		for p in self.players:
			p.showScore()
		self.cardsPlayed = []

if __name__ == "__main__":
	game = Game()
	keepPlaying = True
	while keepPlaying == True:
		game.run()
		highestScore = 0
		for p in game.players:
			if p.points > highestScore:
				losingPlayer = p
				highestScore = p.points
		if highestScore > 49:
			print(losingPlayer.name + " loses with " + str(losingPlayer.points) + " points!")
			keepPlaying = False
		else:
			print(losingPlayer.name + " is currently losing!")