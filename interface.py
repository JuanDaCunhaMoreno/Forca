from os import system, name

def limpar_tela():
    """Limpa o terminal de forma compatível com o sistema operacional."""
    if name == 'nt':
        _ = system('cls')  # Windows
    else:
        _ = system('clear')  # Linux/Mac

def display_hangman(chances):
    """Retorna o desenho da forca de acordo com o número de chances restantes."""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[chances]
