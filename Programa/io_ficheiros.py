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
