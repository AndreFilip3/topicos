import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def ler_numero():
    try:
        return int(input("Informe um valor: "))
    except ValueError:
        print("Erro: Por favor, informe um número válido.")
        return ler_numero()

def soma(n1, n2):
    return n1 + n2

def main():
    limpar_tela()
    n1 = ler_numero()
    n2 = ler_numero()
    print(f"A soma é: {soma(n1, n2)}")

main()
