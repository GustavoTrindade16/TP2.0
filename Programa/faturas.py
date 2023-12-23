import os
import sys
sys.path.insert(0, os.path.abspath('../scr'))

from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"

def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
    """
    Solicita ao utilizador a introdução dos dados de uma nova fatura.

    Esta função interage com o utilizador para obter os dados necessários à criação
    de uma nova fatura. Os dados incluem o ID do cliente, o ID do veículo e outros
    campos relevantes, os quais podem ser adicionados conforme necessário. A função
    retorna um dicionário representando a nova fatura.

    Argumentos:
        lista_de_clientes (list): Uma lista de clientes disponíveis.
        lista_de_veiculos (list): Uma lista de veículos disponíveis.

    Returns:
        dict: Um dicionário representando a nova fatura. O dicionário terá as seguintes chaves:
            - "cliente": O ID do cliente associado à fatura (int).
            - "veiculo": O ID do veículo associado à fatura (int).
            - "data": A data atual da criação da fatura (objeto date).
            - Outros campos relevantes podem ser adicionados conforme necessário.

    Exemplo:
        >>> clientes = [{"id": 1, "nome": "João Silva"},
        ...             {"id": 2, "nome": "Maria Oliveira"}]
        >>> veiculos = [{"id": 101, "modelo": "Carro A"},
        ...              {"id": 102, "modelo": "Carro B"}]
        >>> nova_fatura = cria_nova_fatura(clientes, veiculos)
        >>> print(nova_fatura)
        {"cliente": 1, "veiculo": 101, "data": date.today(), ...}

    Nota:
        Certifique-se de validar os dados de entrada antes de retornar o dicionário.
        Em caso de dados inválidos, a função pode solicitar novamente as informações
        ou levantar exceções conforme necessário.

    Tarefas Pendentes:
        - Pedir o resto dos dados da fatura.
        - Validar os dados para garantir que sejam válidos e relevantes.
        - Devolver um dicionário com as informações da nova fatura.
    """
    id_cliente = pergunta_id(questão="Qual o ID do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questão="Qual o ID do veículo?", lista=lista_de_veiculos, mostra_lista=True)

    fatura = {"cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today()}

    return fatura
    
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

# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome faturas*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro faturas.py existente, deve apagar
# todos os outros ficheiros faturas-*.py, e inclusive estes comentários

# ...
