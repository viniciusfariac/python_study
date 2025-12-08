import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent


# os.mkdir(ROOT_PATH / "diretorio_teste")

# arquivo = open(ROOT_PATH / "novo.txt", "r")
# arquivo.close()

# os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")
# os.remove(ROOT_PATH / "alterado.txt")
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "diretorio_teste" / "novo.txt")