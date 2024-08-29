# Exercício 3
entrada = input("Digite uma sequência de palavras separadas por vírgula: ")
palavras = entrada.split(",")
palavras.sort()
print("Palavras ordenadas:", ", ".join(palavras))
