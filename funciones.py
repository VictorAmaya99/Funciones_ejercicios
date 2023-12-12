# Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir
# el radio como parámetro y devolver el área.



def calcular_area_circulo(radio = float):

    """Esta funcion retorna el radio del area de un circulo dado

    Returns:
        float: area de un circulo
    """    
    #radio = float(input("Ingrese radio a calcular: "))
    pi = 3.14

    area = pi * radio * radio
    
    return print(f"el area del circulo es: {area:.2f}")

# Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función
# debe imprimir un mensaje indicando si el número es par o impar.

def numero_par_impar(numero = int):
    """Funcion debe verificar si el numero dado es par o impar.

    Args:
        numero (int): devuelve si es par o impar 
    """
    numero = int(input("Ingrese un numero:"))
    if numero % 2 == 0:
        print(f"el numero: {numero} es par")
    else:
        print(f"El numero: {numero} es impar")

#numero_par_impar(31)

# Ejercicio 03: Diseña una función que tome una lista de números y devuelva la suma de
# todos los elementos.

def sumar_elementos(lista = list)->int:
    """funcion suma los numeros de una lista dada

    Args:
        lista (_type_, optional): lista de numeros

    Returns:
        int: resultado de la suma
    """
    suma = 0
    for element in lista:
        suma += element
    return print(f"La suma de los elementos de la lista es: {suma}")

lista_elementos = [2,3,4,3,100]



# Ejercicio 04: Define una función que encuentre el máximo de tres números. La función
# debe aceptar tres argumentos y devolver el número más grande.

def maximo_de_tres_numeros(x: int, y: int, z: int)->int:
    """funcion busca el numero maximo de tres numeros dados

    Args:
        x (int): numero entero
        y (int): numero entero
        z (int): numero entero

    Returns:
        int: El mayor de los numeros dados
    """
    if x > y and x > z:
        print(f"el numero {x} es el mayor de los numeros dados")
    elif y > z:
        print(f"el numero {y} es el mayor de los numeros dados")
    else:
        print(f"el numero {z} es el mayor de los numeros dados")


#maximo_tres_numeros(5,23,11)

# Ejercicio 05: Escribe una función que tome una cadena como entrada y devuelva la
# cadena invertida.

def cadena_invertida(cadena = str):
    """La funcion toma una cadena como entrada y devuelve una cadena invertida.

    Args:
        cadena : Es un string

    Returns:
        _type_: una cadena "string"
    """
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return print(cadena_invertida)

#cadena_invertida("a,b,c,d,e")

# Ejercicio 06: Crea una función que reciba una lista de palabras y devuelva una nueva lista
# con las palabras ordenadas alfabéticamente.

def lista_ordenada(lista=list):
    """Recibe una lista y la ordena alfabeticamente.

    Args:
        lista: lista de strings

    Returns:
        _type_: lista ordenada alfabeticamente
    """
    lista_ordenada = []
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    lista_ordenada.append(lista)
    return print(lista_ordenada)


lista_nombres = ["Juan", "Alma", "Luis", "Omar"]

# lista_ordenada(lista_nombres)

# Ejercicio 07: Diseña una función que calcule la potencia de un número. La función debe
# recibir la base y el exponente como argumentos y devolver el resultado.

def calcular_potencia(base = int, exponente = int)->int:
    """calcula la potencia de un numeros dados como base y exponente.

    Args:
        base: entero.
        exponente: entero.

    Returns:
        int: devuelve un entero
    """
    resultado = base ** exponente
    return print(resultado)

#calcular_potencia(4,3)

# Ejercicio 08: Define una función que reciba una lista de números y devuelva una nueva
# lista con solo los números pares.

def lista_pares(lista=list)->list:
    """La funcion recive una lista de numeros y devuelve una nueva lista de solo los numeros
        pares.

    Args:
        lista: lista de numeros.

    Returns:
        list: lista de numeros pares.
    """
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return print(pares)

lista_numeros = [1,2,3,4,56,6,74,81,9]

#lista_pares(lista_numeros)

# Ejercicio 09: Escribe una función que tome una lista de números y calcule el producto de
# todos los elementos.

def calcular_producto(lista:list):
    """La funcion toma una lista de numeros y calcula el producto de todos los elementos.

    Args:
        lista: lista de numeros

    Returns:
        _type_: entero
    """
    producto = 1
    for numero in lista:
        producto *= numero
    return print(producto)

lista_numeros = [1,2,3,4,5,]

#calcular_producto(lista_numeros)

# Ejercicio 10: Crea una función que determine si una cadena dada es un palíndromo (se lee
# igual de izquierda a derecha que de derecha a izquierda).

def palindromo(cadena=str):
    """La funcion determina si una cadena dada es palindromo.

    Args:
        cadena: string
    """
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    x = 0
    y = len(cadena) - 1

    for i in range(len(cadena)):
        x += 1
        y -= 1
    if cadena[0] == cadena[-1]:
        print("La palabra es palidroma")
       
    else:
        print("La palabra no es palindroma")
       
    
#palindromo("loco")

def menu():
    print("""
        ***Menu de Opciones***
        -----------------------------------------
        1 - Area del circulo
        2 - Numero par o impar
        3 - Suma de todos los elementos
        4 - Maximo de tres numeros
        5 - Cadena invertida
        6 - Lista ordenada alfabeticamente
        7 - Potencia de un numero
        8 - Lista numeros pares
        9 - Producto de todos los elementos
        10 - Cadena palindromo
        """)
    opcion = input("Ingrese opcion: ")
    return opcion
    

def resultados():
    match(menu()):
        case "1":
            calcular_area_circulo(20)

        case "2":
            numero_par_impar(4)
    
        case "3":
            sumar_elementos(lista_elementos)
        
        case "4":
            maximo_de_tres_numeros(32, 890, 345)
    
        case "5":
            cadena_invertida("a,b,c,d,e")
        
        case "6":
            lista_ordenada(lista_nombres)
        
        case "7":
            calcular_potencia(4,3)
        
        case "8":
            lista_pares(lista_numeros)
        
        case "9":
            calcular_producto(lista_numeros)
            
        case "10":
            palindromo("oso")