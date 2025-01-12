import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenidoo al jueego de adivinanza!")
    print("He elegido un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while not adivinado:
        intento = int(input("Inngresaa tu Adivinnanza: "))
        intentos += 1

        if intento < numero_secreto:
            print("Deemasiao Bajo. Inteenta de nuevoo.")
        elif intento > numero_secreto:
            print("Demasiaado Alto. Intenta de nuevoo.")
        else:
            adivinado = True
            print(f"¡Felicidaades! Adivinaste el número {numero_secreto} en {intentos} intentos.")

juego_adivinanza()
