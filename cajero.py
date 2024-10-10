import numpy as np
import matplotlib.pyplot as plt
import random

# Parámetros de la simulación
total_time = 60  # Simular por 60 minutos
arrival_rate = 0.5  # Tasa de llegada de clientes (clientes por minuto)
service_rate = 1.0  # Tasa de servicio (transacciones por minuto)

# Inicializar variables
time = 0
queue = []  # Cola de clientes
waiting_times = []  # Tiempos de espera para los clientes
served_customers = 0  # Contador de clientes atendidos
busy_until = 0  # Tiempo en que el cajero estará ocupado

# Simulación de 60 minutos
while time < total_time:
    # Generar el tiempo de llegada del siguiente cliente (distribución exponencial)
    time_to_next_arrival = np.random.exponential(1 / arrival_rate)
    time += time_to_next_arrival
    
    if time > total_time:
        break
    
    # Si el cajero está libre, atender al cliente inmediatamente
    if time >= busy_until:
        service_time = np.random.exponential(1 / service_rate)
        busy_until = time + service_time
        waiting_times.append(0)  # No tuvo que esperar
        served_customers += 1
    else:
        # Si el cajero está ocupado, agregar el cliente a la cola
        queue.append(time)

    # Atender a los clientes en cola si el cajero se libera
    while queue and time >= busy_until:
        # Atender al siguiente cliente en la cola
        arrival_time = queue.pop(0)
        service_time = np.random.exponential(1 / service_rate)
        waiting_time = busy_until - arrival_time
        waiting_times.append(waiting_time)
        busy_until += service_time
        served_customers += 1

# Resultados de la simulación
average_waiting_time = np.mean(waiting_times)
print(f"Clientes atendidos: {served_customers}")
print(f"Tiempo promedio de espera: {average_waiting_time:.2f} minutos")

# Graficar la distribución de los tiempos de espera
plt.hist(waiting_times, bins=20, color='lightblue', edgecolor='black')
plt.title('Distribución de los tiempos de espera en el cajero automático')
plt.xlabel('Tiempo de espera (minutos)')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
