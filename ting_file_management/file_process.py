from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return

    file_lines = txt_importer(path_file)

    format_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines
    }
    instance.enqueue(format_data)
    return sys.stdout.write(str(format_data))


def remove(instance):
    if instance.is_empty():
        return print("Não há elementos")
    path_file = instance.dequeue()["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    pass
