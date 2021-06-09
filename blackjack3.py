import random

shape = ['s','h','d','c']
num = ['2','3','4','5','6','7','8','9','10', 'j', 'q', 'k']
aces = ['ace']
deck = []

deck.extend(aces*4)
for i in shape:
    for j in num:
        deck.append(str(i+j))


random.shuffle(deck)
cards.append(deck.pop())
cards.append(deck.pop())
class Game():
    def game(self):
        self.number = 0
        self.cards = []   
        while number < 21:
            random.shuffle(deck)       
            print(self.cards)
            for card in self.cards:
                if 'j' in card or 'q' in card or 'k' in card:
                    self.number += 10
                    hors = input("Hit이면 h, Stand면 s를 누르세요.")
                    if hors == 'h':
                        continue
                    else:
                        "게임을 종료합니다."
                        break
                elif card == 'ace':
                    num = input("Ace가 나왔습니다. 1과 11중에 선택하세요.")
                    while num != '11' and num != '1':
                        num = input("아니 1과 11 중에 선택하라니까?")
                    self.number += int(num)       
                else: 
                    print(cards)
                    hors = input("Hit이면 h, Stand면 s를 누르세요.")
                    if hors == 'h':
                        if len(card) > 1:
                            num = card[1:]
                            self.number += int(num)
                            continue
                        else:
                            hors = input("Hit이면 h, Stand면 s를 누르세요.")
                            if hors == 'h':
                                print(cards)
                                num = int(card[1])
                            continue
                    elif hours == 's':
                        break

        if self.number == 21:
            print("축하합니다. 당신의 승리입니다!")
        
        elif self.number > 21:
            print("21을 초과하였습니다. 딜러의 승리입니다.")


# print(cards)
print(number)


def compare():

class Dealer(Game):
    game()
    


