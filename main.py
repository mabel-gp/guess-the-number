import random


def juego():
    """Si jugadora o computadora aciertan el ciclo se rompe, y se ejecuta repetir juego"""

    intentos_jugadora = []
    intentos_computadora = []
    numero_aleatorio = random.randint(1, 100)
    print('\n¡Hola! Elige un número entre 1 y 100\n')
    
    while True:
        
        if turno_jugadora(numero_aleatorio, intentos_jugadora):
            break
       
        if turno_computadora(numero_aleatorio, intentos_computadora):  
            break
    
    # Después del break llama a repetir_juego para que se reinicie
    repetir_juego(intentos_jugadora, intentos_computadora)


def turno_jugadora(numero_aleatorio, intentos_jugadora):
    """Devuelve True cuando la jugadora acierta, caso contrario retorna False"""

    print(">>> Turno Jugadora <<<")

    try:
        numero_jugadora = int(input("-> Escribe tu número aquí: "))
        intentos_jugadora.append(numero_jugadora)
    except ValueError:
        print("Tu entrada es inválida, por favor ingresa un número entre 1 y 100\n")
        return False

    if numero_jugadora < 1 or numero_jugadora > 100:
        print("Por favor ingresa un número dentro del rango\n")
        return False

    if numero_jugadora < numero_aleatorio:
        print("El número es MAYOR\n")
        return False
    elif numero_jugadora > numero_aleatorio:
        print("El número es MENOR\n")
        return False
    else:
        print("¡JUGADORA GANA!")
        print (f"Estos son tus intentos: {' , '.join(map(str,intentos_jugadora))}\n¡FELICIDADES!\n")
        return True


def turno_computadora(numero_aleatorio, intentos_computadora): 
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
        print (f"Estos son los intentos de Computadora: {' - '.join(map(str,intentos_computadora))}\n¡FELICIDADES!\n")
        return True


def repetir_juego(intentos_jugadora, intentos_computadora):
    """Reinicia el juego, incluyendo la lista de intentos """

    repetir = input("¿Quieres jugar de nuevo? Escribe si o no: ").lower()
    if repetir == 'si':
        intentos_jugadora.clear()
        intentos_computadora.clear()
        juego()
    elif repetir == 'no':
        print("\n¡Fin del juego!¡Espero que te hayas divertido!\n")
        

if __name__ == '__main__':
    juego()
