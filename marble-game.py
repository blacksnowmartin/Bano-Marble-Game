import random

class Marble:
    def __init__(self, name):
        self.name = name

class Hole:
    def __init__(self):
        self.is_occupied = False

def main():
    player1_marble = Marble("Player 1 Marble")
    player2_marble = Marble("Player 2 Marble")

    hole = Hole()

    while True:
        input("Press Enter to shoot...")

        if not hole.is_occupied:
            # Simulate shooting and check if the marble enters the hole
            if random.random() < 0.5:
                hole.is_occupied = True
                print("Marble entered the hole! Player can now hit opponent's marble.")
            else:
                print("Missed! Marble did not enter the hole.")

        if hole.is_occupied:
            # Allow the player to hit the opponent's marble
            hit_opponent = input("Do you want to hit opponent's marble? (y/n): ")
            if hit_opponent.lower() == 'y':
                hole.is_occupied = False
                print("Player scored a point by hitting opponent's marble!")
            else:
                print("Player chose not to hit opponent's marble. Turn ends.")

        print("\nCurrent Game State:")
        print(f"{player1_marble.name}: {'' if hole.is_occupied else 'not '}in hole")
        print(f"{player2_marble.name}: {'' if hole.is_occupied else 'not '}in hole")
        print("\n-----------------------------\n")

if __name__ == "__main__":
    main()
