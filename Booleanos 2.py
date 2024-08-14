# Construir un sistema booleano con objetos (No existe True,False,if)
#and: Devuelve True si ambos operandos son True
#or: Devuelve True si al menos uno de los operandos es True.
#not: Invierte el valor booleano del operando.

## AND
class Verdadero:
    def y(self, otro):
        return otro

    def __str__(self):
        return "verdadero"

    def or_(self, otro):
        return self

    def no(self, otro):
        return falso

class Falso:
    def y(self, otro):
        return self

    def __str__(self):
        return "falso"

    def or_(self, otro):
        return otro

    def no(self, otro):
        return verdadero

verdadero = Verdadero()
falso = Falso()
print("---AND---")
print("Verdadero", verdadero)
print("Falso", falso)
print(verdadero.y(falso))
print(verdadero.y(verdadero))
print(falso.y(falso))
print(falso.y(verdadero),"\n","--------","\n")

print("---OR---")
print("Verdadero", verdadero)
print("Falso", falso)
print(verdadero.or_(falso))
print(verdadero.or_(verdadero))
print(falso.or_(falso))  #
print(falso.or_(verdadero), "\n","--------","\n")

print("---NOT---")
print("Verdadero", verdadero.no(falso))
print("Falso", falso.no(verdadero))
print(verdadero.no)
print(falso.no,"\n","--------","\n")


# verdadero = True
# print(not verdadero)