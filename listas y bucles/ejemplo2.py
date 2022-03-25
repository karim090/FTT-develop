# existe la tupla, muy parecido a una lista, pero se usa de manera mas estatica
# no se la mofica luego de haberla definido.

tupla = ("hola", "mundo", "!!!")

# podemos acceder a los elementos de esa tupla por el numero de orden (index)

mensaje = tupla[0] + " " + tupla[1] + " " + tupla[3]
# el agregado de espacios es solo estetico.
print(mensaje)