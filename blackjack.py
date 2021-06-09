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

def giveoutcards(deck):
    random.shuffle(deck)
    cards.append(deck.pop()) 
    cards.append(deck.pop())
    return cards

def insidecards(func):
        def new_function(*args):
            print("start")
            global cards
            for card in cards:
                print("started")
                result = func(*args)
                print('end')
            return result
    return new_function

@insidecards
def card2num(cards):
    global number
    print("card2num")
    print(cards)
    if card[1] == 'j' or 'q' or 'k':
        card = '10'
        number += int(card)
        print('jqk')
        print(number)
    elif 'ace' == card:
        print('ace popped up')
        ace()
        print('ace taken cared')
        number += int(card)
    else:
        print('started usual')
        card = int(card[1])
        number.append(card)
        print("just usual")
    return cards
    print(cards) 

giveoutcards(deck)
# print(cards)
card2num(cards)

def ace():        
    if 'ace' in cards:
        print(cards)
        card = input("ace가 나왔습니다.1과 11중에 선택하세요.")
        if card == '11' or '1':
            number += card
            print(number)
            return 
        else: '아니 1과 11 중에서 선택하라니까?'

        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

    # for card in cards:
    #     if 'j' in card:
    #         card == '10'
    #         print(cards)
    # if 'ace' in cards:
    #     a = input("1과 11중에 선택하세요.")
    #     if a == '11':
    #         card == '11'
    #         print(cards)

    # cards = [random.choice(deck),random.choice(deck)] 
    # for card in cards: 
    #     deck = deck.remove(card)
    # print(cards)
    print(deck )