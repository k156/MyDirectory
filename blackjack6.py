import random
shape = ['s','h','d','c']
num = ['2','3','4','5','6','7','8','9','10', 'j', 'q', 'k']
aces = ['ace']
deck = []
deck.extend(aces*4)
for i in shape:
    for j in num:
        deck.append(str(i+j))
# random.shuffle(deck)
# cards.append(deck.pop())
# cards.append(deck.pop())
class Game():
    def __init__(self):
        self.number = 0
        self.cards = []
        random.shuffle(deck)
        self.cards.append(deck.pop())
        self.cards.append(deck.pop())
        return deck 
        return self.cards
        return self.number
    def distribute(self, deck, cards):
        random.shuffle(deck)
        self.cards.append(deck.pop())
        print(self.cards)
        return deck
        return self.card
    def play(self, deck, cards):
        self.cards = cards
        for card in self.cards:
            if card == 'ace':
                num = input("Ace가 나왔습니다. 1과 11중에 선택하세요.")
                while num != '11' and num != '1':
                    num = input("아니 1과 11 중에 선택하라니까?")
                self.number += int(num)       
            if 'j' in card or 'q' in card or 'k' in card:
                self.number += 10
            if len(self.card) > 1:
                num = self.card[1:]
                self.number += int(num)
            else:
                self.num = int(card[1])
            hors = input("Hit이면 h, Stand면 s를 누르세요.")
            while hors == 'h':
                distribute(deck, cards)
                play(deck, cards)
                continue
                if hors == 's' or self.number > 21:
                    print("게임이 끝났습니다.")
                    print(self.cards)
                    break
                    if dealer.number < self.number:
                        print("축하합니다. 당신의 승리입니다!")
                        print("딜러=",Dealer.number +', 플레이어=', self.number)
                    elif dealer.number > self.number:
                        print("딜러의 승리입니다.")
                        print("딜러=",Dealer.number +', 플레이어=', self.number)
                    else:
                        print('무승부입니다.')
                        print("딜러=",Dealer.number +', 플레이어=', self.number)
                else:
                    'h 또는 s를 누르세요.'
class Dealer(Game):
    def __init__(self):
        self.number = 0
        self.cards = []
    def play(self):
        distribute(self)
game = Game()
dealer = Dealer()
if game.number < 21 and dealer.number < 17:
    game.distribute()
    game.play()
    dealer.play()
if game.number < 21 and dealer.number > 17:
    game.play()
elif game.number > 21:
    print(game.cards)
    print("21을 초과하였습니다. 딜러의 승리입니다.")
elif game.number == 21:
    print("축하합니다! 당신의 승리입니다.")