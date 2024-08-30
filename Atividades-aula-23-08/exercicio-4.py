# Exercício 4
entrada = input("Digite uma sequência: ")
letras = sum(c.isalpha() for c in entrada)
digitos = sum(c.isdigit() for c in entrada)
print("Letras:", letras)
print("Dígitos:", digitos)