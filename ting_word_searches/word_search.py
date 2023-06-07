def exists_word(word, instance):
    response = []
    for item in range(len(instance)):
        format_data = {
            "palavra": word,
            "arquivo": instance.search(item)["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for line_number, line in enumerate(instance.search(item)
                                           ["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                format_data["ocorrencias"].append({"linha": line_number + 1})

        if format_data["ocorrencias"]:
            response.append(format_data)

    return response


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
