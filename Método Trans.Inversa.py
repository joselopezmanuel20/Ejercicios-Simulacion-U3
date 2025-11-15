
# Problema: Generar tiempos de llegada de un autobús (minutos)
# que siguen una distribución exponencial con media = 10 min

#numpy para cálculos numéricos y aleatorios.
#matplotlib para graficar los resultados.

import numpy as np
import matplotlib.pyplot as plt

# Parámetro lambda de la distribución exponencial
# λ = 1 / media
lambd = 1 / 10  

# Cantidad de valores a generar
n = 10000

# Paso 1: Generar números aleatorios uniformes U(0,1)
U = np.random.rand(n)

# Paso 2: Aplicar la transformada inversa
X = - (1 / lambd) * np.log(1 - U)

# Paso 3: Visualizar los resultados
plt.figure(figsize=(8,5))
plt.hist(X, bins=40, density=True, alpha=0.7, color='skyblue', label='Datos simulados')
plt.title('Generación de variables aleatorias exponenciales \nMétodo de la transformada inversa')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
