#Hay cuatro estados posibles: rojo, rojo-amarillo,verde
#y amarilllo.
# No poner string, ni arrays, sin primitivas
class Semaforo:
    def __init__(self):
        self.__estado_actual = 0
        self.__estados_disponibles = ["rojo", "rojo-amarillo", "verde", "amarillo"]

    def __str__(self):
        return self.__estados_disponibles[self.__estado_actual]

    def cambiar_de_estado(self):
        if self.__estado_actual == 3:
            self.__estado_actual = -1
        self.__estado_actual += 1

semaforo = Semaforo()
print("\nEl semáforo cambia a los siguientes colores \n")
print(semaforo)     # rojo default
semaforo.cambiar_de_estado()
print(semaforo)     # rojo amarelo
semaforo.cambiar_de_estado()
print(semaforo, "\n")   # verde

semaforo.cambiar_de_estado()
print(semaforo)     # amarelo
semaforo.cambiar_de_estado()
print(semaforo)     # rojo
