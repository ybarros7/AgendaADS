# Agenda Telefonica
import funcoes

while True:
    funcoes.bemvindo()

    # Opcoes do Usuario
    opcao = str(input())
    print("Seleccionaste", opcao)

    # Estrutura de controle
    if opcao == "1":
        funcoes.adicionar()
        continue
    elif opcao == "2":
        funcoes.listar(1)
        continue
    elif opcao == "4":
        funcoes.buscar()
        continue
    elif opcao == "5":
        funcoes.deletar()
        continue
    elif opcao == "9":
        break
    else:
        funcoes.falha()
        continue
