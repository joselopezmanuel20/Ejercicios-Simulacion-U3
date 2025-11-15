# Simulación de una variable aleatoria discreta: Distribución Binomial
# Parámetros: n = 10 ensayos, p = 0.5 probabilidad de éxito
set.seed(123)  # Semilla para reproducibilidad
muestras <- rbinom(n = 1000, size = 10, prob = 0.5)

# Mostrar las primeras 20 simulaciones
head(muestras, 20)

# Tabla de frecuencias
tabla <- table(muestras)
print(tabla)

# Visualización del histograma
barplot(tabla / sum(tabla),
        main = "Distribución Binomial (n=10, p=0.5)",
        xlab = "Número de éxitos",
        ylab = "Frecuencia relativa",
        col = "skyblue")

