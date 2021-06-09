import random

shape = ['s','h','d','c']
num = ['2','3','4','5','6','7','8','9','10', 'j', 'q', 'k']
aces = ['ace']
deck = []
cards = []
number = 0
# cards = []

deck.extend(aces*4)
for i in shape:
    for j in num:
        deck.append(str(i+j))


random.shuffle(deck)
cards.append(deck.pop())
cards.append(deck.pop())

def game():
    global number
    
    while number < 21:
        random.shuffle(deck)       
        print(cards)
        for card in cards:
            if 'j' in card or 'q' in card or 'k' in card:
                number += 10
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
                number += int(num)       
            else: 
                if len(card) > 1:
                    num = card[1:]
                    number += int(num)
                else:
                    num = int(card[1])
    if number == 21:
        print("축하합니다. 당신의 승리입니다!")
    
    else:
        print("21을 초과하였습니다. 딜러의 승리입니다.")


game()  
# print(cards)
print(number)