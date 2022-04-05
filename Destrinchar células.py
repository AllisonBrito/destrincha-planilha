import pandas as pd
import PySimpleGUI as sg

def separa_nome(caminho):
  separa_extensao = caminho.split('.')
  separa_barra = separa_extensao[0].split('/')
  return separa_barra[-1]

sg.theme('Dark Blue 3')
caminho_planilha = sg.popup_get_file('Defina o caminho da planilha')

nome_arquivo = separa_nome(caminho_planilha)

planilha_dataframe = pd.read_excel(caminho_planilha)

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

planilha_refaturada.to_excel(f'{nome_arquivo} v2.xlsx', sheet_name='DADOS')

sg.popup('Arquivo salvo!)
