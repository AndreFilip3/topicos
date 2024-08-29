# Exercício 5
entrada = input("Digite uma sequência: ")
maiusculas = sum(c.isupper() for c in entrada)
minusculas = sum(c.islower() for c in entrada)
print("Maiúsculas:", maiusculas)
print("Minúsculas:", minusculas)
