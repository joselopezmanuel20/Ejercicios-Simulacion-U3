# Limpia el entorno
rm(list = ls())

# Parámetros
set.seed(2025)
n <- 1000  # número de simulaciones
p_joven <- 0.6
p_adulto <- 0.4

# Paso 1: Generar tipo de usuario (0 = joven, 1 = adulto mayor)
tipo_usuario <- rbinom(n, size = 1, prob = p_adulto)

# Paso 2: Generar tiempos según tipo
tiempos <- numeric(n)
for (i in 1:n) {
  if (tipo_usuario[i] == 0) {
    tiempos[i] <- rexp(1, rate = 1/2)  # joven: media 2 min
  } else {
    tiempos[i] <- rexp(1, rate = 1/5)  # adulto mayor: media 5 min
  }
}

# Mostrar primeras simulaciones
head(tiempos, 20)

# Estadísticos descriptivos
cat("Media simulada:", mean(tiempos), "\n")

# Histograma
hist(tiempos,
     breaks = 30,
     probability = TRUE,
     main = "Tiempo de atención por tipo de usuario (composición)",
     xlab = "Minutos",
     col = "purple",
     border = "white")

