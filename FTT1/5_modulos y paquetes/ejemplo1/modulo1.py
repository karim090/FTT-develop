# vamos a usar este archivo para definir cosas y reutilizarlas en otro lado

class Objeto1:
    nombre=None

    def __init__(self, n):
        self.nombre = n

    def print_nombre(self):
        print(self.nombre)


# tambien podemos tener funciones o variables globales

variable1 = "casa"

def print_prueba():
    print("prueba")