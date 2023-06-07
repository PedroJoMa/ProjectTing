import sys
import os


def txt_importer(path_file):
    if not os.path.isfile(path_file):
        error_message = f"Arquivo {path_file} não encontrado"
        print(error_message, file=sys.stderr)
        return []

    if not path_file.lower().endswith(".txt"):
        error_message = "Formato inválido"
        print(error_message, file=sys.stderr)
        return []

    with open(path_file, "r") as file:
        lines = file.read().split("\n")
        return lines
