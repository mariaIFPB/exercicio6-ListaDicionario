turmas = {}
programaRodando = 1

def calcularMedia(nota1, nota2):
  matricula = [nota1,nota2]
  media = (nota1 + nota2)/2
  print(media)

def adicionarTurma (turma):
  turmas[turma] = {}

def adicionarAlunoNotas (turma,matricula,nota1,nota2):
  turmas[turma][matricula] = [nota1,nota2]
  
def resultadoFinal ():
  print(turmas)
  
def menu():
  
  print("opções: \n 1. Adicionar turma;\n 2. adicionar aluno e notas;\n 3. Calcular média de um Aluno;\n 4. exibir todas as turmas e seus alunos \n 5. sair")
  
  opcao = int(input("informe sua opção:"))
  if (opcao == 1):
    qturmas = int(input("informe a quantidade de turmas que deseja adicionar: "))
    for y in range (0,qturmas):
      turma = input("informe a sigla da turma (ex: 1BINFO):")
      adicionarTurma(turma)
    adicionarTurma(turma)

  if (opcao == 2):
    turma = input("informe em qual turma deseja adicionar aluno: ")
    if (turma in turmas):
      matricula = int(input("Digite a matrícula do aluno: "))
      global notas
      nota1 = int(input("informe a 1º nota:"))
      nota2 = int(input("informe a 2º nota:"))
      
      adicionarAlunoNotas(turma, matricula, nota1, nota2)
    
  if (opcao == 3):
    turma = input("Digite a turma do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))
    
    calcularMedia(turmas[turma][matricula][0], turmas[turma][matricula][1])
    
  if (opcao == 4):
    resultadoFinal()
    
  if (opcao == 5):
    global programaRodando
    programaRodando = 0
    print("programa finalizado.")

while(programaRodando):
  menu()
