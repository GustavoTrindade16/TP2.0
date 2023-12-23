def pergunta_id(questao, lista, mostra_lista=False):
    """
    Solicita ao utilizador um ID da lista.

    Esta função interage com o utilizador, apresentando uma questão e, opcionalmente,
    mostrando a lista de opções disponíveis. O utilizador é solicitado a inserir um ID,
    e a função valida se o ID está dentro dos limites da lista. Se não estiver, o utilizador
    é informado, e a pergunta é repetida até que um ID válido seja fornecido.

    Args:
        questao (str): A questão a ser apresentada ao utilizador.
        lista (list): A lista de opções disponíveis.
        mostra_lista (bool): Se True, imprime a lista antes de solicitar o ID.

    Returns:
        int: O ID fornecido pelo utilizador.

    Example:
        >>> opcoes = ["Opção A", "Opção B", "Opção C"]
        >>> pergunta_id("Escolha uma opção:", opcoes, mostra_lista=True)
        Escolha uma opção:
        +----+----------+
        | id | Opções   |
        +====+==========+
        | 0  | Opção A  |
        | 1  | Opção B  |
        | 2  | Opção C  |
        +----+----------+
        1

    Nota:
        Se a opção `mostra_lista` for True, a função utiliza a função `imprime_lista` para
        apresentar as opções disponíveis.

    Tarefas Pendentes:
        - Adicionar suporte a mensagens de erro personalizadas.

    :param questao: A questão a ser apresentada ao utilizador.
    :param lista: A lista de opções disponíveis.
    :param mostra_lista: Se True, imprime a lista antes de solicitar o ID.
    :return: O ID fornecido pelo utilizador.
    """
    
    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"ID inexistente. Tente novamente. Valores admitidos de {0} a {len(lista) - 1}")

