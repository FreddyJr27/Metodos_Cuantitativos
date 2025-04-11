import math

class WorkforcePlanner:
    """
    Resuelve el problema de dimensionamiento de la fuerza laboral usando Programación Dinámica.
    """

    def __init__(self, requirements, excess_cost, fixed_hire_cost, var_hire_cost):
        """
        Inicializa el planificador.

        Args:
            requirements (list): Lista de requisitos de trabajadores por semana (b_t).
                                 El índice 0 corresponde a la semana 1, etc.
            excess_cost (float): Costo por trabajador excedente por semana.
            fixed_hire_cost (float): Costo fijo por realizar contrataciones en una semana.
            var_hire_cost (float): Costo variable por cada trabajador contratado por semana.
        """
        self.requirements = [0] + requirements # Agrega un dummy al inicio para indexar desde 1
        self.num_weeks = len(requirements)
        self.excess_cost = excess_cost
        self.fixed_hire_cost = fixed_hire_cost
        self.var_hire_cost = var_hire_cost

        # Determinar un límite superior razonable para el número de trabajadores
        self.max_workers = max(self.requirements) + 5 # Un margen por encima del máximo req.

        # Tablas de DP: f[t][x_t] = costo mínimo, w_star[t][x_t] = decisión óptima w_t
        self.f = [{} for _ in range(self.num_weeks + 2)] # +2 para f[T+1] y el dummy en req.
        self.w_star = [{} for _ in range(self.num_weeks + 1)]

        # Inicializar caso base f[T+1]
        for x in range(self.max_workers + 1):
             self.f[self.num_weeks + 1][x] = 0.0

        print("--- Inicialización ---")
        print(f"Requisitos (b_t): {self.requirements[1:]}")
        print(f"Semanas: {self.num_weeks}")
        print(f"Costo Exceso: {self.excess_cost}")
        print(f"Costo Fijo Contratación: {self.fixed_hire_cost}")
        print(f"Costo Variable Contratación: {self.var_hire_cost}")
        print(f"Máximo de trabajadores considerados: {self.max_workers}")
        print("-" * 20)


    def _calculate_cost(self, t, x_t, w_t):
        """Calcula el costo inmediato c_t(x_t, w_t) para la semana t."""
        if w_t < self.requirements[t]:
            return math.inf # No cumple el requisito

        cost_excess = self.excess_cost * max(0, w_t - self.requirements[t])

        cost_hiring = 0
        if w_t > x_t:
            cost_hiring = self.fixed_hire_cost + self.var_hire_cost * (w_t - x_t)

        return cost_excess + cost_hiring

    def solve(self, initial_workforce=0):
        """
        Ejecuta el algoritmo de Programación Dinámica (paso hacia atrás)
        y reconstruye la solución (paso hacia adelante).

        Args:
            initial_workforce (int): Número de trabajadores al inicio de la semana 1.
        """
        print("\n--- Calculando Costos Mínimos (Hacia Atrás) ---")

        # Paso hacia atrás: Calcular f_t(x_t) desde t = T hasta 1
        for t in range(self.num_weeks, 0, -1):
            print(f"\n=== Semana {t} (Requisito b_{t} = {self.requirements[t]}) ===")
            for x_t in range(self.max_workers + 1): # Estado: trabajadores al inicio de la semana t
                min_cost_for_xt = math.inf
                optimal_wt_for_xt = -1

                print(f"  Estado x_{t} = {x_t}:") # Trabajadores al inicio de la semana t

                # Decisión: Número de trabajadores w_t durante la semana t
                # Debe ser al menos el requisito b_t y no más del máximo considerado
                for w_t in range(self.requirements[t], self.max_workers + 1):
                    cost_immediate = self._calculate_cost(t, x_t, w_t)
                    cost_future = self.f[t + 1][w_t] # Costo futuro óptimo si terminamos semana t con w_t

                    if cost_immediate == math.inf or cost_future == math.inf:
                        total_cost = math.inf
                    else:
                        total_cost = cost_immediate + cost_future

                    print(f"    Decisión w_{t} = {w_t}:")
                    print(f"      Costo Semana {t} (c_{t}({x_t},{w_t})): {cost_immediate:.2f}")
                    print(f"      Costo Futuro Óptimo (f_{t+1}({w_t})): {cost_future:.2f}")
                    print(f"      Costo Total (c_{t} + f_{t+1}): {total_cost:.2f}")

                    if total_cost < min_cost_for_xt:
                        min_cost_for_xt = total_cost
                        optimal_wt_for_xt = w_t

                # Almacenar resultados para este estado x_t
                self.f[t][x_t] = min_cost_for_xt
                self.w_star[t][x_t] = optimal_wt_for_xt
                print(f"  -> Mínimo Costo para x_{t}={x_t}: f_{t}({x_t}) = {min_cost_for_xt:.2f}, Decisión Óptima w*_{t} = {optimal_wt_for_xt}")

        # Paso hacia adelante: Reconstruir la solución óptima
        print("\n--- Reconstruyendo Solución Óptima (Hacia Adelante) ---")
        optimal_plan = []
        current_x = initial_workforce
        total_min_cost = self.f[1][initial_workforce]

        print(f"Costo total mínimo iniciando con {initial_workforce} trabajadores: ${total_min_cost:.2f}")
        print("Plan Óptimo Semanal:")
        print("Semana | Inicio (x_t) | Decisión (w*_t) | Requisito (b_t) | Exceso | Contratados | Costo Semana")
        print("-" * 80)

        cumulative_cost_check = 0
        for t in range(1, self.num_weeks + 1):
            optimal_w_t = self.w_star[t][current_x]
            if optimal_w_t == -1:
                 print(f"Error: No se encontró solución óptima para x_{t}={current_x} en semana {t}")
                 break

            cost_t = self._calculate_cost(t, current_x, optimal_w_t)
            excess = max(0, optimal_w_t - self.requirements[t])
            hired = max(0, optimal_w_t - current_x)
            cumulative_cost_check += cost_t

            optimal_plan.append({
                'week': t,
                'start_workforce': current_x,
                'chosen_workforce': optimal_w_t,
                'requirement': self.requirements[t],
                'excess': excess,
                'hired': hired,
                'weekly_cost': cost_t
            })

            print(f"  {t:^4} | {current_x:^12} | {optimal_w_t:^14} | {self.requirements[t]:^15} | {excess:^6} | {hired:^11} | ${cost_t:^12.2f}")

            # El número de trabajadores al final de esta semana es la decisión w_t
            # que se convierte en el estado x_{t+1} para la siguiente semana
            current_x = optimal_w_t

        print("-" * 80)
        print(f"Suma de costos semanales (verificación): ${cumulative_cost_check:.2f}")


        return total_min_cost, optimal_plan

# --- Datos del Problema ---
requisitos_semanales = [5, 7, 8, 4, 6] # b1, b2, b3, b4, b5
costo_exceso = 300
costo_fijo_contratar = 400
costo_variable_contratar = 200

# --- Crear instancia y resolver ---
planner = WorkforcePlanner(requisitos_semanales, costo_exceso, costo_fijo_contratar, costo_variable_contratar)
min_costo_total, plan_optimo = planner.solve(initial_workforce=0)

# --- Mostrar Resultados Finales ---
print("\n--- Resultados Finales ---")
print(f"El costo total mínimo para las 5 semanas es: ${min_costo_total:.2f}")
print("\nDetalle del Plan Óptimo:")
for step in plan_optimo:
    print(f"Semana {step['week']}: Iniciar con {step['start_workforce']}, contratar hasta {step['chosen_workforce']} "
          f"(Req: {step['requirement']}, Exceso: {step['excess']}, Contratados: {step['hired']}). "
          f"Costo Semana: ${step['weekly_cost']:.2f}")