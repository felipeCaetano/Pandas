import pandas as pd
import numpy as np

"""
Lendo e Reconhecendo os dados
"""
data_frame = pd.read_csv('speeddatting.csv', low_memory=False, sep=';')
#limpando um pouco o data_frame:
del data_frame['has_null']
del data_frame['wave']

#olhando as primeiras linhas
print(data_frame.head())

#quantas observações existem no data set?
print()
print(data_frame.info()) #data_frame.shape[0]

#quantas colunas existem no data set?
print('\nNumero de Colunas')
print(data_frame.shape[1])

#exibindo os nomes das colunas
print("\nNome das Colunas")
print(data_frame.columns)

#Como o data set está indexado?
print("\nPara indexar uma linha:")
print(data_frame.index)

# #Quais os raças litstadas?
print(data_frame.race.unique())
print(len(data_frame.race.unique()))
#
# #Quantos anos tem os participantes?:
print("\nQuantas idades diferentes tem os participantes?")
print(data_frame.age.nunique())
#
# #Descrição da coluna idade:
print("\nDescrição da coluna idade")
print(data_frame.age.describe())
#
# #Quantas ocorrencias de cada idade?
print("\nQuais ocorrencias de cada idade:")
idades = data_frame.age.sort_index()
#trocando o ? por 0
for i,v in enumerate(idades.values):
    if v == '?':
        idades.values[i] = '0'

print(idades.value_counts().sort_index())
print(f'\nValor mediano das idades é {data_frame.age.unique().median()}')
#
# #Descrição das colunas numericas
# #Descrição da destribuição das idades:
print("\nDescrição da destribuição das idades:")
print(idades.value_counts().describe())
#
# Como está a distribuição pelos sexos?
print("\nOs generos estáo assim destribuídos:")
genero = data_frame.groupby("gender")
print(genero.head())
print(f'\nExistem {len(genero)} diferente(s) genero(s)')

#
#print(genero.age)
# #Mostrando BSI de Recife:
# print('\nEstudantes de Direito do Recife:')
# print(data_frame[(data_frame['MUNICIPIO_BENEFICIARIO_BOLSA']=='RECIFE') & (data_frame['NOME_CURSO_BOLSA']=='Direito')])
