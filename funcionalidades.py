import pygsheets
import pandas as pd
import numpy as np
# conexão com o sheets do google
c_google = pygsheets.authorize(
    service_file="../mapa/service_account.json")

# dataframe vazio
dataframe = pd.DataFrame()

# dados que serão inseridos --> cabeçalho/linhas
dataframe['teste'] = ['ana', 'marcos', 'cesinha', 'bia']

# abre a planilha
#abre_planilha = c_google.open('TESTEE')

# abrindo a planilha com base no ID. Voce pode pegar o id na URL
abre_id = c_google.open_by_key('1D_NUCWNMg5x-wGT4LYR-2x3-Nr5hG2AaEzSAfbBTIuI')

# escolhe sheet pelo index
primeiro_sheet = abre_id[0]
segundo_sheet = abre_id[1]

# escreve com base na posição --> linha/coluna
primeiro_sheet.set_dataframe(dataframe, (3, 1))

# limpa o conteudo da planilha
# segundo_sheet.clear()

# pega valor da célula com base na posição
pega_celula = primeiro_sheet.get_value('A3')
pega_celula2 = primeiro_sheet.cell((3, 1)).value

# altera valor na posicao
primeiro_sheet.cell((3, 1)).value = 'Escrevendo'
primeiro_sheet.update_value('A9', 'Feito')

# pega todo o conteudo da planilha
# pd.DataFrame(segundo_sheet.get_all_values())
conteudo = segundo_sheet.get_all_values(include_tailing_empty=False)
conteudo_dict = segundo_sheet.get_all_records()
# retira os arrays vazios
valores_planilha = list(filter(None, conteudo))

print(valores_planilha)

# outra forma de ler a planilha, mas a de cima é melhor
le_planilha = segundo_sheet.get_as_df()
print(le_planilha.head())

# pegando o valor de uma linha ou coluna específicos
# print(segundo_sheet.get_row(2,include_tailing_empty=False))
# print(segundo_sheet.get_col(3,include_tailing_empty=False))
