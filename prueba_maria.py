from os import system

# IMPORTANTE:
# las funciones comunmente son definidas con " def nombre_funcion(): "
# pero python version 3, soporta ingresar el tipo de datos de las variables que son ingresadas en la funcion
# ademas del tipo de dato que retorna la funcion
# ----------------
# yo lo encuentro mas seguro porque asi defines altiro el tipo de dato que debe ingresar y lo que retorna (esto se hace en lenguajes tipados)
# esto en python es totalmente opcional, por lo que escribir esto:
# def es_primo(numero: int) -> str:
# es lo mismo que esto
# def es_primo(numero):


def menu() -> None:
    print(f"""
    -----------------------------------------------------------------------
                            MENU DEL PROGRAMA
    -----------------------------------------------------------------------
          
    1. Verificar si un número es primo.
    2. Verificar si un número es par o impar
    3. Calcular la suma de los números pares ingresados hasta el momento.
    4. Salir del programa
          
    -----------------------------------------------------------------------
    """)

# funcion que verifica si un numero es primo o no
def es_primo(numero: int) -> str:
    for i in range(2, numero):
        if numero % i == 0:
            return print(f"El número {numero} NO es primo")
        
    return print(f"El número {numero} es primo")

# funcion que verifica si un numero es par o no
def es_par(numero: int) -> str:
    if numero % 2 == 0:
        return print(f"El número {numero} es par")
    else:
        return print(f"El número {numero} es impar")

# funcion que calcula la suma de los numero pares ingresados por el usuario
def calcular_suma_pares(numeros_ingresados: list[int]) -> str:
    # aqui ocupo una variable "suma" que contendra la suma de los valores, esto se puede hacer de varias formas
    suma = 0
    for i in range(len(numeros_ingresados)):
        if numeros_ingresados[i] % 2 == 0:
            suma = suma + numeros_ingresados[i]

    return print(f"La suma de los numeros pares ingresados hasta el momento es: {suma}")

# funcion que verificar si el numero ingresado por el usuario es entero y positivo
def verificar_numero(numero: int) -> bool:
    # type() te retorna el tipo de datos de la variable (int, float, str, etc) y verifico si es distinto de int
    # o si el numero convertido a entero es menor que 1 por lo tanto es negativo
    if (type(numero) != int) or (int(numero) < 1):
        print(f"El número ingresado {numero} no es entero y/o es menor que 0.")
        return False
    return True

# funcion que verifica si la opcion ingresada por el usuario es entero y esta dentro de las opciones permitidas (1-4)
def verificar_opcion(opcion: int) -> bool:
    opciones_permitidas = [1,2,3,4]
    if (type(opcion) != int) or (opcion not in opciones_permitidas):
        print(f"La opción {opcion} no es válida")
        return False
    return True


# declaro este arreglo que va a contener todos los numeros ingresados por el usuario
numeros_ingresados = []

# bucle while para ejecutar el programa
# se usa try y except para manejar errores y en caso de ingresar una opcion 4 con "break" se sale del bucle y del programa
# ademas se usan funciones para validar la opcion ingresada y el numero
while True:
    try:
        # realizo el menu en una funcion aparte para ocupar funciones 
        menu()
        opcion = int(input("Ingrese su opción: "))
        es_opcion_valida = verificar_opcion(opcion)
        if es_opcion_valida == False:
            # con "continue" se salta todo el codigo que sigue y vuelve a generar el bucle (se puede usar en while, for, etc)
            continue

        if opcion == 4:
            print(f"¡Gracias por utilizar el programa!")
            # con "break" se sale del bucle (se puede usar en while, for, etc)
            break
        elif opcion == 3:
            calcular_suma_pares(numeros_ingresados)
        
        numero = int(input("Ingrese un número: "))

        # se verifica si el numero es entero y positivo
        verificar_numero(numero)
        numeros_ingresados.append(numero)

        if opcion == 1:
            es_primo(numero)
        elif opcion == 2:
            es_par(numero)
    
    # manejo de excepciones 
    except Exception as error:
        print("Error al ejecutar el programa")