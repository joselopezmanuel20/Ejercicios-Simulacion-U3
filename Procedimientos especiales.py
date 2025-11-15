


import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
p_camion = 0.7
p_avion = 0.3
lambda_camion = 1 / 2  # 0.5
lambda_avion = 1 / 1   # 1.0

# Queremos estimar P(T > threshold)
threshold = 5.0

# Tamaño de muestra base (usa un número par si quieres antitéticos)
N = 20000

# Funciones auxiliares
def sample_mixture(n):
    """Genera n muestras de la mezcla usando transformada inversa."""
    U = np.random.rand(n)
    X = np.zeros(n)
    # para cada muestra, decidir componente y generar exponencial
    # si U[i] < p_camion -> camión, else avión
    mask_camion = U < p_camion
    m1 = np.sum(mask_camion)
    m2 = n - m1
    # para camión
    X[mask_camion] = - (1 / lambda_camion) * np.log(1 - np.random.rand(m1))
    # para avión
    X[~mask_camion] = - (1 / lambda_avion) * np.log(1 - np.random.rand(m2))
    return X

def mixture_pdf(x):
    """Densidad de la mezcla en x (x puede ser array)."""
    x = np.asarray(x)
    pdf = p_camion * lambda_camion * np.exp(-lambda_camion * x) + \
          p_avion * lambda_avion * np.exp(-lambda_avion * x)
    return pdf

# 1) Crude Monte Carlo
T = sample_mixture(N)
I = (T > threshold).astype(float)
est_crude = I.mean()
var_crude = I.var(ddof=1) / N  # var del estimador (var muestral / N)

# 2) Antithetic variates
#    -> generamos N/2 pares (U1,U2) y (1-U1,1-U2)
def sample_mixture_antithetic(N):
    assert N % 2 == 0, "N must be even for antithetic pairing"
    half = N // 2
    # generar uniformes U1 (decisión de componente) y U2 (transformada)
    U1 = np.random.rand(half)
    U2 = np.random.rand(half)
    # pares antitéticos
    U1_a = 1 - U1
    U2_a = 1 - U2

    def build_from(U1s, U2s):
        X = np.zeros(len(U1s))
        mask_cam = U1s < p_camion
        # para cada, use U2s para la transformada inversa, pero si no queremos 0 log, usar 1-U2s
        # Usamos formula X = - (1/lambda) * ln(1 - V) con V = U2s
        m1 = np.sum(mask_cam)
        m2 = len(U1s) - m1
        X[mask_cam] = - (1 / lambda_camion) * np.log(1 - U2s[mask_cam])
        X[~mask_cam] = - (1 / lambda_avion) * np.log(1 - U2s[~mask_cam])
        return X

    X1 = build_from(U1, U2)
    X2 = build_from(U1_a, U2_a)
    X = np.concatenate((X1, X2))
    return X

T_ant = sample_mixture_antithetic(N)
I_ant = (T_ant > threshold).astype(float)
est_ant = I_ant.mean()
var_ant = I_ant.var(ddof=1) / N

# 3) Importance Sampling
#    Propuesta g(t) = Exp(lambda_prop) (más pesada en cola)
#    Peso w = f(t) / g(t)
lambda_prop = 0.3  # propuesta con media ~ 3.33 para muestrear más cola
# generar de la propuesta
V = np.random.exponential(1 / lambda_prop, size=N)  # numpy usa scale = 1/lambda
# calcular pesos = f(t)/g(t)
fV = mixture_pdf(V)
gV = lambda_prop * np.exp(-lambda_prop * V)
weights = fV / gV
# estimador IS: media ponderada de I(V>threshold) * w
I_V = (V > threshold).astype(float)
est_is = np.sum(I_V * weights) / N
# var (aprox) del estimador: var_g( I*w ) / N  -> usamos var muestral de I*w
var_is = np.var(I_V * weights, ddof=1) / N

# 4) Control Variates
#    Usamos h(T)=T (media teórica conocida)
#    E[h] = p_camion*2 + p_avion*1 = 1.7
#    Ajuste: I_adj = I - c*(h - E[h])  ; c estimado por mínimos cuadrados
h_mean = p_camion * (1 / lambda_camion) + p_avion * (1 / lambda_avion)  # 1.7
h_vals = T  # usamos T como control
# estimador del coeficiente c* = Cov(I,h)/Var(h) -> pero la forma óptima para reducir var de I is -Cov(I,h)/Var(h) si añadimos -c(h - E)
# Usaremos c = Cov(I,h)/Var(h) y restamos c*(h - E)
cov_Ih = np.cov(I, h_vals, ddof=1)[0,1]
var_h = np.var(h_vals, ddof=1)
c = cov_Ih / var_h
I_cv = I - c * (h_vals - h_mean)
est_cv = I_cv.mean()
var_cv = I_cv.var(ddof=1) / N

# Resultados
print("Estimadores para P(T > {:.1f}) con N = {}".format(threshold, N))
print(f"Crude MC: est = {est_crude:.6f}, var(est) ≈ {var_crude:.6e}")
print(f"Antithetic: est = {est_ant:.6f}, var(est) ≈ {var_ant:.6e}")
print(f"Importance Sampling: est = {est_is:.6f}, var(est) ≈ {var_is:.6e}")
print(f"Control Variates: est = {est_cv:.6f}, var(est) ≈ {var_cv:.6e}")
print()
print("Medias/aux:")
print(f"Media teorica de T (control) = {h_mean:.4f}, coef c usado = {c:.4f}")

# Visualización (opcional)
plt.figure(figsize=(8,4))
plt.bar(['Crude','Antithetic','IS','ControlVar'],
        [est_crude, est_ant, est_is, est_cv],
        yerr=[np.sqrt(var_crude), np.sqrt(var_ant), np.sqrt(var_is), np.sqrt(var_cv)],
        capsize=6)
plt.ylabel("Estimador P(T > {:.1f})".format(threshold))
plt.title("Comparación de estimadores y errores estándar")
plt.grid(axis='y', alpha=0.3)
plt.show()
