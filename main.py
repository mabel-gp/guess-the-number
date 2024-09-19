# 1. Generar un número aleatorio entre 1 y 100. Usar la función randint en el módulo random
# 2. Implementa un ciclo que solicite a la jugadora que adivine el número, usar función input()
# 3. Si la jugadora adivina correctamente, termina el juego
# 4. Si la jugadora adivina incorrectamente, proporciona pista sobre si el número es mayor o menor
# 5. Implementar la lógica para el turno del ordenador
# 6. Continúa el juego hasta que la jugadora o la computadora adivinen correctamente

# Importar el módulo random
import random

numero_aleatorio = random.randint(1,100)
#print(numero_aleatorio)

def juego():
    
    # El bucle continúa hasta que encuentra al comando break
    while True:

        # Turno Jugadora

        numero_jugadora = int(input("Escribe un número entre 1 y 100: "))

        if numero_jugadora < numero_aleatorio:
            print("El número es mayor\n¡Turno Computadora!\n")
        elif numero_jugadora > numero_aleatorio:
            print("El numero es menor\n¡Turno Computadora!\n")
        else:
            print("¡JUGADORA GANA!")
            # El bucle se detiene dado que el numero de la jugadora es igual al aleatorio 
            break 


        # Turno Computadora

        numero_computadora = random.randint(1,100)
        print(f"Computadora elige el número {numero_computadora}")

        if numero_computadora == numero_aleatorio:
            print("¡COMPUTADORA GANA!")
            # El bucle se detiene dado que el número de la computadora es igual al aleatorio
            break 
        else:
            print("El número que eligió Computadora es incorrecto\n¡Turno Jugadora!\n")
            
juego()



#Función para la jugadora
# def jugadora():

#     numero_jugadora = int(input("Escribe un número entre 1 y 100"))

#     # Mientras(while) el número ingresado sea diferente al numero aleatorio, continua el ciclo
#     while numero_jugadora != numero_aleatorio:

#         if numero_jugadora < numero_aleatorio:
#             print("El número es mayor ¡Jugadora intenta de nuevo!")
#             numero_jugadora = int(input("Escribe un numero"))
#         elif numero_jugadora > numero_aleatorio:
#             print ("El numero es menor ¡Jugadora intenta de nuevo!")
#             numero_jugadora = int(input("Escribe un numero"))

#     # Esta línea se ejecuta cuando el número ingresado es igual número aleatorio
#     print("El número es correcto ¡JUGADORA GANA!")    

# jugadora()


# # Función para la computadora
# def computadora():

#     numero_computadora = random.randint(1,100)

#     while numero_computadora != numero_aleatorio:

#         print(f"Computadora elige el número {numero_computadora}")

#         if numero_computadora < numero_aleatorio:
#             print("El número es mayor ¡Computadora intenta de nuevo!")
#         elif numero_computadora > numero_aleatorio:
#             print ("El numero es menor ¡Computadora intenta de nuevo!")

#         numero_computadora = random.randint(1,100)

#     print ("El número es correcto ¡COMPUTADORA GANA!")

# computadora()


