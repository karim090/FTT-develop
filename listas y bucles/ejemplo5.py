# los bucles son utilizador para generar repeticiones de funciones ejecutadas 
# de manera mas corta
# en python existen los bucles "for" y "while"
# while <condition>:
#     <code>
# este codigo quiere decir "mientras el valor de la condicion sea True ejecutar
# todo este codigo" una vez que i toma el valor de 10, se saltea el bloque entero
# y continua la ejecucion del resto del codigo


print("inicio")
i=0
while i < 10:
    print("teracion numero: " + str(i))
    i = i + 1
print("fin")


# tambien los bucles se usan para recorrer los elementos de una lista

lista = ["cordoba", "santa fe", "la rioja", "catamarca"]
for n in lista:
    print(n)

# otra forma de recorrer la mismta lista
i = 0
while lista:
    print(lista[i])
    i = i + 1