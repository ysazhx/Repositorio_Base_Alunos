print("--------------------------------")
print("!Sistema de Estoque de Produtos!")
print("--------------------------------")

produto = []

def cadastrar(produto): # type: ignore
    novo_produto = input("Digite o novo produto: ")
    produto.append(novo_produto)
    print(f"Produto {novo_produto} Adicionado com sucesso!")

def listar(produto):
  for i, produtos in enumerate(produto, start=1):
            print(f"{i}. {produtos}")

def excluir(excluir_produto):
    excluir_produto = input("Digite o nome do Produto: ")
    produto.remove(excluir_produto)
    print(f"{excluir_produto}Excluido com sucesso")

try:
    while True:
        print("--------------------------------")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produto")
        print("3 - Exclui Produto")
        print("0 - Sair")
        print("--------------------------------")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
          cadastrar(produto)
        elif opcao == "2":
          listar(produto)
        elif opcao == "3":
          excluir(produto)
        elif opcao == "0":
            break
except:
    print("Código inválido, tente novamente")
