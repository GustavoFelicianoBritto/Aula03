meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
num = int(input("Digite o valor referente ao mês: "))
if num >= 1 and num <=12:
    mes = meses[num-1]
    print(f"O mês é: {mes}")
else:
    print("Número inválido")




