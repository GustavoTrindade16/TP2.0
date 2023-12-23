def imprime_lista_de_faturas(lista_de_faturas):
    """
    Imprime a lista de faturas.

    Esta função recebe uma lista de faturas e imprime as informações de cada fatura na lista.
    As informações incluem o ID do cliente, o ID do veículo, a data da fatura e outros campos
    relevantes que podem ser adicionados conforme necessário.

    Args:
        lista_de_faturas (list): Uma lista contendo dicionários, cada dicionário representando
            as informações de uma fatura. Cada dicionário deve ter as chaves 'cliente', 'veiculo'
            e 'data' como mínimo.

    Returns:
        None

    Raises:
        ValueError: Se a lista de faturas estiver vazia ou se algum dicionário na lista não tiver
            as chaves necessárias.

    Example:
        >>> faturas = [{'cliente': 1, 'veiculo': 101, 'data': date.today()},
        ...            {'cliente': 2, 'veiculo': 102, 'data': date.today()}]
        >>> imprime_lista_de_faturas(faturas)
        Cliente: 1, Veículo: 101, Data: 2023-12-23
        Cliente: 2, Veículo: 102, Data: 2023-12-23

    Note:
        Certifique-se de fornecer uma lista válida de faturas para garantir que a função opere
        corretamente. Caso contrário, exceções serão levantadas para indicar problemas na entrada.

    Todo:
        - Implementar a lógica de impressão das faturas.
        - Garantir a formatação adequada das informações durante a impressão.

    """
    if not lista_de_faturas:
        raise ValueError("Erro: A lista de faturas não pode estar vazia.")

    for fatura in lista_de_faturas:
        if not all(key in fatura for key in ('cliente', 'veiculo', 'data')):
            raise ValueError("Erro: Cada dicionário na lista deve ter as chaves 'cliente', 'veiculo' e 'data'.")

        id_cliente = fatura['cliente']
        id_veiculo = fatura['veiculo']
        data_fatura = fatura['data']

        print(f"Cliente: {id_cliente}, Veículo: {id_veiculo}, Data: {data_fatura}")
