# 1. Generar un número aleatorio entre 1 y 100. Usar la función randint en el módulo random
# 2. Implementa un ciclo que solicite a la jugadora que adivine el número, usar función input()
# 3. Si la jugadora adivina correctamente, termina el juego
# 4. Si la jugadora adivina incorrectamente, proporciona pista sobre si el número es mayor o menor
# 5. Implementar la lógica para el turno del ordenador
# 6. Continúa el juego hasta que la jugadora o la computadora adivinen correctamente
# 7. Mostrar registro de suposiciones

# Importar el módulo random
import random

numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)

def juego():
    
    intentos = 0
    # El bucle continúa hasta que encuentra al comando break
    while True:
    
        lista_intentos = []
        lista_intentos.append(intentos)
        
        # TURNO JUGADORA

        numero_jugadora = int(input("Escribe un número entre 1 y 100: "))
        intentos = intentos + 1

        if numero_jugadora < numero_aleatorio:
            print("El número es mayor\n¡Turno Computadora!\n")
        elif numero_jugadora > numero_aleatorio:
            print("El numero es menor\n¡Turno Computadora!\n")
        else:
            print("¡JUGADORA GANA!")
            print (f"Lo intentaste {lista_intentos[0]} veces antes de lograrlo. ¡Felicidades!")
            print("Fin del juego")
            # El bucle se detiene dado que el numero de la jugadora es igual al aleatorio 
            break 


        # TURNO COMPUTADORA

        numero_computadora = random.randint(1, 100)
        print(f"Computadora elige el número {numero_computadora}")

        if numero_computadora == numero_aleatorio:
            print("¡COMPUTADORA GANA!")
            print (f"Computadora lo intentó {lista_intentos[0]} veces antes de lograrlo. ¡Felicidades!")
            print("Fin del juego")
            # El bucle se detiene dado que el número de la computadora es igual al aleatorio
            break 
        else:
            print("El número que eligió Computadora es incorrecto\n¡Turno Jugadora!\n")
            
juego()


