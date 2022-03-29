import itertools
from operator import le
from numpy import positive
import pandas as pd
from pandas.core.frame import DataFrame
from numpy import positive
import pandas as pd
from pandas.core.frame import DataFrame

def le_planilha():
    while True:
        try:
            caminho_planilha = input('Defina o caminho da planilha: ')
            return pd.read_excel(caminho_planilha)
        except:
            print('Arquivo não encontrado.')

planilha_dataframe = le_planilha()

nome_colunas = planilha_dataframe.columns

dic = {f'{nome_colunas[g]}': [] for g in range(len(nome_colunas))}

for linha in range(len(planilha_dataframe)):
    for coluna in range(len(planilha_dataframe.columns)):
        celula = str(planilha_dataframe.iloc[linha,coluna])
        verifica_quant = str(planilha_dataframe.iloc[linha,0]).count('|') + 1

        celula = celula.split('| ')
        if len(celula) == verifica_quant:
            for item in celula:
                dic[f'{nome_colunas[coluna]}'] += [item.strip()]
        else:
            for quant in range(verifica_quant):
                for item in celula:
                    dic[f'{nome_colunas[coluna]}'] += [item.strip()]
                    break

planilha_refaturada = DataFrame(dic)

planilha_refaturada.to_excel('SUA NOVA TABELA.xlsx', sheet_name='DADOS')

print('Arquivo Salvo!!!')
