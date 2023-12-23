def imprime_lista(cabecalho, lista):
    """Imprime a :attr:`lista` na forma de uma tabela com um cabeçalho

    Esta função recebe uma lista de dicionários e imprime no terminal uma tabela
    com um cabeçalho especificado. A tabela é formatada utilizando a biblioteca tabulate.

    Argumentos:
        cabecalho (str): Cabeçalho para a listagem.
        lista (list): Lista de dicionários a ser impressa.

    Recebe uma lista na forma [{"atrib1": valor1, "atrib2": valor2, ...},
    {"atrib1": valor1, "atrib2": valor2, ...}, ...] e imprime no terminal uma tabela
    na forma

    ==  ======  ======
    id  atrib1  atrib2
    ==  ======  ======
    0   valor1  valor2
    1   ...      ...
    ==  ======  ======
    
    Exemplo:

        >>> cabecalho = "Listagem de Clientes"
        >>> lista = [{"id": 0, "nome": "João", "idade": 25},
        ...          {"id": 1, "nome": "Maria", "idade": 30}]
        >>> imprime_lista(cabecalho, lista)
        +----+-------+-------+
        | id | nome  | idade |
        +====+=======+=======+
        | 0  | João  | 25    |
        | 1  | Maria | 30    |
        +----+-------+-------+

    :param cabecalho: Cabecalho para a listagem
    :param lista: Lista a ser impressa

    Returns:
        None

    Verificar:
        ValueError: Se a lista estiver vazia.

    Notação:
        Se a lista estiver vazia, será levantada uma exceção ValueError.
    """
    
    print(cabecalho)

    if (len(lista) == 0):
        print("Lista vazia")
    else:
        # cabecalho da tabela
        lista_a_imprimir = [["id"] + list(lista[0].keys())]
        # dados
        lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])

        print(tabulate(lista_a_imprimir, headers="firstrow", tablefmt='psql'))


        from tabulate import tabulate


