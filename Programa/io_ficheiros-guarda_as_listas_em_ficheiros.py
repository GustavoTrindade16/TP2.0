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
