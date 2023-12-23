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
