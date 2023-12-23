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

    # TODO: Pedir o resto dos dados da fatura, e não esquecer de os guardar no dicionário
    # ...

    fatura = {"cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today()}

    return fatura

# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome faturas*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro faturas.py existente, deve apagar
# todos os outros ficheiros faturas-*.py, e inclusive estes comentários

# ...
