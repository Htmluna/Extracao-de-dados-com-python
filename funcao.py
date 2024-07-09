def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: type):
    coluna = []

    # Abre o arquivo e lê linha por linha
    with open(nome_arquivo, mode='r', encoding='utf8') as fp:
        fp.readline()  # Ignora o cabeçalho

        linha = fp.readline().strip()  # Lê a primeira linha

        while linha:
            linha_separada = linha.split(',')  # Separa a linha por vírgulas

            if indice_coluna < len(linha_separada):
                valor = linha_separada[indice_coluna].strip()

                # Converte o valor para o tipo de dado especificado
                if tipo_dado == str:
                    coluna.append(valor)
                elif tipo_dado == int:
                    coluna.append(int(valor))
                elif tipo_dado == float:
                    coluna.append(float(valor))
                else:
                    print('Tipo de dado não suportado')
                    break

            linha = fp.readline().strip()  # Lê a próxima linha

    return coluna

# Testes das funções

# Extrair a coluna 'valor_venda' como strings
valor_venda = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=1, tipo_dado=str)
print(valor_venda)  # Deve retornar ['vhigh', 'med', 'low', ...]

# Extrair a coluna 'pessoas' como inteiros
pessoas = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=4, tipo_dado=int)
print(pessoas)  # Deve retornar [2, 2, 2, ...]


