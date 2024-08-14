# representar un rectangulo a partir de dos puntos, el mismo debe poder calcular su ancho y alto

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.__punto1 = punto1
        self.__punto2 = punto2

    def ancho(self):
        return self.__punto1.distancia_en_x_hacia(self.__punto2)

    def alto(self):
        return self.__punto1.distancia_en_y_hacia(self.__punto2)

    def area(self):
        return self.ancho() * self.alto()

    def transladar(self, distancia_x, distancia_y):
        self.__punto1 = self.__punto1.punto_al_desplazar(distancia_x, distancia_y)
        self.__punto2 = self.__punto2.punto_al_desplazar(distancia_x, distancia_y)

    def __str__(self):
        return f"Rectangulo de {self.ancho()} por {self.alto()}, formado por {self.__punto1} y {self.__punto2}"


class Punto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def distancia_en_x_hacia(self, otro):
        return otro.__x - self.__x

    def distancia_en_y_hacia(self, otro):
        return otro.__y - self.__y

    def punto_al_desplazar(self, distancia_en_x, distancia_en_y):
        return Punto(self.__x + distancia_en_x, self.__y + distancia_en_y)

    def __str__(self):
        return f"{self.__x}@{self.__y}"

un_rectangulo = Rectangulo(Punto(1, 3), Punto(3, 8))
print(un_rectangulo.ancho())
print(un_rectangulo.alto())
print(un_rectangulo.area())
print(un_rectangulo)
un_rectangulo.transladar(3, 5)
print(un_rectangulo)