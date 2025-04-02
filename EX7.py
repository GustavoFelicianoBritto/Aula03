tipoCombustivel = ""
total= 0
litros= float(input("Digite a quantidade de litros: ").replace(',','.'))
combustivelAtual= ""
gasolina=5.80
etanol = 4.90

while tipoCombustivel != "e" and tipoCombustivel != "g":

    tipoCombustivel = input("Escolha o tipo do combustível\n E - Etanol, G - Gasolina: ").lower()


    if tipoCombustivel == "e":
        print("Etanol selecionado")
        total = litros* etanol
        combustivelAtual = "Etanol"

    elif tipoCombustivel == "g":
        print("Gasolina selecionada")
        total = litros * gasolina
        combustivelAtual = "Gasolina"
    else:
        print("Opção inválida, insira novamente")

print(f"O valor total da sua compra é: R$ {total:.2f}\nTipo: {combustivelAtual}\nQuantidade: {litros} litros")


