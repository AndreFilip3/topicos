while True:
    try:
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))
        
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos.")
            continue
        
        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc:.2f}")
        
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")
        continue
    
    resposta = input("Deseja continuar? (s/n) ")
    if resposta.lower() != "s":
        break