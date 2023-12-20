from classData import Data
from classAnaliseDados import AnaliseDados
import numpy as np
import timeit
import statistics
import random 

# Classe Lista Salários

class ListaSalarios(AnaliseDados):

    def __init__(self, salarios=[]):
        super().__init__(type(float))
        self.__lista = salarios        

    def entradaDeDados(self, salario):
        self.__lista.append(salario)

    def mostraMediana(self):
        self.__lista.sort()
        mediana_index = len(self.__lista) // 2
        mediana = self.__lista[mediana_index]
        return mediana

    def mostraMenor(self):
        menor = min(self.__lista)
        return menor

    def mostraMaior(self):
        maior = max(self.__lista)
        return maior

    def listarEmOrdem(self):
        lista_ordenada = sorted(self.__lista)
        return lista_ordenada

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return '\n'.join(str(salario) for salario in self.__lista)

# Função para gerar lista de salários aleatórios

def geraListaSalarios(n, sMin=1000, sMax=5000):
    salarios_aleatorios = [random.uniform(sMin, sMax) for _ in range(n)]
    return ListaSalarios(salarios_aleatorios)