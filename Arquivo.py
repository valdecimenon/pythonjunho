

ARQUIVO = "D:\\Python aluno Carlos Margraf\\Aula 4\\Planilha.csv"

print()
print('-----------------------------------------------------------')
print('NOME         |    DESCRIÇÃO    |     VALOR   | QUANTIDADE |')
print('-----------------------------------------------------------')
#print(ARQUIVO)

arquivo = open(ARQUIVO, 'r')
imprimir = False

for linha in arquivo:
    lista = linha.split(';')
    if imprimir:
        nome = lista[0]
        desc = lista [1]
        valor = float(lista[2])
        quant = int(lista[3])
        print(f'{nome:12} | {desc:15} | R$ {valor:8.2f} | {quant:5}')

    imprimir = True
    
print('----------------------------------------------------------|')        

arquivo.close()
