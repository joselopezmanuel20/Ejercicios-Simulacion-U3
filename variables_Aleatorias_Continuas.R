# Limpia el entorno
rm(list = ls())

# Simulación de una variable aleatoria continua: Distribución Normal
set.seed(456)  # Semilla para reproducibilidad
muestras <- rnorm(n = 1000, mean = 50, sd = 10)

# Mostrar las primeras 20 simulaciones
head(muestras, 20)

# Estadísticos descriptivos
media <- mean(muestras)
desv <- sd(muestras)
cat("Media simulada:", media, "\n")
cat("Desviación estándar simulada:", desv, "\n")

# Histograma con curva de densidad
hist(muestras,
     breaks = 30,
     probability = TRUE,
     main = "Distribución Normal simulada (media=50, sd=10)",
     xlab = "Valores",
     col = "lightgreen",
     border = "white")

# Añadir curva de densidad teórica
curve(dnorm(x, mean = 50, sd = 10),
      col = "red",
      lwd = 2,
      add = TRUE)