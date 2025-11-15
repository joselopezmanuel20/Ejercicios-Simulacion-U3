# Limpia el entorno
rm(list = ls())

# Parámetros de la distribución triangular
a <- 2   # mínimo
b <- 10  # máximo
c <- 4   # modo

# Función de densidad triangular
f_triangular <- function(x, a, b, c) {
  if (x < a || x > b) return(0)
  if (x <= c) return(2 * (x - a) / ((b - a) * (c - a)))
  else return(2 * (b - x) / ((b - a) * (b - c)))
}

# Simulación por aceptación-rechazo
set.seed(3030)
n <- 1000
resultados <- numeric(0)

while (length(resultados) < n) {
  x <- runif(1, min = a, max = b)
  u <- runif(1)
  fx <- f_triangular(x, a, b, c)
  if (u <= fx) {
    resultados <- c(resultados, x)
  }
}

# Mostrar primeras simulaciones
head(resultados, 20)

# Histograma
hist(resultados,
     breaks = 30,
     probability = TRUE,
     main = "Distribución Triangular simulada (a=2, b=10, c=4)",
     xlab = "Minutos",
     col = "salmon",
     border = "white")
