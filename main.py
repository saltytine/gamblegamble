import random
import time
import os

class Card:
    def __init__(self, suit, rank, is_face_up=True):
        self.suit = suit
        self.rank = rank
        self.is_face_up = is_face_up

    def __str__(self):
      if self.is_face_up:
          rank_str = self.rank
          if self.rank == '10':
              rank_str = 'T'
          return f"""
    ___________
    |{rank_str}        |
    |         |
    |         |
    |    {self.suit}    |
    |         |
    |         |
    |        {rank_str}|
    ‾‾‾‾‾‾‾‾‾‾‾
    """
      else:
          return """
    ___________
    |/////////|
    |/////////|
    |/////////|
    |/////////|
    |/////////|
    |/////////|
    |/////////|
    ‾‾‾‾‾‾‾‾‾‾‾
    """


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['♦', '♥', '♣', '♠']:
            for rank in range(2, 11):
                self.cards.append(Card(suit, str(rank)))
            for rank in ['J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.rank.isdigit():
            self.value += int(card.rank)
        elif card.rank in ['J', 'Q', 'K']:
            self.value += 10
        else:
            if self.value + 11 > 21:
                self.value += 1
            else:
                self.value += 11

    def __str__(self):
        hand_str = ""
        for line in range(10):  # Assuming each card has 7 lines
            for card in self.cards:
                card_lines = str(card).split('\n')
                hand_str += card_lines[line] + '   '
            hand_str += '\n'
        return hand_str

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.is_playing = True

    def deal_initial(self):
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        dealer_first_card = self.deck.deal_card()
        dealer_first_card.is_face_up = False  # Face down card
        self.dealer_hand.add_card(dealer_first_card)

        # Display dealer's hand
        print("Dealer's hand:")
        print(self.dealer_hand)
        print(f"Total value: ??\n")

    def player_turn(self):
      while True:
          print("\nYour hand:")
          print(self.player_hand)
          print(f"Total value: {self.player_hand.value}")
          if self.player_hand.value > 21:
              print("Busted! You lose.")
              self.is_playing = False
              break
          action = input("Do you want to hit or stand? (h/s): ").lower()
          if action == 'h':
              self.player_hand.add_card(self.deck.deal_card())
              print("\nYour hand:")
              print(self.player_hand)
              print(f"Total value: {self.player_hand.value}")
          elif action == 's':
              break
          else:
            print("Enter h/s")

    def dealer_turn(self):
      print("\nDealer's turn:")
      while self.dealer_hand.value < 17:
          print("Dealer hits.")
          self.dealer_hand.add_card(self.deck.deal_card())
          print(self.dealer_hand)
          print(f"Total value: {self.dealer_hand.value}")
          time.sleep(2)
      if self.dealer_hand.value > 21:
          print("Dealer busted! You win.")
          self.is_playing = False
      elif self.dealer_hand.value >= self.player_hand.value:
          print("Dealer wins.")
          self.is_playing = False
      else:
          print("You win!")
          self.is_playing = False

    def play(self):
        print("▀█████████▄   ▄█          ▄████████  ▄████████    ▄█   ▄█▄      ▄█    ▄████████  ▄████████    ▄█   ▄█▄ ")
        print("  ███    ███ ███         ███    ███ ███    ███   ███ ▄███▀     ███   ███    ███ ███    ███   ███ ▄███▀ ")
        print("  ███    ███ ███         ███    ███ ███    █▀    ███▐██▀       ███   ███    ███ ███    █▀    ███▐██▀   ")
        print(" ▄███▄▄▄██▀  ███         ███    ███ ███         ▄█████▀        ███   ███    ███ ███         ▄█████▀    ")
        print("▀▀███▀▀▀██▄  ███       ▀███████████ ███        ▀▀█████▄        ███ ▀███████████ ███        ▀▀█████▄    ")
        print("  ███    ██▄ ███         ███    ███ ███    █▄    ███▐██▄       ███   ███    ███ ███    █▄    ███▐██▄   ")
        print("  ███    ███ ███▌    ▄   ███    ███ ███    ███   ███ ▀███▄     ███   ███    ███ ███    ███   ███ ▀███▄ ")
        print("▄█████████▀  █████▄▄██   ███    █▀  ████████▀    ███   ▀█▀ █▄ ▄███   ███    █▀  ████████▀    ███   ▀█▀ ")
        print("             ▀                                   ▀         ▀▀▀▀▀▀                            ▀         ")
        time.sleep(5)
        print("Welcome to Blackjack!")
        print("T, J, K and Q are 10")
        print("A is 11 or 1")
        print("Try to get as close to 21 as possible without going over.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1)
        self.deal_initial()
        while self.is_playing:
            self.player_turn()
            if self.is_playing:
                self.dealer_turn()

    def play_again(self):
      while True:
          answer = input("\nDo you want to play again? (y/n): ").lower()
          if answer == 'y':
              os.system('cls' if os.name == 'nt' else 'clear')
              self.deck = Deck()
              self.player_hand = Hand()
              self.dealer_hand = Hand()
              self.is_playing = True
              self.play()
          elif answer == 'n':
              print("Thanks for playing!")
              break
          else:
              print("Please enter 'y' or 'n'.")

game = BlackjackGame()
game.play()
game.play_again()0
