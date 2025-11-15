# Limpia el entorno
rm(list = ls())

# Parámetro de la distribución exponencial
lambda <- 0.5   # tasa (ej: 0.5 llegadas por minuto)

# Generar 1000 valores usando la transformada inversa
set.seed(789)
U <- runif(1000)  # 1000 valores uniformes (0,1)
X <- - (1/lambda) * log(1 - U)

# Mostrar primeras simulaciones
head(X, 20)

# Estadísticos descriptivos
media <- mean(X)
teorica <- 1/lambda
cat("Media simulada:", media, "\n")
cat("Media teórica:", teorica, "\n")

# Histograma con densidad teórica
hist(X,
     breaks = 30,
     probability = TRUE,
     main = "Distribución Exponencial simulada (λ=0.5)",
     xlab = "Tiempo de espera",
     col = "lightblue",
     border = "white")

curve(dexp(x, rate = lambda),
      col = "red",
      lwd = 2,
      add = TRUE)
