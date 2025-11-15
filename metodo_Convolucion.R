# Limpia el entorno
rm(list = ls())

# Parámetros de la distribución Erlang
lambda <- 0.5   # tasa de cada trámite
k <- 3          # número de trámites consecutivos

# Simulación por convolución: suma de k variables exponenciales
set.seed(1010)
n <- 1000  # número de simulaciones

# Generar matriz de valores exponenciales
exp_matrix <- matrix(rexp(n * k, rate = lambda), nrow = n, ncol = k)

# Sumar por fila para obtener tiempos totales
tiempos_totales <- rowSums(exp_matrix)

# Mostrar primeras simulaciones
head(tiempos_totales, 20)

# Estadísticos descriptivos
media_simulada <- mean(tiempos_totales)
media_teorica <- k / lambda
cat("Media simulada:", media_simulada, "\n")
cat("Media teórica:", media_teorica, "\n")

# Histograma con densidad teórica
hist(tiempos_totales,
     breaks = 30,
     probability = TRUE,
     main = paste("Distribución Erlang simulada (k =", k, ", λ =", lambda, ")"),
     xlab = "Tiempo total de atención",
     col = "orange",
     border = "white")

curve(dgamma(x, shape = k, rate = lambda),
      col = "blue",
      lwd = 2,
      add = TRUE)
