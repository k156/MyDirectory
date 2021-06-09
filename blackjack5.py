import random

shape = ['s','h','d','c']
num = ['2','3','4','5','6','7','8','9','10', 'j', 'q', 'k']
aces = ['ace']
global deck
deck = []
deck.extend(aces*4)
for i in shape:
    for j in num:
        deck.append(str(i+j))



def jqk(self, card):
    if 'j' in card or 'q' in card or 'k' in card:
        self.number += 10
        hors = input("Hit이면 h, Stand면 s를 누르세요.")
        self.hitorstand(hors, self.number)
    else:
        pass


def ace(self, card):
    if card == 'ace':            
        num = input("Ace가 나왔습니다. 1과 11중에 선택하세요.")
        while num != '11' and num != '1':
            num = input("아니 1과 11 중에 선택하라니까?")
        self.number += int(num)
        hors = input("Hit이면 h, Stand면 s를 누르세요.")
        self.hitorstand(hors, self.number)
    else:
        pass     


class Game():
    def __init__(self):
        global deck
        self.cards = []
        random.shuffle(deck)
        self.cards.append(deck.pop())
        self.cards.append(deck.pop())
        self.number = 0

    def hitorstand(self, hors, number):
        while self.number < 21:
            if hors == 'h' or hors == 'H':
                self.giveoutcard(deck)
            elif hors == 's'or hors == 'S':
                self.compare(number)
                break
            else:
                self.compare(number)
                break

    def giveoutcard(self, deck):
        random.shuffle(deck)
        self.cards.append(deck.pop())
        print(self.cards)
        self.play(self.cards)
    
    def play(self, cards):
        print(self.cards)
        for card in self.cards:
            jqk(self, card= card)
            ace(self, card = card)
            if len(card) > 1:
                num = card[1:]
                self.number += int(num)
                hors = input("Hit이면 h, Stand면 s를 누르세요.")
                self.hitorstand(hors, self.number)

    
    def compare(self, number):
        if game.number == 21:
            print("우승입니다! 축하합니다.")
        if dealer.number < game.number:
            print("패배입니다.")
        if dealer.number > game.number:
            print("승리입니다! 축하합니다.")



class Dealer(Game):
    def play(self):
        game.play(cards)
        if self.number < 17:
            print('(dealer:', self.number, ')')
            if giveoutcard == True:
                self.cards.append(deck.pop())


game = Game()
dealer = Dealer()
dealer.play()