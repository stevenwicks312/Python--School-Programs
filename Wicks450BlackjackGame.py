import random
import time

playingCards = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King',)
value = {'Two': 2, 'Three':3, 'Four': 4, 'Five': 5, 'Six': 6,
         'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,'Jack': 10,
         'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

class Card:
    def __init__(self, rank):
        self.rank = rank
    def __str__(self):
        return self.rank

class Deck:
    def __init__(self):
        self.deck = []
        for rank in playingCards:
            self.deck.append(Card(rank))

    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.aces = 0 #Aces get their own value since they can be 1 or 11
        self.value = 0

## Changes ace to 1 or 11
    def adjustAce(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def addCard(self, card):
        self.cards.append(card)
        self.value += value[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

class Chips:
    def __init__(self):
        self.total = 1000
        self.bet = 0
    def win(self):
        self.total += self.bet
    def loss(self):
        self.total -= self.bet

def playerBet(chips):
    while True:
            chips.bet = int(input('Enter Bet:  '))
            if chips.bet > chips.total:
                print('Your bet can not be over {} chips'.format(chips.total))
            else:
                break

def hit(deck, hand):
    hand.addCard(deck.deal())
    hand.adjustAce()

def hitStand(deck, hand):

    global playing
    while True:
        x = input("Type 'h' to hit, or 's' to stand: ")
        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above
        elif x[0].lower() == 's':
            print("Player stands. Dealer's turn.")
            playing = False
        else:
            print("Try again.")
            continue
        break
#display cards
def showStart(player, dealer):
    time.sleep(0.5)
    print("\n___Dealer's Hand___ ")
    print(" **Hidden Card**")
    print(" ", dealer.cards[1])
    print("____Player's Hand____", *player.cards, sep='\n')
    print("*Value of Player's Hand: ", player.value)
def showEnd(player, dealer):
    print("\n___Dealer's Hand____", *dealer.cards, sep="\n")
    print("Value of Dealer's Hand: ", dealer.value)
    print("\n____Player's Hand____", *player.cards, sep='\n')
    print("*Value of Player's Hand: ", player.value)

#end game scenarios
def playerBusted(player, dealer, chips):
    print("***Player has lost***")
    chips.loss()
def dealerBusted(player, dealer, chips):
    print("***Dealer has lost***")
    chips.win()
def playerWin(player, dealer, chips):
    print("***Player has won***")
    chips.win()
def dealerWin(player, dealer, chips):
    print("***Dealer has won****")
    chips.loss()
def tie(player, dealer):
    print("***Player and Dealer tie***")

#start game
while True:
    deck = Deck()
    deck.shuffle()

    playerHand = Hand()
    playerHand.addCard(deck.deal())
    playerHand.addCard(deck.deal())

    dealerHand = Hand()
    dealerHand.addCard(deck.deal())
    dealerHand.addCard(deck.deal())

    playerChips = Chips()
    playerBet(playerChips)
    showStart(playerHand, dealerHand) #hides dealers hand

    while playing:
        hitStand(deck, playerHand)
        showStart(playerHand, dealerHand)
        if playerHand.value > 21:
            playerBusted(playerHand, dealerHand, playerChips)
            break
    if playerHand.value <= 21:
        #dealer stands at 17
        while dealerHand.value < 17:
            hit(deck, dealerHand)
        showEnd(playerHand, dealerHand)

        if dealerHand.value > 21:
            dealerBusted(playerHand, dealerHand, playerChips)
        elif dealerHand.value > playerHand.value:
            dealerWin(playerHand, dealerHand, playerChips)
        elif dealerHand.value < playerHand.value:
            playerWin(playerHand, dealerHand, playerChips)
        else:
            tie(playerHand, dealerHand)

    print("\nPlayers total winnings: ", playerChips.total)
    new_game = input("Type 'y' to play again, or 'n' to end game: ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Game Ended")
        break