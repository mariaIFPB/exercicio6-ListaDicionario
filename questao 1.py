"""
Crie um programa em python para cadastrar os dias da semana em um
dicionário. Cada dia da semana deverá ser identificado por uma chave
ordinal que começará em 1 (domingo) e finalizará em 7 (sábado), o
valor deverá ser o nome do dia. Para isso, defina duas funções
adicionarDia(posicao, dia) e exibirDias(dias).
"""
dias = dict()

def adicionarDia(posicao, dia):
  dias[posicao] = dia

for i in range (0,7):
  posicao = int(input("informe um valor: "))
  dia = input("informe o dia: ")
  adicionarDia(posicao,dia)
  
def exibirDias(dias):
  for x in dias:
    print ( x,":", dias[x])
    
exibirDias(dias)
