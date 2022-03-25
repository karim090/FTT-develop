# los diccionarios son parecidos a las listas y las tuplas pero tienen una "key"
# una llave principal que es asociada a un valor.


diccionario= {
  "nombre": "karim",
  "apellido": "brizuela",
  "edad": 31
}

# tambien se puede expresar asi
diccionario = dict()
diccionario["nombre"] = "karim"
diccionario["apellido"] = "brizuela"
diccionario["edad"] = 31


print(diccionario)



#los valores tambien pueden ser listados, u otros diccionarios

colores = {
    "principales" : ["azul", "gris", "negro"],
    "secundarios" : ["verde", "amarillo", "rosa"],
}

configuraciones = {
    "nombre" : "karim",
    "apellido": "brizuela",
    "colores" : {
        "principales" : ["azul", "gris", "negro"],
        "secundarios" : ["verde", "amarillo", "rosa"],
    }

}





