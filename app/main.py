class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @classmethod
    def bite(cls, herb):
        if isinstance(herb, Carnivore):
            print(f"{herb} is carnivore")
            return
        if herb.hidden:
            print(f"{cls} cannot bite hidden {herb}")
            return
        if herb.health <= 0:
            print(f"{herb} is dead")
            return
        else:
            herb.health -= 50
            if herb.health <= 0:
                Animal.alive.remove(herb)
