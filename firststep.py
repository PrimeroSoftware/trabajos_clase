# %% // Al poner esto en la primera linea del archivo, se le indica a Jupyter que es un script de Python
# Declaracion Variable Numerica
numero = 10.0 # float

numero2 = 40 # int

# El resultado de la suma de dos numeros tiene el tipo de tipo de mayor importancia
resultado = numero + numero2 
print(resultado)
print(type(numero), type(resultado))
# %%
# Declaracion Variable String
# Se puede usar comillas simples o dobles
nombre = "Daniel"

nombre = 'Pepito'
# len es una funcion que devuelve el numero de caracteres de un string
print(type(nombre))
print(nombre[5], nombre[len(nombre)-1], len(nombre), nombre[-len(nombre)])
# %%
# Variable Boolean o Logica
es = True
es2 = False
print(type(es), type(es2))
# Operadores Logicos
print(es and es2) # and Falso
print(es or es2) # or Verdadero
print(not es) # not Negacion de Verdadero

# La variable "condicion" es el resultado de la operacion logica
condicion = es and es2
print(condicion)
condicion = condicion or 25 > 10
if condicion:
    print("La condicion es verdadera")
else:
    print("La condicion es falsa")
# %%
# Estructras de Control
# Condicionales
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

# Se compara 2 numero por medio de operadores de comparacion
# if condicion:
#     accion si condicion es verdadera
# elif condicion2:
#     accion si condicion2 es verdadera
# else:
#     accion si condicion es falsa
if numero1 > numero2:
    print("El primer numero es mayor que el segundo")
elif numero1 < numero2:
    print("El segundo numero es mayor que el primero")
else:
    if numero1 * 10 < numero2:
        print("El primer numero es menor que el segundo por un factor de 10")
    print("Los numeros son iguales")

numero1 = int(input("Ingrese un numero: "))
match numero1:
    case 1:
        print("El numero es uno")
    case 2:
        print("El numero es dos")
    case 3:
        print("El numero es tres")
    case _:
        print("El numero no es ni uno, ni dos, ni tres")
        
if numero1 == 1:
    print("El numero es uno")
elif numero1 == 2:
    print("El numero es dos")
elif numero1 == 3:
    print("El numero es tres")
else:
    print("El numero no es ni uno, ni dos, ni tres")

# %%
# Estracturas de Control
# Ciclos // Iterativas
# While // Mientras
contador = 0
while contador < 10:
    print("Contador:", contador)
    contador += 1  # Incrementa el contador en 1
    # contador = contador + 1  # Otra forma de incrementar el contador
    
# For // Para
palabra = "Python1234"
print(range(10))  # Muestra los numeros del 0 al 9
for i in range(10):  # Itera desde 0 hasta 9
    print("Contador:", i, "Letra: ", palabra[i])

for letra in "Python1234":
    print("Letra:", letra)

# %%
# Trabajo con Cadenas de Texto
cadena1 = 'Hola'
cadena2 = 'Mundo'
pizza = "Pizzaron"
print("Hola Mundo")
print(cadena1 + " " + cadena2)  # Concatenacion de cadenas
print(cadena1 * 3)  # Repeticion de cadenas
print(pizza[0:2])  # Me devuelve los dos primeros caracteres de la cadena
print(pizza[2:4])
print("{} mi {} de {}".format(cadena1, cadena2, pizza))
print(f"{cadena1} mi {cadena2} de {pizza}")  # Formateo de cadenas con f-strings
print(f'''{cadena1} 
      mi {cadena2} 
      de {pizza}''') 
print('12345'.isdigit())  # Verifica si la cadena es un numero
# %%
from pprint import pprint as pp

mylista = [1, 2, 3, 4, 5, 7]
for item in mylista[-3:-1]:
    print(item)

mylista.append(6)  # Agrega un elemento al final de la lista
mylista.insert(0, 0)  # Agrega un elemento al inicio de la lista
mylista.reverse()
print(mylista)  # Invierte el orden de los elementos de la lista
mylista.sort()  # Ordena la lista
print(mylista)  # Muestra la lista ordenada

tablas = []
for i in range(1, 11):
    tabla = []
    for j in range(1, 10):
        tabla.append(i * j)
    tablas.append(tabla)
mylista.pop()  # Elimina el ultimo elemento de la lista
pp(tablas)  # Muestra las tablas de multiplicar del 1 al 10
print(list(range(1, 11)))
print(list(cadena1+cadena2))

#Tuplas
mytuple = tuple(mylista)  # Convierte la lista en una tupla
print(mytuple)  # Muestra la tupla
otratupla = (1, 2, 3, 4, 5)  # Crea una tupla

# Diccionarios
mydiccionario = {
    "nombre": "Daniel",
    "edad": 30,
    "lenguajes": ["Python", "JavaScript", "C++"]
}
print(mydiccionario)  # Muestra el diccionario
print(mydiccionario["nombre"])  # Accede al valor de la clave "nombre"
print(mydiccionario.get("nombre"))  # Accede al valor de la clave "nombre" usando get
print(mydiccionario["lenguajes"][0])  # Accede al primer elemento de la lista de lenguajes
mydiccionario["lenguajes"].append("Java")  # Agrega un nuevo lenguaje a la lista
mydiccionario["apellido"] = "Perez"  # Agrega una nueva clave al diccionario
pp(mydiccionario, sort_dicts=False)  # Muestra el diccionario actualizado

print(f'''
Apellido : {mydiccionario['apellido']}
Nombre   : {mydiccionario['nombre']}
Edad     : {mydiccionario['edad']}
Lenguaje : {mydiccionario['lenguajes'][1]}
      ''')
# %%
# Listas por Comprension
lista_numeros = [1,2,6,5,8,4,5,9,6,2]
for item in lista_numeros:
    print(item, end=" ")

lista2 = list(range(1, 11))
print(lista2)

#Numero del 1 al 500 pares
# Con Compresion de listas
lista3 = [item for item in range(1,501) if item % 2 == 0]
print(lista3)

# Con un ciclo for
lista4 = []
for item in range(1, 501):
    if item % 2 == 0:
        lista4.append(item)
print(lista4)
# %%
#Funciones con paraemtros args
print("")
xx = (1, 2, 3, 5, 6, -7, 8, 9, 10)
def calculos(*args, operacion='suma'):
    '''
    Calcula segun la operacion ingresada el resultado
    Tomando para la operacion los valores numericos (int o float) que se le pasen como argumentos.
    Si no se pasan argumentos, devuelve 0.
    '''
    resultado = 0
    # Verifico que realmente se hayan pasado argumentos
    if args:
        if operacion == 'suma':
            for numero in args:
                if type(numero) == int or type(numero) == float:
                    resultado += numero
        elif operacion == 'resta':
            for numero in args:
                if type(numero) == int or type(numero) == float:
                    resultado -= numero
        else:
            return f"Operación '{operacion}' no reconocida. Usando suma por defecto."
    else:
        return "No se han pasado argumentos, el resultado es 0"
            
    return resultado

def test_calculos():
    """
    Prueba de la funcion calculos con diferentes casos.
    """
    values = []
    value = ''
    while value.lower() != 'exit':
        value = input("Ingrese un numero o 'exit' para salir: ")
        if value.isdigit():
            values.append(int(value))
        else:
            print(f'Por favor, el valor "{value}" no es valido, ingrese un valor valido.')

    print(f"Suma es: {calculos(*values)}")
    print("Resta es: ", calculos(*values, operacion='resta'))

#test_calculos()

funcion = "(2 + 3) * 4"
def evalua_funcion(pfuncion):
    """
    Evalua una funcion matematica en formato string y devuelve el resultado.
    """
    print(f"Evaluando la funcion: {eval(pfuncion)}")
    lista = list(pfuncion)
    print(f"Lista de caracteres: {lista}")
evalua_funcion(funcion)


    
# %%
def mostrar_datos(*args, **kargs):
    resp = ""
    # if testp:
    #     resp += f"Parametro testp: {testp}\n"
    if args:
        for arg in args:
            print(f"- {arg}")
        resp += f"Se recibieron parametros posicionales \n"
    if kargs:
        if "lenguajes" in kargs:
            print("Lenguajes de programacion:")
            for lenguaje in kargs["lenguajes"]:
                print(f"- {lenguaje}")
        if "testpp" in kargs and kargs["testpp"] != "x":
            resp += f"Parametro testpp: {kargs['testpp']}\n"
        for item in kargs:
            print(item)
        resp += f"Se recibieron parametros posicionales tipo clave valor \n"
    return resp

mydiccionario = {
    "nombre": "Daniel",
    "edad": 30,
    "lenguajes": ["Python", "JavaScript", "C++"]
}

for clave, valor in mydiccionario.items():
    print(f"{clave}: {valor}")

print(mostrar_datos(*("Python", "JavaScript", "C++"), nombre="Daniel", edad=30, lenguajes=["Python", "JavaScript", "C++"]))
#mostrar_datos(**mydiccionario)
#mostrar_datos(nombre="Daniel", edad=30, lenguajes=["Python", "JavaScript", "C++"])
