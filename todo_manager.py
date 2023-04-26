from todos import create, read

lista_todos = []

def ler_lista():
    if len(lista_todos) == 0:
        print("Não há afazeres")
    else:
        print("Imprimindo a lista de afazeres")
        for todo in lista_todos:
            read(todo)

def criar_um_todo():
    print("Digite o título da lista")
    titulo = input(">>> ")
    print("Digite os itens da lista separados por vírgula")
    lista_afaz = input(">>> ")
    itens = lista_afaz.split(",")
    # eu que coloquei isso pra caso a pessoa coloque espaço depois da vírgula
    for i in range(0, len(itens)):
        itens[i] = itens[i].strip()
    print("Tem data limite? (S/N)")
    data = input(">>> ")
    if data.lower() == "n":
        data = None
    elif data.lower() == "s":
        print("Insira a data limite (AAAA-MM-DD)")
        data = input(">>> ")
    todo = create(titulo, itens, data)
    global lista_todos
    lista_todos.append(todo)

def salvar():
    file = open('listas.txt', 'w')
    global lista_todos
    file.writelines(lista_todos)
    file.close()