from funciones import menu, es_par, cont_pares, num_primos

menu()

opcion = input("Ingrese una opcion: ")

while True:
    try:
        if opcion == 1:
            num_primos 
        else:
            print ("no es primo.")
    
        if opcion == 2:
            es_par
        else: 
            print("el numero ingresado es impar.")
        
        if opcion == 3:
            cont_pares
        
        if opcion == 4:
            print("usted ha salido del programa. ")
        break
        
    except ValueError:
        opcion = int(input("Dato invalido! ingrese solo numeros, escribe 1 para continuar: "))
 
    except ZeroDivisionError:
        opcion = int(input("Dato invalido! No puedes ingresar 0, Escribe 1 para continuar: "))