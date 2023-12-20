from classData import Data
from classAnaliseDados import AnaliseDados


class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self, nome):
        self.__lista.append(nome)

    def mostraMediana(self):
        self.__lista.sort()
        mediana = self.__lista[len(self.__lista)//2]
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
        return str(self.__lista)