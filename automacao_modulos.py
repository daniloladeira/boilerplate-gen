from pathlib import Path

def criar_estrutura_modulo(modulo):
    pasta_modulo = Path(modulo.upper())

    if pasta_modulo.exists():
        print(f'Uma pasta com o nome {pasta_modulo} já existe')
    else :
        pasta_modulo.mkdir()
        print(f'Pasta {pasta_modulo} criada com sucesso!')
    
    files = {
        "arquivo_exemplos": pasta_modulo / f'exemplos-{modulo}.js',
        "arquivo_exercicio": pasta_modulo / f'exercicio-{modulo}.js',
        "arquivo_html": pasta_modulo / 'index.html'
    }

    conteudos = {
        "arquivo_exemplos": f"// Código de exemplo do módulo {modulo}\n",
        "arquivo_exercicio": f"// Código de exercicio do módulo {modulo}\n",
        "arquivo_html": 
        f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Módulo {modulo}</title>
</head>
<body>
    <script src="exemplos-{modulo}.js"></script>
    <script src="exercicio-{modulo}.js"></script>
</body>
</html>
"""
    }
    
    for nome, caminho in files.items():
        if caminho.exists():
            print(f'O arquivo {caminho.name} já existe.')
        else:
            print(f'O arquivo {caminho.name} não existe. Criando agora...')
            caminho.write_text(conteudos[nome], encoding="utf-8")
            print(f'Arquivo {caminho.name} criado.')

modulo = input("Módulo da aula: ")

criar_estrutura_modulo(modulo)