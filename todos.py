from datetime import date

def create(titulo: str, itens: list[str], data_final=None):
    if data_final is None:
        data = None
    else:
        data = date.fromisoformat(data_final)
    todo = {
        "titulo": titulo,
        "itens": itens,
        "data final": data
    }
    print("Criando afazer", todo["titulo"])
    return todo

def read(todo):
    print('Titulo: ', todo["titulo"])
    print("Itens: ")
    for item in todo["itens"]:
        print(item)
    if todo["data final"] is not None:
        print("Data Final: ", todo["data final"])