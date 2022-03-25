# de esta forma definimos un objeto o clase en python.
class Objeto:
    atributo1 = None
    atributo2 = None

# asi podemos instanciar un objeto y darle valores a sus atributos

objecto = Objeto()
objecto.atributo1 = "attr1"
objecto.atributo2 = "attr2"


# tambien podemos tener funciones de clase propias

class Objeto:
    atributo1 = None
    atributo2 = None

    def funcion1():
        print("esta es la funcion 1")

# vamos a instanciar el objeto y usar su funcion


objecto = Objeto()
objecto.funcion1()



# los objetos tienen un constructor __init__ es una funcion q se ejecuta al crearse una instancia de este
# este se usa para pasarle argumentos al momento de instanciar el objeto

class Objeto:
    atributo1 = None

    def __init__(self, argumento1):
        self.atributo1 = argumento1


# asi instanciamos el objeto dandole su argumento y luego podemos utilizar su atributo con el valor asignado

objecto = Objeto("prueba 1")
print(objecto.atributo1)
