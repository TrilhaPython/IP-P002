from classData import Data
from classAnaliseDados import AnaliseDados

class ListaDatas(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        

    def entradaDeDados(self, data):
        self.__lista.append(data)

    def mostraMediana(self):
        self.__lista.sort(key=lambda x: (x.ano, x.mes, x.dia))
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

    def atualizarDiasAntes2019(self):
        for data in self.__lista:
            if data.ano < 2019:
                data.dia = 1

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return '\n'.join(map(str, self.__lista))