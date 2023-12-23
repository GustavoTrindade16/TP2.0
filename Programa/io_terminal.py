from tabulate import tabulate

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

def pause():
    """
    Faz uma pausa no programa e aguarda que o utilizador pressione ENTER.

    Esta função é utilizada para criar uma pausa durante a execução do programa,
    permitindo que o utilizador pressione a tecla ENTER para continuar a execução.

    Args:
        Nenhum.

    Returns:
        None

    Exemplo:
        >>> pause()
        Pressione ENTER para continuar...

    Nota:
        Esta função utiliza a função `input` do Python para aguardar a entrada do utilizador.
        Após a pausa, o programa continuará a execução.

    Tarefas Pendentes:
        - Considerar a possibilidade de adicionar uma mensagem personalizada.

    """
    input("Pressione ENTER para continuar...")


# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome io_terminal*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro io_terminal.py existente, deve apagar
# todos os outros ficheiros io_terminal-*.py, e inclusive estes comentários

# ...
