import random

# Variables de alcance global
intentos_jugadora = []
intentos_computadora = []

def juego():
    """Si jugadora o computadora aciertan el ciclo se rompe, y se ejecuta repetir juego"""

    global numero_aleatorio
    numero_aleatorio = random.randint(1, 100)
    print('\n¡Hola! Elige un número entre 1 y 100\n')
    
    while True:
        
        if jugadora(numero_aleatorio):
            break
       
        if computadora(numero_aleatorio):  
            break
    
    # Después del break llama a repetir_juego para que se reinicie
    repetir_juego()


def jugadora(numero_aleatorio):
    """Devuelve True cuando la jugadora acierta, caso contrario retorna False"""

    print(">>> Turno Jugadora <<<")
    numero_jugadora = int(input("-> Escribe tu número aquí: "))
    intentos_jugadora.append(numero_jugadora)

    if numero_jugadora < numero_aleatorio:
        print("El número es MAYOR\n")
        return False
    elif numero_jugadora > numero_aleatorio:
        print("El número es MENOR\n")
        return False
    else:
        print("¡JUGADORA GANA!")
        print (f"Estos son tus intentos: {' - '.join(map(str,intentos_jugadora))}\n¡FELICIDADES!\n")
        return True


def computadora(numero_aleatorio): 
    """Devuelve True cuando la computadora acierta, caso contrario retorna False"""

    print(">>> Turno Computadora <<<")
    numero_computadora = random.randint(1, 100)
    intentos_computadora.append(numero_computadora)
    print(f"-> Computadora ha elegido el número: {numero_computadora}")
        

    if numero_computadora < numero_aleatorio:
        print("El número es MAYOR\n")
        return False
    elif numero_computadora > numero_aleatorio:
        print("El número es MENOR\n")
        return False
    else:
        print("¡COMPUTADORA GANA!")
        print (f"Estos son los intentos de Computadora: {' - '.join(map(str,intentos_computadora))}\n¡FELICIDADES")
        return True


def repetir_juego():
    """Reinicia el juego, incluyendo la lista de intentos """

    repetir = input("¿Quieres jugar de nuevo? Escribe si o no: ")
    if repetir == 'si':
        intentos_jugadora.clear()
        intentos_computadora.clear()
        juego()
    else:
        print("¡Fin del juego!¡Espero que te hayas divertido!")
        

if __name__ == '__main__':
    juego()
