import random

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def get_value(self) -> int:
        if self.rank == "King" or self.rank == "Queen" or self.rank == "Jack":
            return 10
        elif self.rank == "Ace":
            return 11
        else:
            return "  2345678910".index(self.rank)

    def get_rank(self) -> str:
        return f"{self.suit} {self.rank}"

class DeskCard:
    def __init__(self) -> None:
        _rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "King", "Queen", "Jack"]
        _suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.__cards = [Card(r, s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)

    def get_card(self) -> Card:
        return self.__cards.pop()

class Player:
    def __init__(self, name: str) -> None:
        self._hand = []
        self.count = 0
        self.name = name

    @property
    def hand(self) -> str:
        return f"Сards in hand: {self._hand}; Points - {self.count}"

    @hand.setter
    def hand(self, card: Card) -> None:
        self.count += card.get_value()
        self._hand.append(card.get_rank())


class Dealer(Player):
    # Easy mod
    # def get_cards(self, cards: DeskCard):
    #     while self.count < 18:
    #         self.hand = cards.get_card()

    # Normal mod
    def get_cards(self, cards: DeskCard):
        while self.count < 21:
            _card = cards.get_card()
            if _card.get_value() + self.count <= 21:
                self.hand = _card
            else:
                break



class Game:
    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name="Dealer")

    def print(self) -> str:
        return f"\n{self.player.name}:\n{self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand}"

    def check_count(self):
        if self.player.count > 21:
            print(f"You lose", self.print())
        elif self.dealer.count > 21 and self.player.count <= 21:
            print(f"You win!", self.print())
        elif self.dealer.count == self.player.count:
            print(f"Draw", self.print())
        elif self.dealer.count > self.player.count:
            print(f"You lose", self.print())
        elif self.dealer.count < self.player.count:
            print(f"You win!", self.print())


    def start(self) -> None:
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()

        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        print(self.player.hand)

        while self.player.count < 21:
            answer = input("Take a card? y/n ")
            if answer == "y":
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer == "n":
                self.dealer.get_cards(self.cards)
                break
        self.check_count()


def main() -> None:
    name = input("Enter your name: ")
    game = Game(name)
    game.start()

if __name__ == '__main__':
    main()
