# en este ejemplo importamos de un modulo externo (un archivo .py) la clase Objeto1
from modulo1 import Objeto1


# luego lo instanciamos y podemos usar sus funciones.

objeto = Objeto1("nombre1")
objeto.print_nombre()

# para importar mas elementos de un mismo modulo podemos hacerlo asi

from modulo1 import Objeto1, print_prueba, variable1

# o tambien podemos importar el modulo entero y tener disponibles todos sus elementos

import modulo1

objeto2 = modulo1.Objeto1("nombre2")
objeto2.print_nombre()
print(modulo1.variable1)
modulo1.print_prueba()