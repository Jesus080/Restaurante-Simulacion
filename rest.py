import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
num_tables = 10  # Número de mesas en el restaurante
arrival_rate = 1/4  # Llegada de clientes cada 4 minutos en promedio
service_rate = 1/30  # Los clientes pasan 30 minutos en promedio en una mesa
simulation_time = 480  # Simulación de 8 horas (480 minutos)

# Variables para la simulación
current_time = 0
next_arrival = np.random.exponential(1 / arrival_rate)  # Tiempo de llegada del primer cliente
tables_occupied = 0
table_release_times = []  # Tiempos en que las mesas se liberarán
queue = []  # Cola de espera de clientes
waiting_times = []  # Tiempos de espera en la cola
customers_served = 0  # Número de clientes atendidos
customers_waiting = 0  # Número de clientes que tuvieron que esperar

# Simulación paso a paso
while current_time < simulation_time:
    # El siguiente evento es la llegada de un cliente o la liberación de una mesa
    if next_arrival <= (min(table_release_times) if table_release_times else float('inf')):
        # Un cliente llega
        current_time = next_arrival
        if tables_occupied < num_tables:
            # Asignar una mesa si hay disponible
            tables_occupied += 1
            service_time = np.random.exponential(1 / service_rate)
            table_release_times.append(current_time + service_time)
        else:
            # Poner al cliente en la cola si no hay mesas disponibles
            queue.append(current_time)
        
        next_arrival = current_time + np.random.exponential(1 / arrival_rate)
    else:
        # Una mesa se libera
        current_time = min(table_release_times)
        table_release_times.remove(current_time)
        tables_occupied -= 1
        customers_served += 1
        
        # Si hay alguien esperando en la cola, asignar la mesa
        if queue:
            arrival_time = queue.pop(0)
            waiting_times.append(current_time - arrival_time)
            customers_waiting += 1
            tables_occupied += 1
            service_time = np.random.exponential(1 / service_rate)
            table_release_times.append(current_time + service_time)

# Resultados
average_waiting_time = np.mean(waiting_times) if waiting_times else 0
print(f"Clientes atendidos: {customers_served}")
print(f"Clientes que esperaron: {customers_waiting}")
print(f"Tiempo promedio de espera en cola: {average_waiting_time:.2f} minutos")

# Graficar tiempos de espera en la cola
plt.figure(figsize=(10, 6))
plt.hist(waiting_times, bins=20, color='orange', edgecolor='black')
plt.title('Distribución de tiempos de espera en cola')
plt.xlabel('Tiempo de espera (minutos)')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()


# Suposiciones:Distribución de tiempos de llegada de clientes: Los clientes llegan según una distribución exponencial.
#Tiempo que los clientes permanecen en una mesa: El tiempo que cada cliente pasa en el restaurante sigue una distribución exponencial.
#Número de mesas: El restaurante tiene un número fijo de mesas disponibles.