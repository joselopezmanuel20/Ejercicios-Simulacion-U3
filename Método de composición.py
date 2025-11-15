# Problema:
# Simular el tiempo de entrega de paquetes (en días)
# que puede venir de dos modos de transporte:
# 70% por camión -> Exponencial(λ1 = 1/2)
# 30% por avión  -> Exponencial(λ2 = 1/1)




import numpy as np # números aleatorios 
import matplotlib.pyplot as plt  #y graficar.

# Probabilidades de cada componente
p_camion = 0.7
p_avion = 0.3

# Parámetros lambda de cada distribución
lambda_camion = 1 / 2  # media = 2 días
lambda_avion = 1 / 1   # media = 1 día

# Cantidad de muestras
n = 10000

# Paso 1: Generar números uniformes para decidir el tipo de envío
U = np.random.rand(n)

# Inicializar vector de resultados
T = np.zeros(n)

# Paso 2: Aplicar el método de composición
#Si el número aleatorio está dentro del 70% → generamos un tiempo con la distribución exponencial del camión.
#Si no → generamos con la distribución del avión.
#Cada caso usa la transformada inversa para obtener el valor.

for i in range(n):
    if U[i] < p_camion:
        # Envío por camión (Exponencial con media 2)
        T[i] = - (1 / lambda_camion) * np.log(1 - np.random.rand())
    else:
        # Envío por avión (Exponencial con media 1)
        T[i] = - (1 / lambda_avion) * np.log(1 - np.random.rand())

# Paso 3: Visualizar los resultados
plt.figure(figsize=(8,5))
plt.hist(T, bins=40, density=True, alpha=0.7, color='lightgreen', label='Simulación (composición)')
plt.title('Método de Composición\nDistribución mixta de tiempos de entrega')
plt.xlabel('Tiempo de entrega (días)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
