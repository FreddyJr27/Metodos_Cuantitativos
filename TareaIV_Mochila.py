class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

    def __str__(self):
        return f"Objeto(peso={self.peso}, valor={self.valor})"

    def __repr__(self):
        return self.__str__()

class Mochila:
    def __init__(self, capacidad_maxima, objetos):
        self.capacidad_maxima = capacidad_maxima
        self.objetos = objetos

    def resolver_mochila(self):
        n = len(self.objetos)
        W = self.capacidad_maxima

        # Inicializar la tabla de programación dinámica
        dp = [[0] * (W + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            peso_obj = self.objetos[i-1].peso
            valor_obj = self.objetos[i-1].valor
            for w in range(W + 1):
                if peso_obj > w:
                    dp[i][w] = dp[i-1][w]
                else:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w - peso_obj] + valor_obj)

        # Reconstruir la solución
        seleccionados = []
        current_weight = W
        peso_total = 0
        valor_total = dp[n][W]

        for i in range(n, 0, -1):
            if dp[i][current_weight] != dp[i-1][current_weight]:
                obj = self.objetos[i-1]
                seleccionados.append(obj)
                current_weight -= obj.peso
                peso_total += obj.peso

        seleccionados.reverse()
        return seleccionados, valor_total, peso_total

# Ejemplo de uso
if __name__ == "__main__":
    capacidad_maxima = 10
    objetos = [
        Objeto(peso=5, valor=10, nombre="Cartera"),
        Objeto(peso=4, valor=40 , nombre="Lapiz"),
        Objeto(peso=6, valor=30 , nombre="Bolso"),
        Objeto(peso=3, valor=50 , nombre="celular"),
    ]

    mochila = Mochila(capacidad_maxima, objetos)
    seleccionados, valor_total, peso_total = mochila.resolver_mochila()

    print("Objetos seleccionados:")
    for obj in seleccionados:
        print(obj)
    print(f"Valor total: {valor_total}")
    print(f"Peso total: {peso_total}")