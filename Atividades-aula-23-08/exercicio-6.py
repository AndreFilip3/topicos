# Exercício 6
import re

def verificar_senha(senha):
    if (6 <= len(senha) <= 12 and
        re.search("[a-z]", senha) and
        re.search("[A-Z]", senha) and
        re.search("[0-9]", senha) and
        re.search("[$#@]", senha)):
        return True
    else:
        return False

senha = input("Digite uma senha: ")
if verificar_senha(senha):
    print("Senha válida")
else:
    print("Senha inválida")
