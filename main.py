
# Importar el módulo random
import random

# Variables de alcance global
intentos_jugadora = []
intentos_computadora = []

def juego():
    
    numero_aleatorio = random.randint(1, 100)
    #print(numero_aleatorio)
    print('\n¡Hola! Elige un número entre 1 y 100\n')
    
    # El bucle continúa hasta que encuentra al comando break
    while True:

        if jugadora(numero_aleatorio):
            break
       
        if computadora(numero_aleatorio):  
            break


def jugadora(numero_aleatorio):

    numero_jugadora = int(input("Escribe tu número aquí: "))
    intentos_jugadora.append(numero_jugadora)

    if numero_jugadora < numero_aleatorio:
        print("El número es mayor\n¡Turno Computadora!\n")
        return False
    elif numero_jugadora > numero_aleatorio:
        print("El número es menor\n¡Turno Computadora!\n")
        return False
    else:
        print("¡JUGADORA GANA!")
        # Con .join se accede a los elementos de la lista, usando antes map para convertirlos en string
        print (f"Estos son tus intentos: {' - '.join(map(str,intentos_jugadora))}\n¡FELICIDADES!\n")
        return True


def computadora(numero_aleatorio): 

    numero_computadora = random.randint(1, 100)
    intentos_computadora.append(numero_computadora)
    print(f"Computadora elige el número {numero_computadora}")
        

    if numero_computadora < numero_aleatorio:
        print("El número es mayor\n¡Turno Jugadora!\n")
        return False
    elif numero_computadora > numero_aleatorio:
        print("El número es menor\n¡Turno Jugadora!\n")
        return False
    else:
        print("¡COMPUTADORA GANA!")
        print (f"Estos son los intentos de Computadora: {' - '.join(map(str,intentos_computadora))}\n¡FELICIDADES")
        return True


# Se llama a la función juego() al final después de que las demás funciones fueron declaradas
juego()

