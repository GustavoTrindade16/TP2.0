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

