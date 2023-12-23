

from clientes import cria_novo_cliente, imprime_lista_de_clientes
from faturas import cria_nova_fatura, imprime_lista_de_faturas
from io_ficheiros import (carrega_as_listas_dos_ficheiros,
                          guarda_as_listas_em_ficheiros)
from io_terminal import pause
from veiculos import cria_novo_veiculo, imprime_lista_de_veiculos

def menu():
    """
    Função que representa o menu principal da aplicação.
    
    Realiza a gestão de clientes, veículos e faturas, permitindo a execução de diversas operações.

    :return: None
    """

    # Listas para armazenar dados
    lista_de_veiculos = []
    lista_de_clientes = []
    lista_de_faturas = []

    while True:
        print("""
        *********************************************************************
        :    (-: OFICINA BARATINHA - RESISTIMOS A QUALQUER ORÇAMENTO :-)    :
        *********************************************************************
        :                                                                   :
        : nc - novo cliente         lc - listagem de clientes               :
        : nv - novo veiculo         lv - listagem de veiculos               :
        : nf - nova fatura          lf - listagem das faturas               :
        : ...                                                               :
        : g - guarda tudo           c - carrega tudo                        :
        : x - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        # Obtém a opção do usuário
        op = input("opcao?").lower()

        # Verifica a opção escolhida
        if op == "x":
            exit()
        elif op == "g":
            # Salva as listas em arquivos
            guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas)
        elif op == "c":
            # Carrega as listas dos arquivos
            lista_de_veiculos, lista_de_clientes, lista_de_faturas = carrega_as_listas_dos_ficheiros()
        elif op == "nc":
            # Adiciona um novo cliente à lista
            novo_cliente = cria_novo_cliente()
            if novo_cliente is not None:
                lista_de_clientes.append(novo_cliente)
        elif op == "nv":
            # Adiciona um novo veículo à lista
            novo_veiculo = cria_novo_veiculo()
            if novo_veiculo is not None:
                lista_de_veiculos.append(novo_veiculo)
        elif op == "nf":
            # Cria uma nova fatura com base nos clientes e veículos
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print("Não há clientes ou veículos registrados...")
                continue
            nova_fatura = cria_nova_fatura(lista_de_clientes, lista_de_veiculos)
            lista_de_faturas.append(nova_fatura)
        elif op == "lc":
            # Imprime a lista de clientes
            imprime_lista_de_clientes(lista_de_clientes)
            pause()
        elif op == "lv":
            # Imprime a lista de veículos
            imprime_lista_de_veiculos(lista_de_veiculos)
            pause()
        elif op == "lf":
            # Imprime a lista de faturas
            imprime_lista_de_faturas(lista_de_faturas)
            pause()

if __name__ == "__main__":
    # Inicia a aplicação executando a função do menu
    menu()
