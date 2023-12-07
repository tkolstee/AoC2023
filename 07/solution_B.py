#!/usr/bin/env python

import sys
from enum import IntEnum


Rank = IntEnum('Rank', list('AKQT98765432J'))
HandRank = IntEnum('HandRank', ['five', 'four', 'FH', 'three', 'two_pair', 'pair', 'high'])

class Hand:
    def __init__(self, hand, bid):
        self.hand = [ Rank[x] for x in hand ]
        self.bid  = int(bid)
        self.freq = {}
        for c in self.hand:
            if c in self.freq:
                self.freq[c] += 1
            else:
                self.freq[c] = 1

    def __repr__(self):
        return f"Hand({self.__str__()}, {self.bid})"

    def __str__(self):
        return ''.join([ i.name for i in self.hand ])

    def handrank(self):
        myfreq = sorted(list(self.freq.values()), reverse=True)
        most = myfreq[0]

        if Rank.J in self.hand:
            most_freq_card = sorted(self.freq.keys(), key=lambda x: self.freq[x], reverse=True)[0]
            if most_freq_card == Rank.J:
                if len(myfreq) > 1:
                    most += myfreq[1]
            else:
                most += self.freq[Rank.J]
            
        if most == 5:
            return HandRank.five
        elif most == 4:
            return HandRank.four
        elif most == 3:
            if myfreq[1] == 2:
                return HandRank.FH
            else:
                return HandRank.three
        elif most == 2:
            if myfreq[1] == 2:
                return HandRank.two_pair
            else:
                return HandRank.pair
        else:
            return HandRank.high

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return False
        return self.hand == other.hand

    def __lt__(self, other):
        if self.__class__ is not other.__class__:
            return NotImplemented

        if self == other:
            return False

        myrank = self.handrank()
        othrank = other.handrank()
        if myrank != othrank:
            return myrank < othrank

        for i in range(len(self.hand)):
            if self.hand[i] < other.hand[i]:
                return True
            elif self.hand[i] > other.hand[i]:
                return False

        return False


def read_data(filename):
    hands = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            h = Hand(fields[0], int(fields[1]))
            hands.append(h)
        return hands


def main(filename):
    hands = read_data(filename)
    hands.sort(reverse=True)
    print(hands)
    total = sum([ hands[i].bid * (i+1) for i in range(len(hands)) ])
    print(f"TOTAL: {total}")


if __name__ == '__main__':
    main(sys.argv[1])
