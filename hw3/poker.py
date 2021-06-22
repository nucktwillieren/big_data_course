# all the categories checking method should be run after ascending sort.

def flush(cards):
    previous = cards[0]
    for card in cards:
        if previous.suit != card.suit:
            return False
    return True

def straight(cards):
    return (
        (cards[0].rank+4 == cards[4].rank or 
        (cards[0].rank == 1 and cards[4].rank == 13 and cards[0].rank + 3 == cards[3].rank)) # Case: A2345
    )

def straight_flush(cards):
    return straight(cards) and flush(cards)

def four_of_a_kind(cards):
    return cards[0].rank == cards[3].rank or cards[1].rank == cards[4].rank 

def full_house(cards):
    return (
        (cards[0].rank == cards[1].rank and cards[2].rank == cards[4].rank) 
        or
        (cards[0].rank == cards[2].rank and cards[3].rank == cards[4].rank) 
    )

def three_of_a_kind(cards):
    return (
        (cards[0].rank == cards[2].rank and cards[3].rank != cards[4].rank) or
        cards[1].rank == cards[3].rank or
        (cards[0].rank != cards[1].rank and cards[2].rank == cards[4].rank)
    )

def two_pair(cards):
    c = 0
    for i in range(1, 5):
        if cards[i].rank == cards[i-1].rank:
            c += 1
    return c == 2

def one_pair(cards):
    c = 0
    for i in range(1, 5):
        if cards[i].rank == cards[i-1].rank:
            c += 1
    return c == 1

def check(cards):
    # all the categories checking method should be run after ascending sort.
    hand = Hand(cards)
    print("Hand: ", hand)
    if straight_flush(hand.cards):
        print(f"Straight Flush({hand}): ", straight_flush(hand.cards))
    elif four_of_a_kind(hand.cards):
        print(f"Four of a Kind({hand}): ", four_of_a_kind(hand.cards))
    elif full_house(hand.cards):
        print(f"Full House({hand}): ", full_house(hand.cards))
    elif flush(hand.cards):
        print(f"Flush({hand}): ", flush(hand.cards))
    elif straight(hand.cards):
        print(f"Straight({hand}): ", straight(hand.cards))
    elif three_of_a_kind(hand.cards):
        print(f"Three of a Kind({hand}): ", three_of_a_kind(hand.cards))
    elif two_pair(hand.cards):
        print(f"Two Pair({hand}): ", two_pair(hand.cards))
    elif one_pair(hand.cards):
        print(f"One Pair({hand}): ", one_pair(hand.cards))
    else:
        print(f"High Card({hand}): ", True)

class Card:
    suit_mapping = {
        "club": 4,
        "heart": 3,
        "diamond": 2,
        "spade": 1,
    }
    rank_mapping = {
        "a":  13, # A is actually on the highest in rank.
        "1":  13, 
        "2":  1,
        "3":  2,
        "4":  3,
        "5":  4,
        "6":  5,
        "7":  6,
        "8":  7,
        "9":  8,
        "10": 9,
        "j":  10,
        "11": 10,
        "q":  11,
        "12": 12,
        "k":  12,
        "13": 12,
    }
    def __init__(self, card_str):
        try:
            t, n = tuple(card_str.split("_"))
            self.rank = self.rank_mapping[n.strip()]
            self.suit = self.suit_mapping[t.strip()]
            self.total = self.rank*10 + self.suit # To give a numbered ranking for comparison
        except:
            self = None

    def __str__(self):
        return f"{self.total}" # representation when directly printing

    def __repr__(self):
        return str(self.total) # representation in printing array

    def __eq__(self, value):
        return self.total == value.total # required when sorting

    def __lt__(self, value):
        return self.total < value.total # required when sorting

    def __le__(self, value):
        return self.total <= value.total # required when sorting

    def __ne__(self, value):
        return self.total != value.total # required when sorting

    def __gt__(self, value):
        return self.total > value.total # required when sorting
    
    def __ge__(self, value):
        return self.total >= value.total # required when sorting
    
class Hand:
    def __init__(self, cards_str = ""):
        cards = cards_str.lower().split(",")
        self.cards = []
        for card in cards:
            c = Card(card)
            self.cards.append(c)
        self.sort()

    def sort(self):
        self.cards = sorted(self.cards)
    
    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)

class TestCase:
    def __init__(self, *args, **kwargs):
        pass
    def straight_flush(self):
        print("Straight Flush Test Case: ")
        cards = "Heart_1, Heart_3, Heart_2, Heart_4, Heart_5"
        check(cards)
        print()
    def four_of_a_kind(self):
        print("Four of a Kind Test Case: ")
        cards = "Club_5, Heart_3, Diamond_5, Spade_5, Heart_5"
        check(cards)
        print()
    def full_house(self):
        print("Full House Test Case: ")
        cards = "Club_5, Heart_3, Diamond_3, Spade_5, Heart_5"
        check(cards)
        print()
    def flush(self):
        print("Flush Test Case: ")
        cards = "Heart_1, Heart_8, Heart_2, Heart_4, Heart_5"
        check(cards)
        print()
    def straight(self):
        print("Straight Test Case: ")
        cards = "Diamond_1, Heart_3, Heart_2, Heart_4, Heart_5"
        check(cards)
        print()
    def three_of_a_kind(self):
        print("Three of a Kind Test Case: ")
        cards = "Club_5, Heart_2, Diamond_3, Spade_5, Heart_5"
        check(cards)
        print()
    def two_pair(self):
        print("Two Pair Test Case: ")
        cards = "Club_5, Heart_3, Diamond_3, Spade_6, Heart_5"
        check(cards)
        print()
    def one_pair(self):
        print("One Pair Test Case: ")
        cards = "Club_5, Heart_1, Diamond_3, Spade_6, Heart_5"
        check(cards)
        print()
    def high_card(self):
        print("High Card Test Case: ")
        cards = "Club_1, Heart_3, Diamond_4, Spade_9, Heart_5"
        check(cards)
        print()
    def run_all(self):
        self.straight_flush()
        self.four_of_a_kind()
        self.full_house()
        self.flush()
        self.straight()
        self.three_of_a_kind()
        self.two_pair()
        self.one_pair()
        self.high_card()

def main():
    mode = input("Mode(Run All Test Case(t) / Enter Input Value by Yourself(i)): ")
    while mode != 't' and mode != 'i':
        mode = input("Mode(Run All Test Case(t) / Enter Input Value by Yourself(i)): ")

    if mode == "i":
        cards = input("Cards(ex: Club_5, Heart_3, Diamond_3, Spade_5, Heart_5): ")
        check(cards)
    elif mode == 't':
        TestCase().run_all()

if __name__ == '__main__':
    main()
    