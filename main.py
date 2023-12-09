import os 
import datetime
import pickle

###Para colocar cor no texto
vermelho = '\033[1;31m'
verde = '\033[92m'
roxo = '\033[95m'
res_cor = '\033[0m'
###codigos de cores retirados do site de inteligencia artificial ChatGPT

f1 = '|AÇAITERIA MAIS SABOR|'
f2 = '  *Self service*'
f3 = '____________________MENU PRINCIPAL____________________'
f4 = '__________________PRODUTOS__________________'
f5 = '___________________VENDAS___________________'
f6 = '__________________FUNCIONÁRIOS__________________'
f7 = '__________________SENHA__________________'




produtos= {} ##dicionário para colocar produtos, preços e estoque 
vendas = {} ##para colocar todas as vendas 
funcionarios = {} #para colocar dados dos funcionários
dia = {} ### salvar as vendas do dia para somar no final do dia(não entra no arquivo)






try:   #recuperar os arquivos 
  arqacaiteria = open("acaiteria.dat", "rb")
  acai = pickle.load(arqacaiteria)
  produtos = acai[1]
  vendas = acai[2]
  funcionarios = acai[3]
  arqacaiteria.close()
except:
  arqacaiteria = open("acaiteria.dat", "wb")
  arqacaiteria.close()
  
def salvar():
  acai = {
  1:produtos,
  2:vendas,
  3:funcionarios,
}
  arqacaiteria = open("acaiteria.dat", "wb")  
  pickle.dump(acai, arqacaiteria)
  arqacaiteria.close()


###Para gerar id
arqacaiteria = open('acaiteria.dat', 'rb')
acai = pickle.load(arqacaiteria)
vendas = acai[2]

   
def validaCPF(cpf):
  tam = len(cpf)
  soma = 0
  d1 = 0
  d2 = 0
  if tam != 11:
    return False
  for i in range(11):
    if (cpf[i] < '0') or (cpf[i] > '9'):
      return False
  for i in range(9):
    soma += (int(cpf[i]) * (10 - i))
  d1 = 11 - (soma % 11)
  if (d1 == 10 or d1 == 11):
    d1 = 0
  if d1 != int(cpf[9]):
    return False
  soma = 0
  for i in range(10):
    soma += (int(cpf[i]) * (11 - i))
  d2 = 11 - (soma%11)
  if (d2 == 10 or d2 == 11):
    d2 = 0
  if d2 != int(cpf[10]):
    return False
  return True

###funcão validaCPF retirado do codigo de - Flavius Gorgonio. Replit.2020-Disponivel em <https://replit.com/@flaviusgorgonio/ValidaCPF?v=1>

print(roxo+ "==============================================="+ res_cor)
print(verde + "=================" + res_cor, vermelho +"INFORMAÇÃO"+res_cor, verde + "=================="+ res_cor)
print(" Esse projeto foi desenvolvido para simular um")
print("sistema de gestão dentro de uma açaiteria. Nem \ntodos os colaboradores forneceram códigos para \no programa, porém, ajudaram no desenvolvimento, \nderam idéias ou ajudaram a resoluciar algum \nproblema.   ")
print(roxo+"==============================================="+ res_cor)
print(" Autora: MARIA CECILIA DANTAS DE MORAIS ")
print (" Colab.: Gabriel Vieira ")
print(" Colab.: Matheus Diniz ")
print(" Colab.: Maxuel Gadelha ")
print(" Colab.: Flavius Gorgônio  ")
print(" Colab.: ChatGPT ")
print(roxo+"==============================================="+res_cor)

print()

continuar= input('Tecle ENTER para continuar')
os.system('clear || cls')

def inicio():
  frase_1 = (roxo + f1 + res_cor)
  frase_2 = verde + f2 + res_cor
  print(verde + '               ____________________' + res_cor)
  print()
  print("             ", frase_1)
  print("               ", frase_2)
  print(roxo + '               ____________________' + res_cor)
  print()
  print()


inicio()


def tela_1():
  mp = (roxo + f3 + res_cor)
  os.system("clear || cls")
  print()
  inicio()
  print()
  print(mp)
  print('Tecle "1" se deseja consultar a área de produtos' )
  print('Tecle "2" se deseja consultar a área de vendas')
  print('Tecle "3" se deseja consultar a área de funcionários')
  print('Tecle "4" se deseja consultar a área de senha')
  print('Tecle "0" se deseja sair do programa')
  print(verde + "_____________________________________________________" + res_cor)
  print()
  
def t_prod():
  pd = (roxo + f4 + res_cor)
  os.system("clear || cls")
  print()
  inicio()
  print()
  print(pd)
  print('Tecle "1" se deseja cadastrar um produto')
  print('Tecle "2" se deseja consultar um produto')
  print('Tecle "3" se deseja atualizar um produto')
  print('Tecle "4" se deseja deletar um produto')
  print('Tecle "5" se deseja listar todos os produtos')
  print('Tecle "6" se deseja deletar todos os produtos')
  print('Tecle "0" se deseja sair de produtos')
  print(verde + "____________________________________________" + res_cor)
  print()

def t_vendas():
  vd = (roxo + f5 + res_cor)
  os.system("clear || cls")
  print()
  inicio()
  print()
  print(vd)
  print('Tecle "1" se deseja cadastrar uma venda')
  print('Tecle "2" se deseja consultar uma venda')
  print('Tecle "3" se deseja atualizar uma venda')
  print('Tecle "4" se deseja deletar uma venda')
  print('Tecle "5" se deseja listar todas as vendas')
  print('Tecle "0" se deseja sair de vendas')
  print(verde + "_________________________________________"+ res_cor)
  print()

def t_func():
  fc = (roxo + f6 + res_cor)
  os.system("clear || cls")
  print()
  inicio()
  print()
  print(fc)
  print('Tecle "1" se deseja cadastrar um funcionários')
  print('Tecle "2" se deseja consultar um funcionários')
  print('Tecle "3" se deseja atualizar um funcionários')
  print('Tecle "4" se deseja deletar um funcionário')
  print('Tecle "5" se deseja listar todos os funcionários')
  print('Tecle "0" se deseja sair de funcionários')
  print(verde + "_______________________________________________" + res_cor)
  print()

def senha_alt():
  vd = (roxo + f7 + res_cor)
  os.system("clear || cls")
  print()
  inicio()
  print()
  print(vd)
  print('Tecle "1" para atualizar a atual senha')
  print('Tecle "2" para consultar a atual senha')
  print('Tecle "0" para sair de senhas')
  print(verde + "_________________________________________"+ res_cor)
  print()
 

def unidade():
  x = int(input('Digite a quantidade de produtos vendidos: '))
  print()
  if x > produtos[produto][1]:
    print(vermelho + 'Quantidade maior que o estoque disponível!! ' + res_cor)
    print()

  else:   
    total = produtos[produto][0] * x
    print("total: R$%.2f" %total)
    print()
    pergunta = input("Deseja dar desconto ao cliente? ")
    print()
    pergunta = pergunta.upper()
    if pergunta == "SIM":
      des = float(input('Digite a porcentagem do desconto: '))
      desconto = total * des/100
      total_des = total - desconto
      estoque = produtos[produto][1] - x
      dia[total] = total_des
      if not bool(vendas):
        vendas[1]=[1, da, produto, x, chave, total_des, func_resp]
        produtos[produto][1] = estoque - x
        dia[1] = total_des
        salvar()
  

      else:
        ultima_chave = list(vendas.keys())[-1]
        id = ultima_chave + 1
        vendas[id]= [id, da, produto, x, total_des, func_resp]
        produtos[produto][1] = estoque - x
        dia[id] = total_des
        salvar()

      print('Total: R$%.2f' %total_des)
      print()
      print('Venda cadastrada com sucesso!')
      print()

    else:
      total = produtos[produto][0] * x
      estoque = produtos[produto][1] - x
      if not bool(vendas):
        vendas[1]=[1, da, produto, x, total, func_resp ]
        produtos[produto][1] = estoque - x
        dia[1] = total 
        salvar()  

      else:
        ultima_chave = list(vendas.keys())[-1]
        id = ultima_chave + 1
        vendas[id]= [id, da, produto, x, total, func_resp]
        dia[id] = total 
      
      salvar()
      print('Total: R$%.2f' %total)
      print()
      print('Venda cadastrada com sucesso!')
      print()



def peso():
  valores = float(input('Digite o peso do produto: '))
  print()
  if valores > produtos[produto][1]:
    print(vermelho + 'Quantidade maior que o estoque disponível!! ' + res_cor)
    print()

  else:  
    total = produtos[produto][0] * valores
    print("Total: R$%.2f" %total)
    print()
    pergunta = input("Deseja dar desconto ao cliente? ")
    print()
    pergunta = pergunta.upper()
    if pergunta == "SIM" or pergunta == "S":
      des = float(input('Digite a porcentagem do desconto: '))
      print()
      desconto = total * des/100
      total_des = total - desconto
      estoque = produtos[produto][1] - valores
      if not bool(vendas):
        vendas[1] = [1, da, produto, valores, total_des, func_resp]
        dia[1] = total_des
        salvar()

      else:
        ultima_chave = list(vendas.keys())[-1]
        id = ultima_chave + 1
        vendas[id]= [id, da, produto, valores, total_des, func_resp]
        dia[id] = total_des
      
      produtos[produto][1] = estoque - valores
  
      salvar()           
      print('Total: R$%.2f' %total_des)
      print()
      print(verde + 'Venda cadastrada com sucesso! ' + res_cor)

    else:
      estoque = produtos[produto][1] - valores
      if not bool(vendas):
        vendas[1] = [1, da, produto, valores, total, func_resp]
        dia[1] = total
        salvar()

      else:
        ultima_chave = list(vendas.keys())[-1]
        id = ultima_chave + 1
        vendas[id]= [id, da, produto, valores, total, func_resp]
        dia[id] = total 
      
      salvar()           
      print('Total: R$%.2f' %total)
      print()
      print(verde + 'Venda cadastrada com sucesso! ' + res_cor)
  

      


senha = ['1234']
p_senha = input('Digite a senha de acesso: ')



while p_senha != senha[0]:
  if p_senha == senha:
    print(verde + '        Bem vindo, caro usuário!' + res_cor)
    print()

  else:
    print(vermelho + 'Senha incorreta, tente novamente!'+ res_cor)
    print()
    p_senha = input('Digite a senha de acesso:')
print()
print(verde + 'Bem vindo, caro usuário!' + res_cor)
print()
continuar = input("Tecle ENTER para continuar")
os.system("clear || cls")
inicio()
os.system("clear || cls")

inicio()
caixa = float(input('Digite o caixa inicial: '))

menu_principal = 5

while menu_principal != '0':
  tela_1() 
  menu_principal = input('O que você deseja consultar?  ')
  print()
  ##para produtos
  if menu_principal == '1':
    tela_1()
    t_prod()
    produtos_p = '7'
    while produtos_p != '0':
      produtos_p = input('Digite o número desejado:  ')
      print()
      if produtos_p == '1':
        prod = True
        while prod:
          produto = input('Digite o nome do produto: ')
          print()
          produto = produto.upper()
          if produto not in produtos:
            valor = float(input('Qual o preço do produto a ser cadastrado? '))
            print()
            estoque = float(input('Qual o estoque do produto a ser cadastrado? '))
            print()
            produtos[produto] = [valor, estoque]
            salvar()
            print('Produto %s cadastrado com sucesso!' % produto.capitalize())
            print()
            prod = False
            
          else:
            
            print('Produto já cadastrado!')
            print()
  
      elif produtos_p == '2':
      
        produto = input("Qual produto quer consultar? ")
        print()
        produto = produto.upper()
        print()
        if produto in produtos:
          if produto == "MILK SHAKE" or produto == "MILK-SHAKE":
            print("Informações sobre o %s: R$ %.2f, %.1f Unidades" % (produto.capitalize(), produtos[produto][0], produtos[produto][1]))
            print()

          elif produto == "SORVETE":
            print("Informações sobre o %s: R$ %.2f, %.1f Kg" % (produto.capitalize(), produtos[produto][0], produtos[produto][1]))
            print()

          elif produto == "AÇAI" or produto== "AÇAÍ":
            print("Informações sobre o %s: R$ %.2f, %.1f Kg" % (produto.capitalize(), produtos[produto][0], produtos[produto][1]))


          
          else:
            print("Informações sobre o %s: R$ %.2f, %.1f unidades" % (produto.capitalize(), produtos[produto][0], produtos[produto][1]))
            
        else:
          print("Produto %s não está cadastrado!" % produto.capitalize())
          print()
    
      elif produtos_p == '3':
      
        produto = input('Qual produto quer alterar? ')
        print()
        produto = produto.upper()
        if produto in produtos:
          valores = float(input('Qual o novo preço desse produto? '))
          produtos[produto][0] = valores
          print()
          estoque = float(input('Qual o novo estoque desse produto? '))
          produtos[produto][1] = estoque
          salvar()
          print()
          print('Produto %s cadastrado com sucesso' % produto.capitalize())
          print()
        else:
          print('Produto %s não está cadastrado!' % produto.capitalize())
          print()
    
      elif produtos_p == '4':
      
        produto = input('Qual produto quer excluir? ')
        produto = produto.upper()
        print()
        if produto in produtos:
          del produtos[produto]
          salvar()
          print()
          print('Produto %s excluido com sucesso' % produto.capitalize())
          print()
        else:
          print('Produto %s não está cadastrado!' % produto.capitalize())
          print()

      elif produtos_p == '5':
        for chave in produtos:
          for conteudo in produtos[chave]:
            print("Produto: %s" %  chave.capitalize(),"\nPreço: R$%.2f" % produtos[chave][0],"\nEstoque: %.1f " %produtos[chave][1])
            print()
            break

      elif produtos_p == '6':
        perg = input('Tem certeza que quer excluir todos os produtos? ')
        perg = perg.upper()
        print()
        if perg == 'SIM' or perg == 'S':
          del produtos
          print("Todos os produtos foram excluídos com sucesso! ")
          

        else:
          print()
  
      elif produtos_p == '0':
        break
     
      else:
        print('Digite um número válido')
        print()

      print()
      produtos_p = input('Tecle ENTER para reiniciar')
      os.system("clear || cls")
      tela_1()
      t_prod()
      
  ##para vendas
  
  elif menu_principal == '2':
    tela_1()
    t_vendas()
    vendas_p = '4'
    while vendas_p != '0':
      vendas_p = input('Digite o número desejado: ')
      print()
      if vendas_p == '1':
        chave_fd = int(input("Digite sua chave de acesso como funcionário: "))
        print() 
        if chave_fd in funcionarios:
          func_resp = funcionarios[chave_fd][1]
          produto = input('Qual o produto vendido? ')
          print()
          produto = produto.upper()
          da = datetime.datetime.now().strftime("%d/%m/%Y")
          if produto in produtos:
            if produto == "MILK-SHAKE" or produto == "MILK SHAKE":
              unidade()
              
            elif produto == "AÇAI" or produto == "AÇAÍ":
              peso()
                  
            elif produto == "SORVETE":
              peso()
    
            else:
              unidade()
          else:
            print()
            print('Esse produto não está cadastrado!')
            print()

        else:
          print('Chave de acesso não cadastrada!')
          print()

      elif vendas_p == '2':
        chave = int(input("Qual venda quer consultar?(digite o ID da venda)  "))
        print()
        if chave in vendas:
          print('Data da venda: ', vendas[chave][1])
          print('ID da venda: ', vendas[chave][0])
          print("Nome do produto: " , vendas[chave][2])
          print('Quantidade do produto: ', vendas[chave][3])
          print('Valor da venda: R$%.2f' %vendas[chave][4])
          print('Funcionário Responsável: ', vendas[chave][5])
          
          print()

        else:
          print('Venda não cadastrada')
          print()
        
      elif vendas_p == '3':
        chave = int(input('Qual venda quer alterar(digite o ID da venda) ? '))
        print()
        if chave in vendas:
          x = int(input('Digite "1" para alterar preço ou "2" para alterar a quantidade! '))
          if x == 1:
            print()
            valores = float(input('Qual o novo preço dessa venda? '))
            da = datetime.datetime.now().strftime("%d/%m/%Y")
            valores = vendas[chave][5]
            dia[da]
            salvar()
            print()
            print(verde + 'Venda cadastrada com sucesso! ' + res_cor)

          elif x == 2:
            print()
            quantidade = float(input('Qual a nova quantidade dessa venda? '))
            da = datetime.datetime.now().strftime("%d/%m/%Y")
            quantidade = vendas[chave][4]
            
            salvar()
            print()
            print('Venda cadastrada com sucesso!')
            print()
            
            
        else:
          print('Venda %s não está cadastrada!' % chave)
          print()
    
      elif vendas_p == '4':
        chave = int(input('Qual venda quer excluir(digite o ID)? '))
        print()
        if chave in vendas:
          del vendas[chave]
          salvar()
          print()
          print('Venda %s excluida com sucesso' % chave)
          print()
        else:
          print('Venda %s não encontrada! ' % chave)
          print()

      elif vendas_p == '5':
        for chave in vendas:
          for conteudo in vendas[chave]:
            print('Data da venda: ', vendas[chave][1])
            print('ID da venda: ', vendas[chave][0])
            print("Nome do produto: " , vendas[chave][2])
            print('Quantidade do produto: ', vendas[chave][3])
            print('Valor da venda: R$%.2f' %vendas[chave][4])
            print('Funcionário Responsável: ', vendas[chave][5])
            print()
            break

      elif vendas_p == '0':
        break
      
      else: 
        print('Digite um número válido')
        print()

      vendas_p  = input('Tecle ENTER para reiniciar')
      os.system("clear || cls")
      tela_1()
      t_vendas()
  
  ##para funcionários
  
  elif menu_principal == '3':
    tela_1()
    t_func()
    funcionarios_p = '4'
    while funcionarios_p != '0':
      funcionarios_p = input('Digite o número desejado: ')
      print()
      if funcionarios_p == '1':
        nome = input('Digite o nome do funcionário: ')
        print()
        nome = nome.upper()
        chave = int(input('Digite uma chave de acesso para esse funcionário(utilize números): '))
        print()
        while chave in funcionarios:
          if chave not in funcionarios:
            print('Chave cadastrada com sucesso! ')
            print()
            
          else:
            print('Essa chave ja está sendo utilizada!')
            print()
            chave = int(input('Digite uma chave de acesso para esse funcionário(utilize números): '))
            print()
            
            
        funci = True
        while funci:
          cpf = input('Qual o CPF do funcionário? ')
          print()
          validaCPF(cpf)
          cpf = cpf.replace('.', '')
          cpf = cpf.replace('-', '')
          cpf = cpf.replace(' ', '')
          if validaCPF(cpf):
            print("CPF Ok!")
            print()
            funci=False
          else:
            print("CPF Inválido!")
            print()
    
        idade = input('Digite a idade do funcionário: ')
        print()
        funcionarios[chave] = [chave, nome, cpf, idade]
        salvar()
        print('Funcionário %s cadastrado com sucesso' % nome)
        print()
          
          
      elif funcionarios_p == '2':
        chave = int(input("Qual a chave de acesso do funcionário? "))
        print()
        if chave in funcionarios:
          print("Dados do funcionário")
          print('Chave de acesso: ', funcionarios[chave][0])
          print('NOME COMPLETO: ', funcionarios[chave][1])
          print('CPF: ', funcionarios[chave][2])
          print('Idade do funcionário: ', funcionarios[chave][3])
          print()
        else:
          print("Funcionário não está cadastrado!")
          print()
        
      elif funcionarios_p == '3':
        chave = int(input('Informe a chave de cadastro do funcionário? '))
        print()
        opcao = int(input('Digite "1" para alterar o CPF ou "2" para alterar a idade? '))
        print()
        funci=True
        if chave in funcionarios:
          if opcao == 2:
              while funci:
                idade = input('Qual a nova idade desse funcionário? ')
                print()
                funcionarios[chave][2] = idade
                salvar()
    
                print()
                print('Idade %s cadastrado com sucesso!'%idade)
                print()
                funci=False
          
          else:
              funci=True
              while funci:
                cpf = input('Qual o CPF do funcionário? ')
                print()
                validaCPF(cpf)
                cpf = cpf.replace('.', '')
                cpf = cpf.replace('-', '')
                cpf = cpf.replace(' ', '')
                if validaCPF(cpf):
                  print("CPF Ok!")
                  print()
                  funci=False
                else:
                  print("CPF Inválido!")
                  print()
                  
                funcionarios[chave][1] = cpf
                salvar()
    
                print()
                print('CPF %s cadastrado com sucesso!' % cpf.capitalize())
                print()
    
        else:
          print('Funcionário não cadastrado! ')
          print()
          
    
      elif funcionarios_p == '4':
      
        chave = int(input('Digite a chave de acesso do funcionário: '))
        print()
        if chave in funcionarios:
          escolha = int(input('Deseja mesmo excluir o funcionário %s? (tecle "1" para sim e "2" para não?' % funcionarios[chave][1]))
          print()
          if escolha == 1:
            del funcionarios[chave]
            salvar()
            print()
            print('Funcionário excluido com sucesso')
            print()

          else:
            print('Ação cancelada com sucesso!')
            print()
            
        else:
          print('Funcionário não está cadastrado!')
          print()

      elif funcionarios_p == '5':
        for chave in funcionarios:
          for conteudo in funcionarios[chave]:
            print("Chave de acesso: ", funcionarios[chave][0], "\nFuncionário: ", funcionarios[chave][1], "\nCPF: " , funcionarios[chave][2], "\nIdade: ", funcionarios[chave][3])       
            print()
            break
          
      elif funcionarios_p == '0':
        break
      
      else:
        print('Digite um número válido')
        print()
    
      funcionarios_p = input('Tecle ENTER para reiniciar')
      os.system("clear || cls")
      tela_1()
      t_func()

  
  elif menu_principal == '4':
    senha_alt()
    senhas = '3'
    while senhas != '0':
      senhap = input('Digite o número desejado: ')
      if senhap == '1':
        nova_senha = input('Digite a nova senha: ')
        nova_senha2 = input('Digite a senha novamente: ')
        if nova_senha2 != nova_senha:
          print('Senhas não correspondem! ')
  
        else:
          senha[0] = nova_senha2
          print('Senha cadastrada com sucesso!')
  
      elif senhap == '2':
        print ()
        print("Senha atual: ", senha[0])
        print()
  
      elif senhap == '0':
        break
  
      else: 
        print('Digite um número válido!')
        

      continuar = input("Tecle ENTER para continuar: ")
      os.system("clear || cls")
      inicio()
      senha_alt()
    
  elif menu_principal == '0':
    break
  
  else:
    print('Digite um número válido')
    print()

    


print()
os.system("clear || cls")
inicio()
print()
print(verde + '               ____________________' + res_cor)
print()
print(vermelho + '                 FIM DO PROGRAMA!!'+ res_cor)
print(roxo + '               ____________________' + res_cor)
print()


somad = 0
for valor in dia:
  if isinstance(valor, (int, float)):
    somad += valor
    dia = somad

caixafnl = caixa + dia

print("Total dos produtos vendidos hoje: R$ %.2f " % somad)
print()
print("Valor final em caixa: R$%.2f " % caixafnl)
print()
