import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanza!")
    print("He elegido un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while not adivinado:
        intento = int(input("Ingresa tu adivinanza: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            adivinado = True
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")

juego_adivinanza()
