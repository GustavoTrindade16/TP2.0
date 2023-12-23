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