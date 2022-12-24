class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, ciliindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = ciliindrada
        

coche = Coche('verde', 'ruedas nuevas', '5 puertas', '220 km/h', '1900 cc')

print(coche.__dict__)