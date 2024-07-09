# Projeto de Análise de Dados

## Descrição
Este projeto contém scripts para análise de dados de carros e processamento de textos. Inclui funções para extrair colunas específicas de arquivos CSV e para extrair linhas específicas de arquivos de texto.

## Estrutura
- **carros.csv**: Arquivo CSV com dados sobre carros.
- **extracao.py**: Contém funções para extração de dados.
- **funcao.py**: Contém funções auxiliares.
- **funcaobonus.py**: Contém funções bônus, incluindo `extrai_linha_txt`.
- **musica.txt**: Arquivo de texto com a letra da música "Roda Viva".
- **readme.md**: Este arquivo de documentação.

## Explicações

## Função:

### Função `extrai_coluna_csv`
- **Parâmetros**:
  - `nome_arquivo`: Nome do arquivo CSV.
  - `indice_coluna`: Índice da coluna que deseja extrair.
  - `tipo_dado`: Tipo de dado para conversão (`str`, `int`, `float`).
- **Descrição**:
  - Lê o arquivo linha por linha.
  - Separa cada linha por vírgulas e extrai o valor da coluna especificada pelo índice.
  - Converte esse valor para o tipo de dado especificado e adiciona à lista `coluna`.
- **Uso do `with open(...)`**:
  - Garante que o arquivo seja fechado automaticamente após o término da operação.
- **Conversão de Tipos**:
  - Implementa uma lógica de conversão clara e eficiente usando o tipo de dado especificado na chamada da função (`str`, `int`, `float`).
- **Exemplos de Uso**:
  ```python
  valor_venda = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=1, tipo_dado='str')
  print(valor_venda)  # Deve retornar ['vhigh', 'med', 'low', ...]

  pessoas = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=4, tipo_dado='int')
  print(pessoas)  # Deve retornar [2, 2, 2, ...]

  ## Função Bônus:

### Função `extrai_linha_txt`

**Parâmetros:**
- `nome_arquivo`: Nome do arquivo de texto a ser lido.
- `numero_linha`: Número da linha que deseja extrair.

**Descrição:**
- Pula as linhas até chegar na linha desejada.
- Lê a linha desejada, remove o caractere de nova linha (`\n`) e divide por espaços.

**Tratamento de Erros:**
- Utiliza `try-except` para capturar possíveis erros durante a leitura do arquivo.
  - `FileNotFoundError`: Retorna uma lista vazia (`[]`) se o arquivo não for encontrado.
  - `StopIteration`: Retorna uma lista vazia (`[]`) se a linha especificada não existir no arquivo.

**Exemplo de Uso:**
```python
linha11 = extrai_linha_txt(nome_arquivo='./musica.txt', numero_linha=11)
print(linha11)  # Deve retornar ['Mas', 'eis', 'que', 'chega', 'a', 'roda']

