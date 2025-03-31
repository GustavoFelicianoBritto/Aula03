print("Bem vindo a tabuada das quatro operações")
num1=float(input("Digite o primeiro valor: "))
num2= float(input("Digite o segundo valor: "))

soma= num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2

print(f"Resultado:\n"
      f"{num1}+{num2} = {soma}\n"
      f"{num1}-{num2} = {sub}\n"
      f"{num1}*{num2} = {mult}\n"
      f"{num1}/{num2} = {div:.2f}")