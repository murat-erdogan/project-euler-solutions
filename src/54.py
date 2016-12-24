#clubs (♣), diamonds (♦), hearts (♥) and spades (♠)

f = open('p054_poker.txt', 'r')

def high_card(hand):
    pass

def one_pair(hand):
    l = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    s = set(l)
    d = []
    for x in l:
        if x in s:
            s.remove(x)
        else:
            d.append(x)
    if len(d) > 0:
        return 1
    else:
        return 0

def two_pairs(hand):
    l = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    s = set(l)
    d = []
    for x in l:
        if x in s:
            s.remove(x)
        else:
            d.append(x)
    if len(d) > 1:
        return 2
    else:
        return 0

def three_of_kind(hand):
    l = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    s = set(l)
    d = []
    for x in l:
        if x in s:
            s.remove(x)
        else:
            d.append(x)
    if len(d) > 2:
        return 3
    else:
        return 0

def straight(hand):
    pass

def flush(hand):
    pass

def full_house(hand):
    pass

def four_of_kind(hand):
    pass

def straight_flush(hand):
    pass

def royal_flush(hand):
    pass

lines = f.read().splitlines()

for line in lines:
    p1 = 0
    p2 = 0
    h = line.split(" ")
    three_of_kind(h[5:10])