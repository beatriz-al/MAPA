import pygsheets
from datetime import date

today = date.today().strftime("%d/%m/%Y")

# conexão com o sheets do google
c_google = pygsheets.authorize(
    service_file="../mapa/service_account.json")

# abrindo a planilha com base no ID. Voce pode pegar o id na URL
abre_id = c_google.open_by_key('1AuxSmUvngx_Fk0YWDu1UHz28NihY6Ds76pkYGblnRFg')

# escolhe sheet pelo index
primeiro_sheet = abre_id[0]

# pega todo o conteudo da planilha
conteudo = primeiro_sheet.get_all_values(include_tailing_empty=False)
# retira os arrays vazios
valores_planilha = list(filter(None, conteudo))

# print(valores_planilha)

for i, linha in enumerate(valores_planilha):
    if today in valores_planilha[i][0]:
        primeiro_sheet.update_value(f'K{i+1}', 'Criado')