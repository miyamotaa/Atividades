import os
tarefas = {}

def adicionar_tarefas(tarefa):
    print("--- Adicionar Tarefas ---")
    print("")
    print("Escreva sua tarefa:")
    descrição = input("--> ")
    sua_tarefa = len(tarefa) + 1 
    tarefa[sua_tarefa] = descrição
    print("Tarefa adicionada com sucesso!")
    os.system("pause")
    os.system("cls")

def editar_tarefas(tarefa):
    print("--- Editar Tarefas ---")
    print("")
    if not tarefa:
        print("Você não possuí nenhuma tarefa para editar.")
        os.system("pause")
        os.system("cls")
        return
    
    print("Tarefas existentes:")
    for sua_tarefa, descrição in tarefa.items():
        print(f"{sua_tarefa} - {descrição}")
    
    editar_tarefa = int(input("Qual tarefa deseja editar? \n--> "))
    if editar_tarefa in tarefa:
        nova_descrição = input("Edite a tarefa: ")
        tarefa[editar_tarefa] = nova_descrição
        print("Tarefa editada!")
    else:
        print("Tarefa não encontrada!")
    
    os.system("pause")
    os.system("cls")

def excluir_tarefas(tarefa):
    print("--- Excluir Tarefa ---")
    print("")
    if not tarefa:
        print("Nenhuma tarefa para excluir.")
        os.system("pause")
        os.system("cls")
        return
    
    print("Tarefas existentes:")
    for sua_tarefa, descrição in tarefa.items():
        print(f"{sua_tarefa} - {descrição}")
    
    s_excluir = int(input("Qual tarefa deseja excluir? \n--> "))
    if s_excluir in tarefa:
        del tarefas[s_excluir]
        print("Tarefa excluída!")
    else:
        print("Tarefa não encontrada.")
    
    os.system("pause")
    os.system("cls")

s = 1

while s == 1:
    print("--- Menu To-Do ---")
    print("escolha uma das opções abaixo:")
    print("1 - Adicionar tarefa;")
    print("2 - Editar tarefa;")
    print("3 - Excluir tarefa;")
    print("4 - Sair;")
    print("")
    escolha = int(input("--> "))
    os.system("cls")

    if escolha == 1:
        adicionar_tarefas(tarefas)
    elif escolha == 2:
        editar_tarefas(tarefas)
    elif escolha == 3:
        excluir_tarefas(tarefas)
    elif escolha == 4:
        print("Saindo...")
        break
    else:
        print("Ação invalida!")
        os.system("pause")
        os.system("cls")