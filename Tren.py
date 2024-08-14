class Tren:
    def __init__(self, locomotora, vagon, bocina):
        self.nombre = "Pepe"
        self.locomotora = locomotora
        self.vagon = vagon
        self.bocina = bocina

    def __str__(self):
        return f" \nEl Tren llamado {self.nombre} tiene la {locomotora.nombre} en el vagon numero {self.locomotora.numero} y suena {self.bocina.ruido}"

class Locomotora:
    def __init__(self):
        self.nombre = "locomotora"
        self.numero = 1

    def __str__(self):
        return {self.nombre, self.numero}

class Vagon:
    def __init__(self, cantidad_vagones):
        self.numero = cantidad_vagones
        self.nombre = "Vagon"

class Bocina:
    def __init__(self):
        self.ruido = "wann"

# agregar un conductor
# los vagones pueden ser de carga o de pasajeros
# distintos tipos de cargas

locomotora = Locomotora()
vagon = Vagon(2)
bocina = Bocina()

print(Tren(locomotora, vagon, bocina))
