import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución normal
media = 0   # Media
desviacion_estandar = 1  # Desviación estándar
num_muestras = 1000  # Número de muestras

# Generar números aleatorios continuos siguiendo una distribución normal
muestras = np.random.normal(media, desviacion_estandar, num_muestras)

# Crear un histograma de las muestras
plt.hist(muestras, bins=30, density=True, alpha=0.6, color='g')

# Graficar la función de densidad de probabilidad (PDF)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = np.exp(-(x - media)**2 / (2 * desviacion_estandar**2)) / (desviacion_estandar * np.sqrt(2 * np.pi))
plt.plot(x, p, 'k', linewidth=2)

# Configuración del gráfico
plt.title('Histograma de Muestras de Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.grid()
plt.show()
