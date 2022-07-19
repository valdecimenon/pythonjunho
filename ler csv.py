#ler_crv.py

import csv

ARQUIVO = 'D:\\Python aluno Carlos Margraf\\Aula 4\\Planilha.csv'


with open(ARQUIVO, encoding= 'utf+8') as f:
    tabela = csv.reader(f)
    for linha in tabela:
        print(linha)

