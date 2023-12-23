import os
import sys
sys.path.insert(0, os.path.abspath('../scr'))

from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"


def cria_novo_veiculo():
    """Pede ao utilizador para introduzir um novo veiculo

    :return: dicionario com um veiculo na forma
        {"marca": <<marca>>, "matricula": <<matricula>>, ...}
    """

    marca = input("marca? ")
    matricula = input("matricula? ").upper()

    # TODO: Pedir o resto dos dados do veiculo, e não esquecer de os guardar no dicionario
    # ...

    veiculo = {"marca": marca,
               "matricula": matricula}

    return veiculo

def imprime_lista_de_veiculos(lista_de_veiculos):
    def imprime_lista_de_veiculos(lista_de_veiculos):
    """
    Imprime a lista de veículos formatadamente.

    :param lista_de_veiculos: Lista de veículos a ser impressa.
    :type lista_de_veiculos: list
    :return: None
    """

    # TODO: Implementar uma descrição adequada para a função
    imprime_lista(cabecalho="Lista de Veículos", lista=lista_de_veiculos)


    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)
