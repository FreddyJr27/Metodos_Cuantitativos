"""
Ejercicio 4 – Métodos Cuantitativos: Programación No Lineal

PROBLEMA:
Minimizar la función:
    f(x) = x² + 4x + 5

Sujeta a las siguientes restricciones:
    g1(x) = x - 2 ≥ 0  →   x ≥ 2
    g2(x) = 5 - x ≥ 0  →   x ≤ 5

Este es un problema simple de optimización no lineal con una variable
y restricciones de tipo "box constraint" o intervalo.

Se usará scipy.optimize para encontrar el mínimo en el intervalo [2, 5].
"""

import numpy as np
from scipy.optimize import minimize_scalar

# Definir la función objetivo
def f(x):
    return x**2 + 4*x + 5

# Usamos minimize_scalar con restricciones en el intervalo [2, 5]
resultado = minimize_scalar(f, bounds=(2, 5), method='bounded')

# Mostrar resultados
if resultado.success:
    x_opt = resultado.x
    f_opt = resultado.fun
    print(" Mínimo encontrado en el intervalo [2, 5]:")
    print(f"  x = {x_opt:.4f}")
    print(f"  f(x) = {f_opt:.4f}")
else:
    print(" No se pudo encontrar un mínimo válido en el intervalo.")
