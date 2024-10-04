import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
num_products = 20  # Número de productos en el lote
mean_times = [5, 7, 4]  # Tiempos promedio de procesamiento en cada estación (en minutos)
std_devs = [1, 1.5, 0.8]  # Desviación estándar de los tiempos de procesamiento
num_stations = 3  # Número de estaciones de trabajo

# Inicializar matrices para guardar los tiempos de procesamiento y finalización
processing_times = np.zeros((num_products, num_stations))
completion_times = np.zeros((num_products, num_stations))

# Simulación del procesamiento de los productos
for i in range(num_products):
    for j in range(num_stations):
        # Generar tiempo de procesamiento aleatorio para cada estación
        processing_time = max(0, np.random.normal(mean_times[j], std_devs[j]))
        processing_times[i, j] = processing_time

        # Calcular el tiempo en que el producto termina en cada estación
        if j == 0:
            # La primera estación depende solo del tiempo de procesamiento
            completion_times[i, j] = processing_time
        else:
            # Las estaciones posteriores dependen del producto anterior y del tiempo de procesamiento
            completion_times[i, j] = max(completion_times[i, j-1], completion_times[i-1, j]) + processing_time

# Resultados
total_time = completion_times[-1, -1]  # Tiempo total en el sistema para el último producto
print(f"Tiempo total para procesar el lote de productos: {total_time:.2f} minutos")

# Graficar tiempos de finalización para cada estación
plt.figure(figsize=(10, 6))
for j in range(num_stations):
    plt.plot(range(1, num_products+1), completion_times[:, j], label=f'Estación {j+1}')
    
plt.title('Simulación de Línea de Producción')
plt.xlabel('Producto')
plt.ylabel('Tiempo de finalización (minutos)')
plt.legend()
plt.grid(True)
plt.show()
