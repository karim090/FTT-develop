# se puede iterar o recorrer un diccionario, igual que las listas
# usando la funcion "items" convertimos el diccionario en un listado 
# iterable de pares de valores correspondientes a la key y value de cada
# elemento del diccionario

diccionario= {
  "nombre": "karim",
  "apellido": "brizuela",
  "edad": 31
}

for k,v in diccionario.items():
    print("key: " + k + " value: " + v)
