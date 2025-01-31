import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


class Card:

  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return self.rank + " of " + self.suit


class Deck:

  def __init__(self):
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit,rank))

  def __str__(self):
    deck_comp = ''
    for card in self.deck:
      deck_comp += '\n' + card.__str__()
    return 'The deck has: '+ deck_comp

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    single_card = self.deck.pop()
    return single_card


class Hand:

  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0

  def add_card(self, card):
    self.cards.append(card)
    self.value += values[card.rank]
    if card.rank == 'Ace':
      self.aces += 1

  def adjust_for_ace(self):
    while self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1


class Chips:

  def __init__(self):
    self.total = 100
    self.bet = 0

  def win_bet(self):
    self.total += self.bet

  def lose_bet(self):
    self.total -= self.bet

def take_bets(chips):
  while True:
    try:
      chips.bet = int(input('How many chips do u want to bet? '))
    except ValueError:
      print("enter a valid response")
    else:
      if chips.bet > chips.total:
        print (f'Sorry, ur bet can\'t exceed {chips.total}')
      else:
        break


def hit(deck, hand):
  hand.add_card(deck.deal())
  hand.adjust_for_ace()


def hit_or_stand(deck, hand):
  global playing
  while True:
    x = input ("hit or stand? h/s: ")
    if x.lower() == 'h':
      hit(deck,hand)
    elif x.lower() == 's':
      print("player stands. dealer is playing")
      playing = False
    break


def show_some(player,dealer):
  print("In dealer's hand: ")
  print("<hidden card>")
  print(dealer.cards[1])
  print("\nIn player's hand: ", *player.cards, sep ='\n')

def show_all(player, dealer):
  print("\nIn dealer's hand: ", *dealer.cards, sep ='\n')
  print("dealer's hand = ", dealer.value)
  print("\nIn player's hand: ", *player.cards, sep ='\n')
  print("player's hand= ", player.value)


def player_busts(player,dealer, chip):
  print("player busts!")
  chip.lose_bet()
def player_wins(player,dealer, chip):
  print("player wins!")
  chip.win_bet()
def dealer_busts(player,dealer, chip):
  print("dealer busts!")
  chip.win_bet()
def dealer_wins(player,dealer, chip):
  print("dealer wins!")
  chip.lose_bet()
def push(player,dealer):
  print("it's a tie! it's a push.")


while True:
  print("Welcome to the Game of Blackjack")
  deck = Deck()
  deck.shuffle()

  player_hand = Hand()
  player_hand.add_card(deck.deal())
  player_hand.add_card(deck.deal())

  dealer_hand = Hand()
  dealer_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())

  player_chips = Chips()
  take_bets(player_chips)
  show_some(player_hand, dealer_hand)

  while playing:
    hit_or_stand(deck, player_hand)
    show_some(player_hand, dealer_hand)
    if player_hand.value > 21:
      player_busts(player_hand, dealer_hand, player_chips)
      break

  if player_hand.value <= 21:
    while dealer_hand.value < 17:
      hit(deck, dealer_hand)
    show_all(player_hand, dealer_hand)
    if dealer_hand.value > 21:
      dealer_busts(player_hand, dealer_hand, player_chips)
    elif dealer_hand.value > player_hand.value:
      dealer_wins(player_hand, dealer_hand, player_chips)
    elif dealer_hand.value < player_hand.value:
      player_wins(player_hand, dealer_hand, player_chips)
    else:
      push(player_hand, dealer_hand)

  print("the player standings are: ", player_chips.total)

  new_game = input("do u want to play another hand? y/n: ")
  if new_game.lower() == 'y':
    playing = True
    continue
  else:
    break