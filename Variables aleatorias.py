
# Descripción:
# Simula tiempos de atención de clientes con distribución normal
# y calcula probabilidades usando funciones estadísticas.


# numpy genera datos, matplotlib grafica, y scipy.stats permite calcular probabilidades con la distribución normal.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1️⃣ Parámetros de la distribución
media = 10      # media (mu)
desviacion = 2  # desviación estándar (sigma)
n = 1000        # cantidad de datos simulados

# 2️⃣ Generar variable aleatoria continua (Normal)
tiempos = np.random.normal(media, desviacion, n)

# 3️⃣ Mostrar ejemplos
print("Ejemplos de tiempos generados (en minutos):")
print(tiempos[:10])

# 4️⃣ Calcular probabilidad: tiempo < 12 minutos
prob_menor_12 = norm.cdf(12, loc=media, scale=desviacion) #Calcula la probabilidad acumulada de que el valor sea menor que 12.
print(f"\nProbabilidad de que el cliente sea atendido en menos de 12 minutos: {prob_menor_12:.4f}")

# 5️⃣ Crear histograma + curva de densidad
x = np.linspace(0, 20, 1000)  # rango de valores
densidad = norm.pdf(x, loc=media, scale=desviacion) #Calcula la densidad de probabilidad en cada punto x.

plt.figure(figsize=(10, 6))
plt.hist(tiempos, bins=25, density=True, color='lightblue', edgecolor='black', alpha=0.6, label='Datos simulados') #Crea un histograma que se normaliza (para representar densidad).
plt.plot(x, densidad, color='red', linewidth=2, label='Curva de densidad normal') #Dibuja la curva teórica de la distribución.

plt.title("Distribución de tiempos de atención (Variable Aleatoria Continua)")
plt.xlabel("Tiempo (minutos)")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
