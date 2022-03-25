full_name = input("Ingresa tu nombre y apellido: ") 
first_name_letter = full_name[0]
last_name = full_name.split(" ")[1]
correo = first_name_letter + last_name + "@craftech.io"
print(correo)


