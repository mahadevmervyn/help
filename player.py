from card import Card
from constants import Constants

class Node:
    def __init__(self, card: Card):
        self.card = card
        self.next = None

class Player:
    def __init__(self, name: str, position: int) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (int): The position of the player

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        self.name = name
        self.position = position
        self.hand = None  # first node of  linked list
        self._size = 0    # to keep track of the number of cards

    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1) - when inserting at the beginning
            Worst Case Complexity: O(n) - when inserting at the end, where n is the number of cards in hand
        """
        new_node = Node(card)
        
        if self.hand is None or (card.color.value < self.hand.card.color.value or 
                            (card.color == self.hand.card.color and 
                             card.label.value < self.hand.card.label.value)):
            new_node.next = self.hand
            self.hand = new_node
        else:
            current = self.hand
            while current.next and (current.next.card.color.value < card.color.value or
                                    (current.next.card.color == card.color and
                                    current.next.card.label.value <= card.label.value)):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        
        self._size += 1
        return None

    def play_card(self, index: int) -> Card:
        """
        Method to play a card from the player's hand

        Args:
            index (int): The index of the card to be played

        Returns:
            Card: The card at the given index from the player's hand

        Complexity:
            Best Case Complexity: O(1) - when removing from the beginning
            Worst Case Complexity: O(n) - when removing from the end, where n is the number of cards in hand
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        if index == 0:
            card = self.hand.card
            self.hand = self.hand.next
        else:
            current = self.hand
            for _ in range(index - 1):
                current = current.next
            card = current.next.card
            current.next = current.next.next
        
        self._size -= 1
        return card

    def __len__(self) -> int:
        
        """
        Method to get the number of cards in the player's hand

        Args:
            None

        Returns:
            int: The number of cards in the player's hand

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return self._size

    def __getitem__(self, index: int) -> Card:
        """
        Method to get the card at the given index from the player's hand

        Args:
            index (int): The index of the card to be fetched

        Returns:
            Card: The card at the given index from the player's hand

        Complexity:
            Best Case Complexity: O(1) - when accessing the first element
            Worst Case Complexity: O(n) - when accessing the last element, where n is the number of cards in hand
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        current = self.hand
        for _ in range(index):
            current = current.next
        return current.card