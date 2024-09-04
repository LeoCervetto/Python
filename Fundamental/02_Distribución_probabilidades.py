import numpy as np
import matplotlib.pyplot as plt

#%% Distribución Normal

# Calcular el percentil 75 con media 100 y desviación estándar 15
percentil_normal = np.percentile(np.random.normal(100, 15, 1000), 75)

print(f"Percentil 75 (Normal): {percentil_normal:.2f}")

# Números aleatorios 
random_normal = np.random.normal(100, 15, 1000)

# Gráfico 
plt.hist(random_normal, bins=30, color='blue', alpha=0.7)
plt.title("Distribución Normal")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()



#%% Distribución de Poisson 

# Calcular la probabilidad de 3 eventos cuando la media (lambda) es 2
prob_poisson = np.random.poisson(lam=2, size=1000).tolist().count(3) / 1000
prob_poisson

# Números aleatorios
random_poisson = np.random.poisson(lam=2, size=1000)

# Gráfico
plt.hist(random_poisson, bins=8, color='blue', alpha=0.7)
plt.title("Distribución de Poisson")
plt.xlabel("Número de eventos")
plt.ylabel("Frecuencia")
plt.show()



#%% Distribución Exponencial 

# Calcular la probabilidad acumulada de un valor < 2 con lambda = 1
prob_exponencial = np.mean(np.random.exponential(scale=1, size=1000) < 2)
prob_exponencial

# Números aleatorios
random_exponencial = np.random.exponential(scale=1, size=1000)

# Gráfico
plt.hist(random_exponencial, bins=30, color='blue', alpha=0.7)
plt.title("Distribución Exponencial")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()



#%% Distribución Hipergeométrica 

# Números aleatorios 
random_hipergeometrica = np.random.hypergeometric(ngood=50, nbad=150, nsample=12, size=1000)

# Calcular la probabilidad de 7 éxitos en una muestra de tamaño 12
prob_hipergeometrica = np.sum(random_hipergeometrica == 7) / 1000

# Gráfico 
plt.hist(random_hipergeometrica, bins=7, color='blue', alpha=0.7)
plt.title("Distribución Hipergeométrica")
plt.xlabel("Número de éxitos")
plt.ylabel("Frecuencia")
plt.show()



#%% Distribución Uniforme

# Calcular la probabilidad acumulada de un valor < 0.5
prob_uniforme = np.mean(np.random.uniform(0, 1, 1000) < 0.5)


# Números aleatorios de una distribución uniforme entre 0 y 1
random_uniforme = np.random.uniform(0, 1, 1000)

# Gráfico
plt.hist(random_uniforme, bins=30, color='blue', alpha=0.7)
plt.title("Distribución Uniforme")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

