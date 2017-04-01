produtos = {}

programaRodando = 1

def cadastrarProduto(produtos, produto, preco):
  produtos[produto] = preco

def exibirProdutos(produtos):
  for produto in (produtos):
      print (produto)

def removerProduto (produtos, produto):
  remover = produtos.pop(produto)
  print ("produto de valor ",remover,"removido com sucesso!")

def exibirCaroProduto(produtos):
  print ("o produto mais caro é ", max(produtos, key=produtos.get))

def exibirBaratoProduto(produtos):
  b = print ("o produto mais barato é :", min(produtos, key=produtos.get))

def menu():
  
  print("opções: \n 1. Adicionar Produto;\n 2. Listar Produtos;\n 3. Remover Produto;\n 4. Exibir o mais caro;\n 5. exibir o mais barato \n 6. sair")
  
  opcao = int(input("informe o numero da opção que você deseja executar:"))
  
  if (opcao == 1):
    produto = input("informe o nome do produto: ")
    preco = eval(input("informe o preço do produto: "))
    cadastrarProduto(produtos, produto, preco)
  
  if (opcao == 2 ):
    exibirProdutos(produtos)
  
  if (opcao == 3):
    produto = input(("informe qual produto deseja remover: "))
    removerProduto (produtos, produto)
    
  if (opcao == 4):
    exibirCaroProduto(produtos)
  
  if (opcao == 5):
    exibirBaratoProduto(produtos)
    
  if (opcao == 6):
    global programaRodando
    programaRodando = 0
    print("programa finalizado.")

while(programaRodando):
  menu()
