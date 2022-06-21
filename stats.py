

class Character:
    def __init__(self, name, eyes, hair):
        self.name = name
        self.eyes = eyes
        self.hair = hair

player1 = Character("Yugi", "Blue", "Yellow")
print(player1.name)

player2 = Character("Kaiba", "Brown", "Brown")
print(player2.name)

class Deck:
    def __init__(self, name, count):
        self.name = name
        self.count = count

for Character in (player1, player2):
    print(f"{Character.name} play {Character.deck} deck")
