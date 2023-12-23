import pickle

from clientes import nome_ficheiro_lista_de_clientes
from faturas import nome_ficheiro_lista_de_faturas

from veiculos import nome_ficheiro_lista_de_veiculos


def le_de_ficheiro(nome_ficheiro):
   """
    Lê os dados de um ficheiro utilizando o formato de serialização pickle.

    :param nome_ficheiro: O nome do ficheiro onde estão armazenados os dados.
    :type nome_ficheiro: str
    :return: Os dados lidos do ficheiro (depende do formato de serialização usado).
    :rtype: object
    """

    with open(nome_ficheiro, "rb") as f:
        return pickle.load(f)
   
   def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """Guarda os dados recebidos num ficheiro

    :param nome_do_ficheiro: nome do ficheiro onde vai guardar os dados
    :param dados: dados a serem guardados
    """

    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)


def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas):
   """
    Guarda as listas de veículos, clientes e faturas em ficheiros.

    :param lista_de_veiculos: Lista de veículos a ser guardada no ficheiro.
    :type lista_de_veiculos: list
    :param lista_de_clientes: Lista de clientes a ser guardada no ficheiro.
    :type lista_de_clientes: list
    :param lista_de_faturas: Lista de faturas a ser guardada no ficheiro.
    :type lista_de_faturas: list
    :return: None
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (s/N)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_veiculos, lista_de_veiculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_clientes, lista_de_clientes)
        guarda_em_ficheiro(nome_ficheiro_lista_de_faturas, lista_de_faturas)
    else:
        print("Gravação cancelada...")

        def carrega_as_listas_dos_ficheiros():
     """
    Carrega as listas de veículos, clientes e faturas a partir dos respetivos ficheiros.

    Esta função lê os dados armazenados nos ficheiros correspondentes e retorna as listas
    de veículos, clientes e faturas. Cada lista é carregada de acordo com o formato de
    serialização utilizado.

    :return: Uma tupla contendo as listas carregadas (lista_de_veiculos, lista_de_clientes, lista_de_faturas).
    :rtype: tuple
    """

    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_veiculos)
    lista_de_clientes = le_de_ficheiro(nome_ficheiro_lista_de_clientes)
    lista_de_faturas = le_de_ficheiro(nome_ficheiro_lista_de_faturas)

    return  lista_de_veiculos, lista_de_clientes, lista_de_faturas
