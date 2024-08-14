# No poner string, ni arrays, ni primitivas

class Semaforo:
    def __init__(self):
        self.señal = Detencion()
        self.luces_activas = self.señal.combinacion_de_luces()

    def __str__(self):
        return self.luces_activas

    def transicionar(self):
        self.señal = self.señal.siguiente()
        self.luces_activas = self.señal.combinacion_de_luces()


class Detencion:
    def __eq__(self, other):
        return self.__class__ == other.__class__

    def siguiente(self):
        return Avance()

    def combinacion_de_luces(self):
        return "ROJO"


class Avance:
    def __eq__(self, other):
        return self.__class__ == other.__class__

    def combinacion_de_luces(self):
        return "ROJO-AMARILLO"

    def siguiente(self):
        return Paso()


class Paso:
    def __eq__(self, other):
        return self.__class__ == other.__class__

    def combinacion_de_luces(self):
        return "VERDE"

    def siguiente(self):
        return Precaucion()


class Precaucion:
    def __eq__(self, other):
        return self.__class__ == other.__class__

    def combinacion_de_luces(self):
        return "AMARILLO"

    def siguiente(self):
        return Detencion()


semaforo = Semaforo()
print(semaforo)
semaforo.transicionar()
print(semaforo)
semaforo.transicionar()
print(semaforo)
semaforo.transicionar()
print(semaforo)
semaforo.transicionar()
print(semaforo)
