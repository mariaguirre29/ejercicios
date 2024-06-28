def menu( ):
    print("1. Verificar si un número es primo.")
    print("2. Verificar si un número es par o impar.")
    print("3. Calcular la suma de los números pares ingresados hasta el momento.")
    print("4. Salir del programa.")
    

def num_primos( ): 
        num=int("ingrese un numero")
        for i in range(1, num):
            if num % i == 0:
                return print(f"El número {num} NO es primo")
        with open ("n_primos.txt" , 'w') as archivo:
            archivo.write( )
            
        return print(f"El número {num} es primo")

def es_par( ):
        num=int("ingrese un numero")
        cont_pares = 0
        if num % 2 == 0:
            print(f"El numero {num} es par")
            contpar=contpar+num


def cont_pares( ):
    print(f"la suma de los numeros pares es: {cont_pares}")

    return print(f"La suma de los numeros pares ingresados hasta el momento es: {cont_pares}")