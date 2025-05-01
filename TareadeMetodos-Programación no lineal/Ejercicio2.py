"""
Ejercicio 2 – Métodos Cuantitativos: Programación No Lineal

PROBLEMA:
Una compañía desea producir tres productos A (x), B (y) y C (z), minimizando los costos de producción con un presupuesto total fijo.

Función de costos a minimizar:
    C(x, y, z) = 5x² + 3y² + z²

Restricción:
    x + y + z = 100 (presupuesto de producción)

FORMULACIÓN:
    Usamos optimización con restricción de igualdad y cotas positivas.
    Este es un caso clásico de programación no lineal con una restricción lineal.

Solución:
    Se utilizará `scipy.optimize.minimize` con método SLSQP y se graficará el punto óptimo encontrado.
"""

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Función objetivo (costos)
def costos(x):
    return 5 * x[0]**2 + 3 * x[1]**2 + x[2]**2

# Restricción: suma total del presupuesto
restriccion_presupuesto = {'type': 'eq', 'fun': lambda x: x[0] + x[1] + x[2] - 100}

# Cotas: no puede producir cantidades negativas
limites = [(0, 100), (0, 100), (0, 100)]

# Punto inicial razonable
punto_inicial = [30, 30, 40]

# Ejecutar optimización
resultado = minimize(costos, punto_inicial, method='SLSQP', bounds=limites, constraints=[restriccion_presupuesto])

# Mostrar resultados
if resultado.success:
    x_opt, y_opt, z_opt = resultado.x
    costo_total = costos([x_opt, y_opt, z_opt])
    print(" Solución encontrada:")
    print(f"  Producción óptima de A (x): {x_opt:.2f}")
    print(f"  Producción óptima de B (y): {y_opt:.2f}")
    print(f"  Producción óptima de C (z): {z_opt:.2f}")
    print(f"  Costo mínimo: {costo_total:.2f}")

    # Graficar los resultados
    etiquetas = ['Producto A (x)', 'Producto B (y)', 'Producto C (z)']
    valores = [x_opt, y_opt, z_opt]

    plt.figure(figsize=(8,5))
    plt.bar(etiquetas, valores, color=['skyblue', 'orange', 'green'])
    plt.title('Distribución óptima de producción (Presupuesto: 100)')
    plt.ylabel('Unidades a producir')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

else:
    print(" No se pudo encontrar una solución válida.")
