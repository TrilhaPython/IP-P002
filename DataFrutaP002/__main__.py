from classData import Data
from classListaDatas import ListaDatas
from classListaIdades import ListaIdades
from classListaNomes import ListaNomes
from classListaSalarios import ListaSalarios
from classAnaliseDados import AnaliseDados
from function import incluirNome, incluirSalario, incluirData, incluirIdade, percorrerListas, calcularReajuste, modificarDiasAntes2019

from abc import ABC, abstractmethod

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
        print("9. Gerar uma lista de salários aleatórios")
        print("10. Sair")

        escolha = input("Escolha uma opção (1-10): ")

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
            qtd_salarios = int(input("Quantidade de salários a serem gerados: "))
            lista_salarios_aleatorios = geraListaSalarios(qtd_salarios)
            print("Lista de salários aleatórios:")
            print(lista_salarios_aleatorios)    
        elif escolha == '10':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()