#IMPORTANDO BIBLIOTECAS
import pandas as pd

#LENDO DADOS
df_janeiro = pd.read_csv('BD_imigrantes_2023\JANEIRO_2023.csv',delimiter = ';')
df_fevereiro = pd.read_csv('BD_imigrantes_2023\FEVEREIRO_2023.csv', delimiter = ';')
df_marco = pd.read_csv('BD_imigrantes_2023\MARCO_2023.csv', delimiter = ';')
df_abril = pd.read_csv('BD_imigrantes_2023\ABRIL_2023.csv', delimiter = ';')
df_maio = pd.read_csv('BD_imigrantes_2023\MAIO_2023.csv', delimiter = ';')
df_junho = pd.read_csv('BD_imigrantes_2023\JUNHO_2023.csv', delimiter = ';')
df_julho =  pd.read_csv('BD_imigrantes_2023\JULHO_2023.csv', delimiter = ';')
df_agosto =  pd.read_csv('BD_imigrantes_2023\AGOSTO_2023.csv', delimiter = ';')
df_setembro =  pd.read_csv('BD_imigrantes_2023\SETEMBRO_2023.csv', delimiter = ';')
df_outubro =  pd.read_csv('BD_imigrantes_2023\OUTUBRO_2023.csv', delimiter = ';')
df_novembro  =  pd.read_csv('BD_imigrantes_2023\NOVEMBRO_2023.csv', delimiter = ';')
df_dezembro =  pd.read_csv('BD_imigrantes_2023\DEZEMBRO_2023.csv', delimiter = ';')

#FUNÇÃO -> NÚMERO MÉDIO DE IMIGRANTES PARA CADA MÊS
def media_mes(data_frame):
    media = data_frame['QTD'].mean()
    return media

media_mes(df_janeiro)