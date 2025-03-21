class Objeto:
    def __init__(self, peso: int, valor: int):
        self.peso = peso
        self.valor = valor
        
    def __str__(self):
        return f"Objeto(peso={self.peso}, valor={self.valor})"
    
    def __repr__(self):
        return self.__str__()

class Mochila:
    def __init__(self, capacidad_maxima: int, objetos: list):
        self.capacidad_maxima = capacidad_maxima
        self.objetos = objetos
        self.seleccionados = []
        self.valor_total = 0
        self.peso_total = 0
    
    def resolver_mochila(self):
        n = len(self.objetos)
        mejor_valor = 0
        mejor_combinacion = []
        
        # Generar todas combinaciones posibles (2^n)
        for mascara in range(1 << n):  # 0 a 2^n - 1
            peso_actual = 0
            valor_actual = 0
            combinacion = []
            
            # Verificar cada bit de la máscara
            for i in range(n):
                if mascara & (1 << i):  # Si el bit i está activo
                    obj = self.objetos[i]
                    combinacion.append(obj)
                    peso_actual += obj.peso
                    valor_actual += obj.valor
            
            # Actualizar mejor combinación si es válida y óptima
            if peso_actual <= self.capacidad_maxima and valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_combinacion = combinacion
                self.peso_total = peso_actual
        
        self.seleccionados = mejor_combinacion
        self.valor_total = mejor_valor
    
    def mostrar_resultado(self):
        print("Objetos seleccionados:")
        for obj in self.seleccionados:
            print(obj)
        print(f"\nValor total: {self.valor_total}")
        print(f"Peso total: {self.peso_total}")

# Ejemplo de uso
if __name__ == "__main__":
    capacidad_maxima = 10
    objetos = [
        Objeto(peso=5, valor=10),
        Objeto(peso=4, valor=40),
        Objeto(peso=6, valor=30),
        Objeto(peso=3, valor=50)
    ]
    
    mochila = Mochila(capacidad_maxima, objetos)
    mochila.resolver_mochila()
    mochila.mostrar_resultado()