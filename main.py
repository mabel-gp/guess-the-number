# TAREA: Generar un número aleatorio entre 1 y 100. Usar la función randint en el módulo random

# Importar el módulo random
import random

numero_aleatorio = random.randint(1,100)
#print(numero_aleatorio)


# TAREA: Implementa un ciclo que solicite a la jugadora que adivine el número, usar función input()
# TAREA: Si la jugadora adivina correctamente, termina el juego
# TAREA: Si la jugadora adivina incorrectamente, proporciona pista sobre si el número es mayor o menor
# TAREA: Implementar la lógica para el turno del ordenador

# Lógica para la jugadora
def jugadora():

    numero_ingresado = int(input("Escribe un numero"))

# Mientras(while) el número ingresado sea diferente al numero aleatorio, continua el ciclo
    while numero_ingresado != numero_aleatorio:

        if numero_ingresado < numero_aleatorio:
            print("El número es mayor ¡Jugadora intenta de nuevo!")
            numero_ingresado = int(input("Escribe un numero"))
        elif numero_ingresado > numero_aleatorio:
            print ("El numero es menor ¡Jugadora intenta de nuevo!")
            numero_ingresado = int(input("Escribe un numero"))

# Esta línea se ejecuta cuando el número ingresado es igual número aleatorio
    print("El número es correcto ¡JUGADORA GANA!")    

jugadora()


# Lógica para la computadora
def computadora():

    numero_computadora = random.randint(1,100)

    while numero_computadora != numero_aleatorio:

        print(f"Computadora elige el número {numero_computadora}")

        if numero_computadora < numero_aleatorio:
            print("El número es mayor ¡Computadora intenta de nuevo!")
        elif numero_aleatorio > numero_aleatorio:
            print ("El numero es menor ¡Computadora intenta de nuevo!")

        numero_computadora = random.randint(1,100)

    print ("El número es correcto ¡COMPUTADORA GANA!")

computadora()