# TAREA: Generar un número aleatorio entre 1 y 100. Usar la función randint en el módulo random

# Importar el módulo random
import random

numero_aleatorio = random.randint(1,100)
print(numero_aleatorio) # Después borrar esta línea


# TAREA: Implementa un ciclo que solicite a la jugadora que adivine el número, usar función input()
# TAREA: Si la jugadora adivina correctamente, termina el juego
# TAREA: Si la jugadora adivina incorrectamente, proporciona pista sobre si el número es mayor o menor

# Implementar el input para que la usuaria elija un número
numero_ingresado = int(input("Escribe un numero"))

# Mientras(while) el número ingresado sea diferente al numero aleatorio, continua el ciclo
while numero_ingresado != numero_aleatorio:
    if numero_ingresado < numero_aleatorio:
        print("El número es mayor ¡Intenta de nuevo!")
        numero_ingresado = int(input("Escribe un numero"))
    elif numero_ingresado > numero_aleatorio:
        print ("El numero es menor ¡Intenta de nuevo!")
        numero_ingresado = int(input("Escribe un numero"))

# Esta línea se ejecuta cuando el número ingresado es igual número aleatorio
print("El número es correcto ¡GANASTE!")    



