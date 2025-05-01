"""
Ejercicio 1 – Métodos Cuantitativos: Programación No Lineal

PROBLEMA:
Un inversor desea maximizar sus rendimientos invirtiendo en dos activos x e y, con restricciones de presupuesto y riesgo.

Función objetivo (rendimiento):
    f(x, y) = 0.1 * x + 0.08 * y

Restricciones:
    Presupuesto: x + y = 1
    Riesgo limitado: 0.02 * x^2 + 0.03 * y^2 <= 0.05

FORMULACIÓN DE LAGRANGE (con múltiples restricciones):

    L(x, y, λ, μ) = 0.1*x + 0.08*y 
                    - λ*(x + y - 1) 
                    - μ*(0.02*x^2 + 0.03*y^2 - 0.05)

Donde:
    λ: multiplicador de Lagrange para la restricción de presupuesto (igualdad)
    μ: multiplicador para la restricción de riesgo (desigualdad)

Para encontrar extremos, se deben resolver las ecuaciones obtenidas al derivar L respecto a x, y, λ, μ y resolver el sistema:
    ∂L/∂x = 0
    ∂L/∂y = 0
    ∂L/∂λ = 0
    ∂L/∂μ = 0
Sin embargo, en este caso implementaremos la solución usando una librería de optimización numérica.
"""

import numpy as np
from scipy.optimize import minimize

# Función objetivo (rendimiento). Se pone negativa porque minimize() minimiza por defecto.
def objetivo(x):
    return -(0.1 * x[0] + 0.08 * x[1])  # Negamos para maximizar

# Restricción 1: presupuesto (x + y = 1)
restriccion_presupuesto = {'type': 'eq', 'fun': lambda x: x[0] + x[1] - 1}

# Restricción 2: riesgo limitado (0.02 * x^2 + 0.03 * y^2 <= 0.05)
restriccion_riesgo = {'type': 'ineq', 'fun': lambda x: 0.05 - (0.02 * x[0]**2 + 0.03 * x[1]**2)}

# Conjunto de restricciones
restricciones = [restriccion_presupuesto, restriccion_riesgo]

# Cotas para las variables: no se puede invertir cantidades negativas
limites = [(0, 1), (0, 1)]

# Punto inicial
punto_inicial = [0.5, 0.5]

# Función auxiliar para validar la solución
def es_valida(solucion):
    x, y = solucion
    return (0 <= x <= 1) and (0 <= y <= 1) and abs(x + y - 1) < 1e-5 and (0.02*x**2 + 0.03*y**2 <= 0.05)

# Ejecutar optimización
resultado = minimize(objetivo, punto_inicial, method='SLSQP', bounds=limites, constraints=restricciones)

# Mostrar resultados
if resultado.success and es_valida(resultado.x):
    x_opt, y_opt = resultado.x
    print(" Solución encontrada:")
    print(f"  Inversión en activo x: {x_opt:.4f}")
    print(f"  Inversión en activo y: {y_opt:.4f}")
    print(f"  Rendimiento máximo: {-resultado.fun:.4f}")
else:
    print(" No se pudo encontrar una solución válida.")
