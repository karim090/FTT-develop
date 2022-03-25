# tambien hay operadores logicos "and", "or" y "not" que permiten agrupar expresiones booleanas

# and	Devuelve True si ambos elementos son True -> True and True = True
# or	Devuelve True si al menos un elemento es True -> True or False = True
# not	Devuelve el contrario, True si es Falso y viceversa	-> not True = False

variable1 = "azul"
variable2 = "importado"


if variable1 is "azul" and variable2 is not "importado":
    print("es azul y nacional")
elif variable1 is "azul" and variable2 is "importado":
    print("es azul e importado")
else:
    print("ni azul ni importado")



