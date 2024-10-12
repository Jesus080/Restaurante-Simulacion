import random

# Generar un número entero aleatorio entre un rango específico
def generar_numero_entero(minimo, maximo):
    return random.randint(minimo, maximo)

# Generar un número de punto flotante aleatorio entre un rango específico
def generar_numero_flotante(minimo, maximo):
    return random.uniform(minimo, maximo)

# Generar un número aleatorio de una secuencia
def elegir_elemento(lista):
    return random.choice(lista)

# Generar una lista de números aleatorios únicos
def generar_lista_unica(tamano, minimo, maximo):
    return random.sample(range(minimo, maximo + 1), tamano)

# Ejemplos de uso
if __name__ == "__main__":
    print("Número entero aleatorio entre 1 y 10:", generar_numero_entero(1, 10))
    print("Número de punto flotante aleatorio entre 0.0 y 1.0:", generar_numero_flotante(0.0, 1.0))
    
    lista = ['manzana', 'banana', 'cereza', 'datil']
    print("Elemento aleatorio de la lista:", elegir_elemento(lista))
    
    print("Lista de 5 números aleatorios únicos entre 1 y 20:", generar_lista_unica(5, 1, 20))
