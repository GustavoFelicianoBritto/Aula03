num = int(input("Digite o valor referente ao mês: "))

if num > 12 or num <1:
    print("Número inválido")

else:
    if num == 1:
        print("Janeiro")
    elif num ==2:
        print("Fevereiro")
    elif num == 3:
        print("Março")
    elif num == 4:
        print("Abril")
    elif num == 5:
        print("Maio")
    elif num == 6:
        print("Junho")
    elif num == 7:
        print("julho")
    elif num == 8:
        print("Agosto")
    elif num == 9:
        print("Setembro")
    elif num == 10:
        print("Outubro")
    elif num == 11:
        print("Novembro")
    else:
        print("Dezembro")


numSemana=int(input("Digite um número referente ao dia da semana: "))

match numSemana:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Valor inválido")




