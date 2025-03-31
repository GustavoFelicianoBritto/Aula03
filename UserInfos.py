#Atividade solicitar nome, idade e salário do usuário

nome = input("Olá, digite seu nome: ")
idade= int(input(f"Olá, {nome}. Digite sua idade: "))
salario=float(input(f"Olá, {nome}. Digite agora seu salário: ").replace(',','.'))

print(f"Nome: {nome}\n"
      f"Idade: {idade} anos\n"
      f"salário: R$ {salario:.2f}")
