"""
Ejercicio 3 – Métodos Cuantitativos: Programación No Lineal

PROBLEMA:
Minimizar la función:
    f(x, y, z) = x² + y² + z² - 2xy + 3z

Se requiere:
a) Calcular el gradiente ∇f(x, y, z)
b) Implementar el algoritmo de descenso del gradiente desde el punto (1, 1, 1)
   con un paso de aprendizaje α = 0.1
c) Realizar 15 iteraciones y graficar la evolución del valor de f

SOLUCIÓN:

1. Cálculo del gradiente:
   ∂f/∂x = 2x - 2y
   ∂f/∂y = 2y - 2x
   ∂f/∂z = 2z + 3
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir la función objetivo
def f(x, y, z):
    return x**2 + y**2 + z**2 - 2*x*y + 3*z

# Gradiente ∇f(x, y, z)
def gradiente(x, y, z):
    df_dx = 2*x - 2*y
    df_dy = 2*y - 2*x
    df_dz = 2*z + 3
    return np.array([df_dx, df_dy, df_dz])

# Parámetros de descenso del gradiente
alpha = 0.1
iteraciones = 15
punto = np.array([1.0, 1.0, 1.0])  # punto inicial

# Guardamos la evolución de f en cada iteración
historial_f = [f(*punto)]

print("Iteraciones del descenso del gradiente:")
print(f"Iteración 0: x = {punto[0]:.4f}, y = {punto[1]:.4f}, z = {punto[2]:.4f}, f = {historial_f[0]:.4f}")

for i in range(1, iteraciones + 1):
    grad = gradiente(*punto)
    punto = punto - alpha * grad  # actualización
    valor_f = f(*punto)
    historial_f.append(valor_f)
    print(f"Iteración {i}: x = {punto[0]:.4f}, y = {punto[1]:.4f}, z = {punto[2]:.4f}, f = {valor_f:.4f}")

# Gráfica de evolución de la función f
plt.figure(figsize=(8, 5))
plt.plot(range(iteraciones + 1), historial_f, marker='o', color='purple')
plt.title("Evolución del valor de f(x, y, z) con descenso del gradiente")
plt.xlabel("Iteración")
plt.ylabel("f(x, y, z)")
plt.grid(True)
plt.show()
