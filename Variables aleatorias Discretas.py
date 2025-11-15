# Ejercicio: Variables Aleatorias Discretas
# Descripción:Un casino desea simular el lanzamiento de un dado justo (de seis caras) y de un dado cargado 
# (no todas las caras tienen la misma probabilidad).
# Genere una variable aleatoria discreta que represente los posibles resultados de un dado.
#Calcule la frecuencia relativa de cada número (1 al 6) después de varios lanzamientos.
#Compare el comportamiento entre un dado justo y un dado cargado.


#Se usan numpy (para generar datos aleatorios) y matplotlib (para graficar).
import numpy as np
import matplotlib.pyplot as plt

n = 10000  # número de lanzamientos

# 2️⃣ Dado justo (todas las caras tienen la misma probabilidad)
caras = np.array([1, 2, 3, 4, 5, 6])
prob_justo = np.ones(6) / 6  # todas las caras con 1/6
dados_justo = np.random.choice(caras, size=n, p=prob_justo) #np.random.choice() Permite elegir valores de un conjunto con ciertas probabilidades.

# 3️⃣ Dado cargado (caras con diferente probabilidad)
# Probabilidades: la cara 6 tiene más probabilidad
prob_cargado = np.array([0.05, 0.1, 0.15, 0.2, 0.2, 0.3])
dados_cargado = np.random.choice(caras, size=n, p=prob_cargado)

# 4️⃣ Calcular frecuencias relativas
valores, frec_justo = np.unique(dados_justo, return_counts=True) #Cuenta cuántas veces apareció cada cara.
frec_justo = frec_justo / n

valores, frec_cargado = np.unique(dados_cargado, return_counts=True)
frec_cargado = frec_cargado / n

# 5️⃣ Mostrar resultados en consola
print("Resultados - Dado Justo:")
for v, f in zip(valores, frec_justo):
    print(f"Caras {v}: Frecuencia relativa = {f:.3f}")

print("\nResultados - Dado Cargado:")
for v, f in zip(valores, frec_cargado):
    print(f"Caras {v}: Frecuencia relativa = {f:.3f}")

# 6️⃣ Graficar resultados
plt.figure(figsize=(10, 5))
x = np.arange(1, 7)

plt.bar(x - 0.15, frec_justo, width=0.3, label='Dado Justo', color='skyblue')
plt.bar(x + 0.15, frec_cargado, width=0.3, label='Dado Cargado', color='salmon')

plt.xticks(x)
plt.xlabel("Caras del Dado")
plt.ylabel("Frecuencia Relativa")
plt.title("Comparación: Dado Justo vs Dado Cargado")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
