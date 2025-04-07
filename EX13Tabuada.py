num = int(input("Digite o número que deseja saber a tabuada: "))
for i in range(1,11,1):
    resultado = (num * i)
    print(f"{i} x {num} = {resultado}") #end=", "
