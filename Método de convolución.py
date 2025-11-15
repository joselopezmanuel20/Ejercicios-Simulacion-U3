# Problema:
# Simular el tiempo total de atención al cliente (minutos)
# compuesto por dos etapas independientes, cada una con
# distribución exponencial (media = 10 min)


import numpy as np # números aleatorios 
import matplotlib.pyplot as plt #y graficar.

# Parámetro lambda (1/media)
lambd = 1 / 10

# Cantidad de muestras
n = 10000

# Paso 1: Generar dos variables exponenciales independientes
X1 = - (1 / lambd) * np.log(1 - np.random.rand(n))
X2 = - (1 / lambd) * np.log(1 - np.random.rand(n))

# Paso 2: Aplicar convolución (suma)
T = X1 + X2  # Tiempo total

# Paso 3: Visualizar los resultados
plt.figure(figsize=(8,5))
plt.hist(T, bins=40, density=True, alpha=0.7, color='orange', label='Simulación (convolución)')
plt.title('Método de Convolución\nSuma de dos variables exponenciales (Gamma(2, λ))')
plt.xlabel('Tiempo total (minutos)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
