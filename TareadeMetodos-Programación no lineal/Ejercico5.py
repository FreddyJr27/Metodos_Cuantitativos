"""
Ejercicio 5 – Métodos Cuantitativos: Programación No Lineal

TEMA: PUNTOS ESTACIONARIOS

 DEFINICIÓN:
Un punto estacionario de una función f(x) es un punto x₀ donde la derivada primera se anula:
    f'(x₀) = 0

Los puntos estacionarios pueden clasificarse como:
1.  Mínimo local: si f''(x₀) > 0 (la curva es cóncava hacia arriba)
2.  Máximo local: si f''(x₀) < 0 (la curva es cóncava hacia abajo)
3.  Punto de inflexión: si f''(x₀) = 0, pero no cambia el crecimiento/ decrecimiento (no es ni mínimo ni máximo)

 MÉTODO:
Para identificar el tipo de punto estacionario:
- Se deriva la función f'(x)
- Se iguala a 0 para encontrar candidatos
- Se evalúa la derivada segunda f''(x) para clasificar el tipo

Ejemplo:
Explicado abajo con gráficos.

"""

import numpy as np
import matplotlib.pyplot as plt

# Crear un rango de valores de x para graficar
x = np.linspace(-4, 4, 400)

# 🎯 Ejemplo 1: MÍNIMO LOCAL
# f(x) = x^2 → mínimo en x = 0
f1 = x**2

# 🎯 Ejemplo 2: MÁXIMO LOCAL
# f(x) = -x^2 → máximo en x = 0
f2 = -x**2

# 🎯 Ejemplo 3: PUNTO DE INFLEXIÓN
# f(x) = x^3 → inflexión en x = 0
f3 = x**3

# Crear subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# Gráfico 1: mínimo
axs[0].plot(x, f1, label="f(x) = x²", color="green")
axs[0].scatter(0, 0, color='red')
axs[0].set_title("Mínimo Local (x = 0)")
axs[0].grid(True)
axs[0].legend()

# Gráfico 2: máximo
axs[1].plot(x, f2, label="f(x) = -x²", color="blue")
axs[1].scatter(0, 0, color='red')
axs[1].set_title("Máximo Local (x = 0)")
axs[1].grid(True)
axs[1].legend()

# Gráfico 3: punto de inflexión
axs[2].plot(x, f3, label="f(x) = x³", color="purple")
axs[2].scatter(0, 0, color='red')
axs[2].set_title("Punto de Inflexión (x = 0)")
axs[2].grid(True)
axs[2].legend()

plt.suptitle("Ejemplos de Puntos Estacionarios")
plt.tight_layout()
plt.show()
