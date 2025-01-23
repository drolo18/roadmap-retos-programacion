"""
Funciones definidas por el usuario
"""

# Sinple

def Greet():
    print ("Hola python")

Greet()

# Con retorno

def return_Greet():
    return "Hola python!"

print (return_Greet())

# Con un argumento

def arg_Greet(name):
    print (f"Hola {name}!")

arg_Greet("drolo18")

# Con varios argumentos

def args_Greet(name, age):
    print (f"Hola {name}! tienes {age} años")

args_Greet("drolo18", 37)
args_Greet(age=37, name="drolo18")

# Con un argumento por predeterminado   

def defaultarg_Greet(name = "python"):
    print (f"Hola {name}!") 

defaultarg_Greet()
defaultarg_Greet("drolo18")

# con argumentos y retorno

def argreturnargs_Greet(name, age):
    return f"Hola {name}! tienes {age} años"

print (argreturnargs_Greet("drolo18", 37))

# con retorno de varios valores

def multiple_return_Greet():
    return "Hola", "python"

Greet, name= multiple_return_Greet()
print (f"{Greet} {name}")

# con un numero variable de argumentos

def variable_args_Greet(*names):
    for name in names:
        print (f"Hola {name}!") 

variable_args_Greet("drolo18", "python")

# Con un número variable de argumentos y palabra clave


def variable_key_args_Greet(**names):
    for value, key in names.items():
        print (f"Hola, {value}, {key}!")

variable_key_args_Greet(
    language="python", 
    name="drolo18", 
    edad=37
    )

"""
Funciones dentro de funciones
"""

def outer_function():   
    def inner_function():
        print ("Funcion interna: Hola python!")
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in functions)
"""

print (len("drolo18"))
print (type("drolo18"))
print (int("18"))
print (str(18)) 
print (float(18))
print (bool(18))
print (list("drolo18"))
print (tuple("drolo18"))
print (set("drolo18"))
print (range(18))
print ("drolo18".upper())
print ("drolo18".lower())
print ("drolo18".capitalize())
print ("drolo18".title())
print ("drolo18".strip())

"""
Variables locales y globales
"""

global_var = "python"
print (global_var)

def hello_python():
    local_var = "Hola"
    print (f"{local_var}, {global_var}")

hello_python()

# print (local_var) es  una variable local y no se puede acceder desde fuera de la función

"""
Extra
"""

def print_numbers(fizz, buzz) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0: 
            print (fizz + buzz)
        elif number % 3 == 0: 
            print (fizz)
        elif number % 5 == 0: 
            print (buzz)
        else: 
            print (number)
            count += 1
    return count

        
print(print_numbers("fizz", "buzz"))

# End