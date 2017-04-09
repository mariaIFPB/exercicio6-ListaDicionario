"""
Crie um programa em python para cadastrar os funcionários de uma
empresa. Cada funcionário é identificado por sua matrícula e nome.
Para isso, defina três funções adicionarFuncionario(matricula, nome),
buscarFuncionario(matricula) e exibirFuncionarios(funcionarios).
"""
def adicionarFuncionario(matricula, nome):
  funcionarios[matricula] = nome

def buscarFuncionario(matricula):
  buscar = funcionarios[matricula]
  print (buscar)
  
def exibirFuncionarios(funcionarios):
  for matricula in (funcionarios):
    print ( matricula,":", funcionarios[matricula])

while True:
  funcionarios = dict()
  qfunc = int(input("digite a quantidade de funcionários na empresa: "))
  
  if (qfunc != 0):
    for i in range (0,qfunc):
      matricula = eval(input("informe a matricula: "))
      nome = input("informe o nome: ")
      adicionarFuncionario(matricula,nome)
    adicionarFuncionario(matricula,nome)
    bF = input(("você deseja buscar algum funcionário?(sim ou nao)"))
    if (bF == "sim"):
      matricula = input("informe a matricula do funcionario que deseja encontrar: ")  
      buscarFuncionario(matricula)
    if(bF == "sim" or bF == "nao" ):
      historicoFunc = input("você deseja olhar seu histórico de funcionários?(sim ou nao)")
      if (historicoFunc == "sim"):
        exibirFuncionarios(funcionarios)

  else:
    print("programa finalisado! obrigado e volte sempre!")
    break
