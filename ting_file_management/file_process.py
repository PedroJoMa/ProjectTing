from ting_file_management.queue import Queue
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
    class_queue = Queue()
    fila = process(instance, class_queue)
    try:
        print(fila[position])
    except IndexError:
        return "Posição inválida"

    # if instance.search(path_file) is not None:
    #     print(f"Arquivo {path_file} já foi processado anteriormente")
    #     return

    # file_lines = txt_importer(path_file)
    # if not file_lines:
    #     return

    # file_dict = process_file(file_lines)

    # instance.enqueue(path_file)
    # instance.enqueue(file_dict)

    # print(f"Dados processados do arquivo {path_file}:")
    # print(file_dict)
