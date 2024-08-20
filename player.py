from card import Card
from constants import Constants
from data_structures.array_sorted_list import ArraySortedList

class Player:
    def __init__(self, name: str, position: int) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (int): The position of the player

        Returns:
            None
        """
        self.name = name
        self.position = position
        self.hand = ArraySortedList(Constants.DECK_SIZE) 

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
        self.hand.add(card)

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

        return self.hand.delete_at_index(index)

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
        return len(self.hand)
    
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
        return self.hand[index]
