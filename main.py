
# Importar el módulo random
import random

# Variables de alcance global
intentos_jugadora = []
intentos_computadora = []

def juego():
    
    # Uso global antes de declarar la variable, para decir que es de ámbito global
    global numero_aleatorio
    numero_aleatorio = random.randint(1, 100)
    print('\n¡Hola! Elige un número entre 1 y 100\n')
    
    # El bucle continúa hasta que encuentra al comando break
    while True:
        
        if jugadora(numero_aleatorio):
            break
       
        if computadora(numero_aleatorio):  
            break
    
    # Después del break llama a repetir_juego para que se reinicie
    repetir_juego()


def jugadora(numero_aleatorio):

    numero_jugadora = int(input("-> Escribe tu número aquí: "))
    intentos_jugadora.append(numero_jugadora)

    if numero_jugadora < numero_aleatorio:
        print("El número es MAYOR\n¡Turno Computadora!\n")
        return False
    elif numero_jugadora > numero_aleatorio:
        print("El número es MENOR\n¡Turno Computadora!\n")
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
        print("El número es MAYOR\n¡Turno Jugadora!\n")
        return False
    elif numero_computadora > numero_aleatorio:
        print("El número es MENOR\n¡Turno Jugadora!\n")
        return False
    else:
        print("¡COMPUTADORA GANA!")
        print (f"Estos son los intentos de Computadora: {' - '.join(map(str,intentos_computadora))}\n¡FELICIDADES")
        return True


def repetir_juego():

    repetir = input("¿Quieres jugar de nuevo? Escribe si o no: ")
    if repetir == 'si':
        intentos_jugadora.clear()
        intentos_computadora.clear()
        juego()
    else:
        print("¡Espero que te hayas divertido!")
        

# Se llama a la función juego() al final después de que las demás funciones fueron declaradas
juego()
