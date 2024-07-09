def extrai_linha_txt(nome_arquivo: str, numero_linha: int):
    try:
        with open(nome_arquivo, encoding='utf8') as fp:
            # Pula as linhas até chegar na linha desejada (começando da linha 1)
            for _ in range(numero_linha - 1):
                next(fp)

            # Lê a linha desejada, remove o caractere de nova linha e divide por espaços
            linha = next(fp).rstrip('\n')
            return linha.split(' ')
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []
    except StopIteration:
        print(f"Linha {numero_linha} não encontrada no arquivo '{nome_arquivo}'.")
        return []

# Exemplo de uso da função para extrair a linha 11 do arquivo './musica.txt'
linha11 = extrai_linha_txt(nome_arquivo='./musica.txt', numero_linha=11)
print(linha11)  # Deve retornar ['Mas', 'eis', 'que', 'chega', 'a', 'roda', 'viva']
