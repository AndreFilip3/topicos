# Inicializa as variáveis
numeros = []
pares = 0
impares = []
maior = None
menor = None
soma = 0

# Recebe os números do usuário
while True:
    numero = input("Digite um número (ou 'q' para sair): ")
    if numero.lower() == 'q':
        break
    numero = int(numero)
    numeros.append(numero)

# Determina a quantidade de números pares
for num in numeros:
    if num % 2 == 0:
        pares += 1

# Determina quais são os números ímpares
impares = [num for num in numeros if num % 2 != 0]

# Determina o maior e o menor número
maior = max(numeros)
menor = min(numeros)

# Calcula a média dos números
for num in numeros:
    soma += num
media = soma / len(numeros)

# Apresenta os resultados
print("Resultados:")
print(f"Quantidade de números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média dos números: {media:.2f}")