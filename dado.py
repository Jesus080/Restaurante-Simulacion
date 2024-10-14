import random

# Definir las caras del dado y sus probabilidades
caras = [1, 2, 3, 4, 5, 6]
probabilidades = [1/6] * 6  # Probabilidades uniformes

# Función para lanzar el dado
def lanzar_dado():
    return random.choices(caras, probabilidades)[0]

# Simular lanzamientos del dado
num_lanzamientos = 1000
resultados = []

for _ in range(num_lanzamientos):
    resultado = lanzar_dado()
    resultados.append(resultado)

# Contar la frecuencia de cada cara
frecuencias = {cara: resultados.count(cara) for cara in caras}

# Mostrar resultados
print("Resultados de los lanzamientos del dado:")
for cara, frecuencia in frecuencias.items():
    print(f"Cara {cara}: {frecuencia} veces ({frecuencia/num_lanzamientos * 100:.2f}%)")
