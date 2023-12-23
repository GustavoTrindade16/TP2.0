from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def imprime_lista_de_clientes(lista_de_clientes):
    """
        Imprime a lista de clientes.

        Esta função recebe uma lista de clientes e imprime as informações
        de cada cliente na lista.

        Argumentos:
            lista_de_clientes (list): Uma lista contendo dicionários, cada
                dicionário representando as informações de um cliente.
                Cada dicionário deve ter as chaves 'nome' e 'idade' como mínimo.

        Returns:
            None

        Raises:
            ValueError: Se a lista de clientes estiver vazia ou se algum
                dicionário na lista não tiver as chaves 'nome' e 'idade'.

        Exemplo:
            >>> clientes = [{'nome': 'João', 'idade': 25},
            ...             {'nome': 'Maria', 'idade': 30}]
            >>> imprime_lista_de_clientes(clientes)
            Nome: João, Idade: 25
            Nome: Maria, Idade: 30

        Detailhe do Exemplo:
            A função aceita uma lista de clientes com informações mínimas
            sobre cada cliente. A lista pode ter a seguinte estrutura:

            [
                {'nome': 'Cliente1', 'idade': 30},
                {'nome': 'Cliente2', 'idade': 25},
                ...
            ]

            Cada cliente deve ter um nome ('nome') e uma idade ('idade').
            Se a lista estiver vazia ou se algum cliente não atender a esses
            critérios, um ValueError será levantado.

        Notação:
            Certifique-se de fornecer uma lista válida de clientes para
            garantir que a função opere corretamente. Caso contrário, exceções
            serão levantadas para indicar problemas na entrada.

        Mostração em codigo : 
            if not lista_de_clientes:
                raise ValueError("Erro: A lista de clientes não pode estar vazia.")

            for cliente in lista_de_clientes:
                if not all(key in cliente for key in ('nome', 'idade')):
                    raise ValueError("Erro: Cada dicionário na lista deve ter as chaves 'nome' e 'idade'.")

                nome = cliente['nome']
                idade = cliente['idade']
                print(f"Nome: {nome}, Idade: {idade}")
    """

    #TODO: Implementar esta função
    # ...


def cria_novo_cliente():
    """
        Solicita os dados de um novo cliente.

        Esta função tem como objetivo interagir com o utilizador para obter os dados necessários
        à criação de um novo registo de cliente. Os dados incluem o nome, NIF (Número de Identificação
        Fiscal), e outros campos relevantes, os quais podem ser adaptados conforme necessário.

        Returna:
            dict: Um dicionário representando o novo cliente. O dicionário terá as seguintes chaves:
                - "nome": O nome do cliente (str).
                - "nif": O NIF (Número de Identificação Fiscal) do cliente (str).
                - Outros campos relevantes podem ser adicionados conforme necessário.

        Exemplo:
            >>> novo_cliente = cria_novo_cliente()
            >>> print(novo_cliente)
            {"nome": "João Silva", "nif": "123456789", ...}

        Nota:
            Certifique-se de validar os dados de entrada antes de retornar o dicionário.
            Em caso de dados inválidos, a função pode solicitar novamente as informações
            ou levantar exceções conforme necessário.

        Tarefas Pendentes:
            - Solicitar os dados do cliente.
            - Validar os dados para garantir que sejam válidos e relevantes.
            - Devolver um dicionário com as informações do novo cliente.
    """
    # TODO: pedir os dados do cliente e não esquecer de os devolver
    # ...

    pass

# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome clientes-*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro clientes.py existente, deve apagar
# todos os outros ficheiros clientes-*.py, e inclusive estes comentários

# ...
