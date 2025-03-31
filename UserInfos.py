#Atividade solicitar nome, idade e salário do usuário


#Recebendo informações básicas
nome = input("Olá, digite seu nome: ")
idade= int(input(f"Olá, {nome}. Digite sua idade: "))
salario=float(input(f"Olá, {nome}. Digite agora seu salário: ").replace(',','.'))



#Calculo do percentual
#Recebo o valor de aumento Ex: 30 (30%)
percentual = float(input("Digite o percentual de aumento: ").replace(',','.'))

#Valor do aumento Ex: 100/100*30%
aumento = (salario/100)*percentual

#soma do aumento com o salário atual
novosalario = salario + aumento

print(f"Nome: {nome}\n"
      f"Idade: {idade} anos\n"
      f"salário: R$ {salario:.2f}")

print(f"O novo salário de {nome} com aumento de {percentual}% é: {novosalario:.2f}")