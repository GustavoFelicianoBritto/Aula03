nota1=float(input("Digite a primeira nota: ").replace(',','.'))
nota2=float(input("Digite a segunda nota: ").replace(',','.'))
nota3=float(input("Digite a terceira nota: ").replace(',','.'))

media = (nota1+nota2+nota3)/3

if media>=7.0:
    print(f"Parabéns, aluno aprovado. Nota:{media:.2f}")
elif(media >=4.0):
    print(f"Aluno em recuperação. Nota: {media:.2f}")
else:
    print(f"Aluno reprovado. Nota:{media:.2f}")

