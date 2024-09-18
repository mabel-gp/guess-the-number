# Generar un número aleatorio entre 1 y 100. Usar la función randint en el módulo random

import random

# Cambié el rango de números aleatorios
numero_aleatorio = random.randint(1,5)
print(numero_aleatorio)

# Implementa un ciclo que solicite a la jugadora que adivine el número. Usar función input()

# Implementar el input para que la usuaria elija un número
numero_ingresado = int(input("Escribe un numero"))

# Mientras el número ingresado sea diferente al numero aleatorio, continua el ciclo
while numero_ingresado != numero_aleatorio:
    print("El número es incorrecto ¡Intenta de nuevo!")
    numero_ingresado = int(input("Escribe un numero"))
    
print("El número es correcto ¡GANASTE!")    

