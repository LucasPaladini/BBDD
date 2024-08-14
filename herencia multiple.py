class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("llamando...")
    def ocupado(self):
        print("ocupado...")

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print("tomando fotos...")

class Reproduccion:
    def __init__(self):
        pass
    def reproduccion_de_musica(self):
        print("reproduciendo musica")
    def reproducir_video(self):
        print("reproducir un video")

class Smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):
        print("telefono apagado")

celular = Smartphone()
print(celular.reproduccion_de_musica(), celular.llamar())
