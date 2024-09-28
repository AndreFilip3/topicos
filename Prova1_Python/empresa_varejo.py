import json

produtos = []
codigo_incremental = 1

def exibir_menu():
    print("\nVarejão do João")
    print("[1] Cadastrar produto")
    print("[2] Relatório de produtos")
    print("[3] Relatório de Estoque Baixo")
    print("[4] Exportar dados")
    print("[0] Sair")

def cadastrar_produto():
    global codigo_incremental
    nome = input("Nome do produto: ")
    valor_compra = float(input("Valor de compra: "))
    quantidade = int(input("Quantidade em estoque: "))
    valor_venda = valor_compra * 1.25  
    
    produto = {
        "codigo": codigo_incremental,
        "nome": nome,
        "valor_compra": valor_compra,
        "valor_venda": valor_venda,
        "quantidade": quantidade
    }
    
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")
    
    codigo_incremental += 1  
    
def relatorio_produtos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\nRelatório de Produtos:")
        for produto in produtos:
            print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, "
                  f"Valor de Compra: R$ {produto['valor_compra']}, "
                  f"Valor de Venda: R$ {produto['valor_venda']}, "
                  f"Quantidade: {produto['quantidade']}")

def relatorio_estoque_baixo():
    print("\nRelatório de Estoque Baixo:")
    encontrou_baixo = False
    for produto in produtos:
        if produto["quantidade"] <= 5:
            print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, "
                  f"Quantidade: {produto['quantidade']}")
            encontrou_baixo = True
    
    if not encontrou_baixo:
        print("Nenhum produto com estoque baixo.")

def exportar_dados():
    with open('produtos.json', 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)
    print("Dados exportados com sucesso!")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            relatorio_produtos()
        elif opcao == "3":
            relatorio_estoque_baixo()
        elif opcao == "4":
            exportar_dados()
        elif opcao == "0":
            print("Você escolheu sair :( -> Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Execução do programa
if __name__ == "__main__":
    main()