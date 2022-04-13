class Employee:
    first_name = None
    last_name = None
    salario= None

    def __init__(cls, n, ln):
        cls.first_name = n
        cls.last_name = ln

    def get_email(cls):
        return cls.first_name + cls.last_name + "@craftech.io"

    def calculate_salary(cls):
        return cls.salario

    def get_data(cls):
        return cls.calculate_salary() + cls.get_email()



full_name = input("Ingresa tu nombre y apellido: ")
input_name = full_name.split(" ")[0]
input_last_name = full_name.split(" ")[1]

k = Employee(input_name, input_last_name)
print(k.get_data())
