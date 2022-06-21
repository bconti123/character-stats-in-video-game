class Characters:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def basicAttack(self):
        return self.attack

class Goo(Characters):
    def __init__(self, name, attack, defense):
        super().__init__(name, attack, defense)

    def basicAttack(self):
        return self.attack + 60

class Wolf(Characters):
    def __init__(self, name, attack, defense):
        super().__init__(name, attack, defense)

    def basicAttack(self):
        return self.attack + 55

ListofCharacter = [Goo("Goo", 20, 25), Wolf("Wolf", 30, 10)]

for duel in ListofCharacter:
    print(duel.name, "does", duel.basicAttack(), "damage")
player1 = Goo("goo", 55, 50)
player2 = Wolf("Wolf", 35, 100)


input_b = int(input("enter :"))
print(player1.attack + input_b)

if player1.attack - player2.defense > player2.attack - player1.defense:
    print(player1.name, " has ", player1.attack, " vs ", player2.name, player2.attack)
    print(player1.name + " win")
else:
    print(player1.name, " has ", player1.attack, " vs ", player2.name, player2.attack)
    print(player2.name + " win")
