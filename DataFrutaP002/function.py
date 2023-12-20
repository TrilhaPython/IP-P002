from classData import Data
from classListaDatas import ListaDatas
from classListaIdades import ListaIdades
from classListaNomes import ListaNomes
from classListaSalarios import ListaSalarios
from classAnaliseDados import AnaliseDados

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