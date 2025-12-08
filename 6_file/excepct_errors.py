import os
from pathlib import Path

try:
    ROOT_PATH = Path(__file__).parent
    arquivo = open(ROOT_PATH / "er.txt", "r")
except FileNotFoundError as error:
    print("Arquivo não encontrado ", error)
except IOError as error:
    print("Permissão negada ", error)
except IsADirectoryError as error:
    print("Diretorio não encontrado ", error)