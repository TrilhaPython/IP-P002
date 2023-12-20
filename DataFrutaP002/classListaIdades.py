from classData import Data
from classAnaliseDados import AnaliseDados
import numpy as np
import timeit
import statistics
import random 

# Classe Lista Idades

class ListaIdades(AnaliseDados):
    
    def __init__(self, lista_idades=None):
        super().__init__(type(int))
        if lista_idades is None:
            lista_idades = []
        self.__lista = np.array(lista_idades)
    
    def entradaDeDados(self, idade):
        self.__lista = np.append(self.__lista, idade)

    def mostraMediana(self):
        mediana = np.median(self.__lista)
        return mediana

    def mostraMenor(self):
        menor = np.min(self.__lista)
        return menor

    def mostraMaior(self):
        maior = np.max(self.__lista)
        return maior

    def listarEmOrdem(self):
        lista_ordenada = np.sort(self.__lista)
        return lista_ordenada

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return '\n'.join(str(idade) for idade in self.__lista)

def geraListaIdades(quantidade, idade_min=18, idade_max=65):
    lista_idades_aleatorias = np.random.randint(idade_min, idade_max + 1, quantidade)
    return ListaIdades(lista_idades_aleatorias)

# Criando uma ListaIdades com 5000 idades aleatórias
lista_idades_grande = geraListaIdades(5000)

# Medição do tempo para o método mostraMediana
tempo_mediana = timeit.timeit("lista_idades_grande.mostraMediana()", globals=globals(), number=100)
print(f"Tempo médio para mostraMediana: {tempo_mediana:.8f} segundos")

# Medição do tempo para o método mostraMenor
tempo_menor = timeit.timeit("lista_idades_grande.mostraMenor()", globals=globals(), number=100)
print(f"Tempo médio para mostraMenor: {tempo_menor:.8f} segundos")

# Medição do tempo para o método mostraMaior
tempo_maior = timeit.timeit("lista_idades_grande.mostraMaior()", globals=globals(), number=100)
print(f"Tempo médio para mostraMaior: {tempo_maior:.8f} segundos")

# Calcula o desvio padrão do timeit
# Lista para armazenar os tempos medidos
tempos_medidos = []

# 100 medições do método mostraMediana
for _ in range(100):
    tempo_mediana = timeit.timeit("lista_idades_grande.mostraMediana()", globals=globals(), number=1)
    tempos_medidos.append(tempo_mediana)

# Calculando o desvio padrão dos tempos medidos
desvio_padrao = statistics.stdev(tempos_medidos)

print(f"Desvio padrão dos tempos medidos: {desvio_padrao:.8f} segundos")