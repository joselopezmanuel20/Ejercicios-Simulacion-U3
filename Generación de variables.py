# Ejercicio: Generación de Variables Aleatorias
# Este programa genera variables aleatorias de distintos tipos
# (Uniforme, Normal y Exponencial) y muestra sus histogramas.
#Se usa numpy para generar los números aleatorios y matplotlib para graficar.
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 1️⃣ Configuración inicial
# -----------------------------
n = 1000  # cantidad de números aleatorios a generar

# -----------------------------
# 2️⃣ Generar variables aleatorias
# -----------------------------
# Distribución Uniforme (entre 0 y 1)
uniforme = np.random.uniform(0, 1, n)

# Distribución Normal (media = 0, desviación = 1)
normal = np.random.normal(0, 1, n)

# Distribución Exponencial (lambda = 1)
exponencial = np.random.exponential(1, n)

# -----------------------------
# 3️⃣ Mostrar resultados
# -----------------------------
print("Ejemplo de variables generadas:")
print(f"Uniforme: {uniforme[:5]}")
print(f"Normal: {normal[:5]}")
print(f"Exponencial: {exponencial[:5]}")

# -----------------------------
# 4️⃣ Graficar las distribuciones
# -----------------------------
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.hist(uniforme, bins=20, color='skyblue', edgecolor='black')
plt.title("Distribución Uniforme (0,1)")

plt.subplot(1, 3, 2)
plt.hist(normal, bins=20, color='lightgreen', edgecolor='black')
plt.title("Distribución Normal (μ=0, σ=1)")

plt.subplot(1, 3, 3)
plt.hist(exponencial, bins=20, color='salmon', edgecolor='black')
plt.title("Distribución Exponencial (λ=1)")

plt.tight_layout()
plt.show()
