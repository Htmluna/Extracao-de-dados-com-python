def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: type):
    coluna = []

    with open(nome_arquivo, mode='r', encoding='utf8') as arquivo:
        arquivo.readline()  # pula o cabeçalho

        linha = arquivo.readline().strip()  # lê a primeira linha

        while linha:
            linha_separada = linha.split(',')  # separa a linha por vírgulas
            if indice_coluna < len(linha_separada):
                valor = linha_separada[indice_coluna].strip()

                # Conversão de tipo de dado conforme especificado
                if tipo_dado == str:
                    coluna.append(valor)
                elif tipo_dado == int:
                    coluna.append(int(valor))  # converte para inteiro
                elif tipo_dado == float:
                    coluna.append(float(valor))  # converte para float
                else:
                    print('Tipo de dado não suportado')
                    break

            linha = arquivo.readline().strip()  # lê a próxima linha

    return coluna

# Teste para extrair a coluna valor_venda (índice 1) como strings
valor_venda = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=1, tipo_dado=str)
print(valor_venda)

# Teste para extrair a coluna porta_malas (índice 5) como strings
porta_malas = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=5, tipo_dado=str)
print(porta_malas)
