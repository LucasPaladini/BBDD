class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descrpcion(self):
        return "{} es un pokemon de tipo: {}".format(self.nombre, self.tipo)

class Pikachu (Pokemon):
    def ataque(self, tipo_ataque):
        return "{} es de tipo de ataque: {}".format(self.nombre, tipo_ataque)

class Charmander (Pokemon):
    def ataque(self, tipo_ataque):
        return "{} es de tipo de ataque: {}".format(self.nombre, tipo_ataque)

nuevo_pokemon = Pikachu("luk", "peronista")
print(nuevo_pokemon.descrpcion())
