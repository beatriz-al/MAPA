from numpy import c_
import pygsheets
import pandas as pd

# conexão com o sheets do google
c_google = pygsheets.authorize(
    service_file="../mapa/service_account.json")

print(c_google.spreadsheet_titles())

# dataframe vazio
dataframe = pd.DataFrame()

# dados que serão inseridos --> cabeçalho/linhas
dataframe['teste'] = ['ana', 'marcos', 'cesinha', 'bia']

# abre a planilha
#abre_planilha = c_google.open('TESTEE')

# abrindo a planilha com base no ID. Voce pode pegar o id na URL =>>>> https://docs.google.com/spreadsheets/d/1D_NUCWNMg5x-wGT4LYR-2x3-Nr5hG2AaEzSAfbBTIuI/edit#gid=0
abre_id = c_google.open_by_key('1D_NUCWNMg5x-wGT4LYR-2x3-Nr5hG2AaEzSAfbBTIuI')

# escolhe sheet pelo index
sheet = abre_id[0]

# escreve com base na posição --> linha/coluna
sheet.set_dataframe(dataframe, (3, 1))

