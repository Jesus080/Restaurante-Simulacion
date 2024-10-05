import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
arrival_rate = 1 / 5  # Tasa de llegada de clientes (1 cliente cada 5 minutos en promedio)
service_rate = 1 / 8  # Tasa de servicio (cada cliente tarda en promedio 8 minutos en ser atendido)
simulation_time = 500  # Tiempo total de simulación en minutos

# Inicializar variables
arrival_times = []  # Tiempos de llegada de cada cliente
service_times = []  # Duración del servicio de cada cliente
waiting_times = []  # Tiempo de espera en cola
departure_times = []  # Tiempo en que cada cliente sale del sistema
queue_length = []  # Número de clientes en cola en cada minuto de la simulación

# Simulación de llegadas y servicios
current_time = 0
while current_time < simulation_time:
    # Tiempo entre llegadas de clientes
    interarrival_time = np.random.exponential(1 / arrival_rate)
    current_time += interarrival_time
    if current_time > simulation_time:
        break
    arrival_times.append(current_time)
    
    # Tiempo de servicio
    service_time = np.random.exponential(1 / service_rate)
    service_times.append(service_time)

# Simulación de atención de los clientes
next_available_time = 0  # Tiempo en que el servidor estará disponible
for i in range(len(arrival_times)):
    if arrival_times[i] >= next_available_time:
        # Cliente es atendido inmediatamente
        waiting_time = 0
        departure_time = arrival_times[i] + service_times[i]
    else:
        # Cliente debe esperar en cola
        waiting_time = next_available_time - arrival_times[i]
        departure_time = next_available_time + service_times[i]
    
    waiting_times.append(waiting_time)
    departure_times.append(departure_time)
    next_available_time = departure_time

# Resultados
average_waiting_time = np.mean(waiting_times)
average_time_in_system = np.mean(np.array(waiting_times) + np.array(service_times))

print(f"Tiempo promedio de espera en cola: {average_waiting_time:.2f} minutos")
print(f"Tiempo promedio total en el sistema: {average_time_in_system:.2f} minutos")

# Graficar tiempos de espera
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, waiting_times, label='Tiempo de espera', color='orange')
plt.title('Simulación de Espera en la Cola (Sistema de Atención)')
plt.xlabel('Tiempo de llegada (minutos)')
plt.ylabel('Tiempo de espera (minutos)')
plt.grid(True)
plt.legend()
plt.show()
