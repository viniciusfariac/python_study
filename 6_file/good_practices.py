from pathlib import Path

PATH_ROOT = Path(__file__).parent

# try:
#     with open(PATH_ROOT / "teste-utf8.txt", "w", encoding="utf8") as file:
#         file.write("Learning manipulations files with python")
# except FileNotFoundError as err:
#     print(f"Arquivo não encontrado {err}")

try:
    with open(PATH_ROOT / "teste-utf8.txt", "r", encoding="utf8") as file:
        print(file.read())
except FileNotFoundError as err:
    print(f"Arquivo não encontrado {err}")
except UnicodeEncodeError as err:
    print(f"Arquivo em outro codigo {err}")