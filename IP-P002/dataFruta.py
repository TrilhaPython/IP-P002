from abc import ABC, abstractmethod
import numpy as np
import timeit
import statistics

#Classe Análise de Dados

class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass
    
    @abstractmethod
    def listarEmOrdem(self):
        pass

# Classe Data

class Data:
    
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

# Classe Lista Datas

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

# Classe Lista Nomes

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

# Classe Lista Salários

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

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

# Function

def incluirNome(listaNomes):
    nome = input("Digite um nome: ")
    listaNomes.entradaDeDados(nome)

def incluirSalario(listaSalarios):
    salario = float(input("Digite um salário: "))
    listaSalarios.entradaDeDados(salario)

def incluirData(listaDatas):
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    data = Data(dia, mes, ano)
    listaDatas.entradaDeDados(data)

def incluirIdade(listaIdades):
    idade = int(input("Digite uma idade: "))
    listaIdades.entradaDeDados(idade)

def percorrerListas(listaNomes, listaSalarios):
    print("Iterador zip:")
    for nome, salario in zip(listaNomes, listaSalarios):
        print(f"{nome}: {salario}")

def calcularReajuste(listaSalarios):
    print("Iterador map:")
    salarios_reajustados = map(lambda x: x * 1.1, listaSalarios)
    print(list(salarios_reajustados))

def modificarDiasAntes2019(listaDatas):
    print("Iterador filter:")
    listaDatas.atualizarDiasAntes2019()
    for data in listaDatas:
        print(data)

# Main Menu

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    while True:
        print("\nMenu:")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salário na lista de salários")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salários")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Gerar uma lista de idades aleatórias")
        print("9. Sair")

        escolha = input("Escolha uma opção (1-9): ")

        if escolha == '1':
            incluirNome(nomes)
        elif escolha == '2':
            incluirSalario(salarios)
        elif escolha == '3':
            incluirData(datas)
        elif escolha == '4':
            incluirIdade(idades)
        elif escolha == '5':
            percorrerListas(nomes, salarios)
        elif escolha == '6':
            calcularReajuste(salarios)
        elif escolha == '7':
            modificarDiasAntes2019(datas)
        elif escolha == '8':
            qtd = int(input("Quantidade de idades a serem geradas: "))
            lista_aleatoria = geraListaIdades(qtd)
            print("Lista de idades aleatórias:")
            print(lista_aleatoria)
        elif escolha == '9':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
