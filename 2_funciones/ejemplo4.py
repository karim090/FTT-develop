# las variables tambien pueden guardar el resultado de una funcion
# siempre y cuando la funcion ejecutada tenga definia una salida
# para esto se usa "return"

def generador_de_saludo(nombre):
    mensaje = "Hola " + nombre + "!"
    return mensaje

nombre = generador_de_saludo("José Cuervo")
print(nombre)


# si la funcion que ejecutamos dentro de una variable no tiene return
# nuestra variable tendra un valor nulo (None) 