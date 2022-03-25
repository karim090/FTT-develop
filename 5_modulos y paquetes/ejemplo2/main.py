
# podemos importar varios modulos desde un paquete
from paquete.modulo1 import Objeto1
from paquete.modulo2 import Objeto2
from paquete.modulo3 import Objeto3

# o bien 
from paquete import modulo1, modulo2, modulo3
# y usar
modulo1.Objeto1
modulo2.Objeto2
modulo3.Objeto3
#


objeto = modulo1.Objeto1("prueba")
objeto.print_nombre()


