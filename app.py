import random
import statistics

class ListaIdade:
    def __init__(self, lista):
        self.lista = lista

    def mostraMediana(self):
        return statistics.median(self.lista)

    def mostraMenor(self):
        return min(self.lista)

    def mostraMaior(self):
        return max(self.lista)

def geraListaIdade(n, iMin=18, iMax=65):
    lista_idades = [random.randint(iMin, iMax) for _ in range(n)]
    return ListaIdade(lista_idades)

class ListaSalarios:
    def __init__(self, lista):
        self.lista = lista

    def mostraMediana(self):
        return statistics.median(self.lista)

    def mostraMenor(self):
        return min(self.lista)

    def mostraMaior(self):
        return max(self.lista)

def geraListaSalarios(n, sMin=1000, sMax=5000):
    lista_salarios = [round(random.uniform(sMin, sMax), 2) for _ in range(n)]
    return ListaSalarios(lista_salarios)

# Testando ListaIdade
idades_obj = geraListaIdade(5000)

# Tempo para mostrar a mediana
%timeit idades_obj.mostraMediana()

# Tempo para mostrar o menor valor
%timeit idades_obj.mostraMenor()

# Tempo para mostrar o maior valor
%timeit idades_obj.mostraMaior()

# Testando ListaSalarios
salarios_obj = geraListaSalarios(5000)

# Tempo para mostrar a mediana
%timeit salarios_obj.mostraMediana()

# Tempo para mostrar o menor valor
%timeit salarios_obj.mostraMenor()

# Tempo para mostrar o maior valor
%timeit salarios_obj.mostraMaior()