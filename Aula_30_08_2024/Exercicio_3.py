def coletar_informacoes():
    """Coleta as informações do usuário."""
    nome = input("Digite seu nome: ")
    endereco = input("Digite seu endereço: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: ")
    escolaridade = input("Digite sua escolaridade: ")
    experiencia = input("Descreva sua experiência profissional: ")
    
    return {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "escolaridade": escolaridade,
        "experiencia": experiencia
    }

def gerar_html(curriculo):
    """Gera o código HTML do currículo."""
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo de {curriculo['nome']}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            p {{ line-height: 1.6; }}
        </style>
    </head>
    <body>
        <h1>Currículo de {curriculo['nome']}</h1>
        <p><strong>Endereço:</strong> {curriculo['endereco']}</p>
        <p><strong>Telefone:</strong> {curriculo['telefone']}</p>
        <p><strong>E-mail:</strong> {curriculo['email']}</p>
        <p><strong>Escolaridade:</strong> {curriculo['escolaridade']}</p>
        <h2>Experiência Profissional</h2>
        <p>{curriculo['experiencia']}</p>
    </body>
    </html>
    """
    return html

def salvar_html(html, nome):
    """Salva o HTML em um arquivo."""
    with open(f"{nome.replace(' ', '_')}_curriculo.html", "w") as file:
        file.write(html)
    print(f"Currículo salvo como {nome.replace(' ', '_')}_curriculo.html")

def main():
    """Função principal que executa o programa."""
    curriculo = coletar_informacoes()
    html = gerar_html(curriculo)
    salvar_html(html, curriculo['nome'])

# Executa o programa
if __name__ == "__main__":
    main()