tipoCombustivel = ""
total= 0
litros= float(input("Digite a quantidade de litros: ").replace(',','.'))
combustivelAtual= ""
gasolina=5.80
etanol = 4.90

while tipoCombustivel != "e" and  tipoCombustivel != "E" and tipoCombustivel != "g" and tipoCombustivel != "G":

    #print(tipoCombustivel)
    tipoCombustivel = input("Escolha o tipo do combustível\n E - Etanol, G - Gasolina: ")


    if tipoCombustivel == "e" or tipoCombustivel=="E":
        print("Etanol selecionado")
        total = litros* etanol
        combustivelAtual = "Etanol"

    elif tipoCombustivel == "g" or tipoCombustivel== "G":
        print("Gasolina selecionada")
        total = litros * gasolina
        combustivelAtual = "Gasolina"

    else:
        print("Opção inválida, insira novamente")

print(f"O valor total da sua compra é: R$ {total:.2f}\nTipo: {combustivelAtual}\nQuantidade: {litros} litros")


