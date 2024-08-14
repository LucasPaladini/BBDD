class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3

numeros_sumar = Matematica()
numeros_sumar.suma()
#print(numeros_sumar.n1 + numeros_sumar.n2)

class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1/n2

#operacion = Calculadora(1,2)
#print(operacion.producto)


class Ropa:
    def __init__(self):
        self.marca = "DC"
        self.talla = "M"
        self.color = "Azul"

campera = Ropa()
print("El talle de la campera es", campera.talla, "y su color es:", campera.color)



