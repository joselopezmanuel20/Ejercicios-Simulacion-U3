# Limpia el entorno
rm(list = ls())

# Parámetro de la distribución exponencial
lambda <- 0.5

# Generar muestra simulada (como en el Ejercicio 3)
set.seed(4040)
n <- 1000
U <- runif(n)
X <- - (1/lambda) * log(1 - U)  # Transformada inversa

# Prueba de Kolmogorov-Smirnov
ks_result <- ks.test(X, "pexp", rate = lambda)

print(ks_result)
