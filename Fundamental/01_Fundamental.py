# Script Básico de Python para Operaciones y Visualización
# Autor: Lcervetto
# Descripción: Este script cubre operaciones básicas, manejo de variables, tipos de datos, 
#              estadística descriptiva y visualización en Python.

#%% Importar librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt






#%% Uso como calculadora

# Suma
4 + 8

# Resta
7 - 3

# Multiplicación
6 * 7

# División
20 / 5

# Exponencial
3 ** 3

# Operación combinada
(3 + 9) / (2 * 2)


#%% Asignar variables

mi_variable = 50

# Impresión explicita
print(mi_variable)

# Impresión implícita
mi_variable

# Operación entre variables
x = 40
y = 10

x + y

# Ver y eliminar variables
print(list(locals().keys()))
del mi_variable


#%% Estructura para almacenar datos

# Conjunto unidimensional 
conjunto_1 = [20, 26, 32, 40, 50]
conjunto_2 = list(range(2, 24, 2))
conjunto_3 = np.array(range(1, 10))

# Conjunto multidimensional
conjunto_4 = np.reshape(np.arange(1, 13), (4, 3))
conjunto_5 = pd.DataFrame({
    "col1": np.arange(1, 13),
    "col2": np.full(12, 5 * 2),
    "col3": np.full(12, 3)
})


#%% Estadística descriptiva 

# Ejemplo
ventas = np.array([100, 95, 103, 105, 112])
costos = np.array([90, 80, 97, 93, 100])

Control_diario = pd.DataFrame({"ventas": ventas, 
                               "costos": costos})

# Añadir columna de utilidad
Control_diario["utilidad"] = Control_diario["ventas"] - Control_diario["costos"]

# Cálculos básicos
sum(Control_diario["ventas"])
np.sum(ventas)

np.mean(ventas)
np.max(ventas)
np.min(ventas)
len(ventas)
np.std(ventas)
np.var(ventas)
np.percentile(ventas, 75)
Control_diario["ventas"].describe()

# Selecionar 3er cuartil
Control_diario["ventas"].describe()[6]


#%% Gráficos 

# Barplot
plt.bar(range(len(ventas)), ventas)
plt.title("Ventas Diarias")
plt.xlabel("Día")
plt.ylabel("Ventas")
plt.show()

# Boxplot
plt.boxplot(ventas)
plt.title("Distribución de Ventas")
plt.show()

# Histograma
plt.hist(ventas, bins = 5, color='lightblue')
plt.title("Histograma de Ventas")
plt.xlabel("Ventas")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de Puntos
plt.plot(ventas, 'o')
plt.title("Ventas Diarias")
plt.xlabel("Día")
plt.ylabel("Ventas")
plt.show()

# Scatter
plt.scatter(costos, ventas, color='blue', marker='o')
plt.title("Relación entre Costos y Ventas")
plt.xlabel("Costos")
plt.ylabel("Ventas")
plt.show()


# Línea
plt.plot(ventas, linestyle = '-', marker = 'o', linewidth = 2)
plt.title("Ventas en el Tiempo")
plt.xlabel("Día")
plt.ylabel("Ventas")
plt.show()

#
plt.plot(ventas, costos, linestyle = '--')
plt.title("Ventas contra costos")
plt.xlabel("Costo")
plt.ylabel("Ventas")
plt.show()

