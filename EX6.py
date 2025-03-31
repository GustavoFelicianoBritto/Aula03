time1= "Glorioso Santa Cruz FC"
time2="Ixport"
golstime1=int(input(f"Quantidade de gols do {time1}: "))
golstime2=int(input(f"Quantidade de gols do {time2}: "))

if golstime1 > golstime2:
    print(f"O {time1} venceu o {time2}\n{time1} {golstime1} x {golstime2} {time2}!!! \nParabéns {time1}!!!")
elif golstime2 > golstime1:
    print(f"O {time2} venceu o {time1}\n{time2} {golstime2} x {golstime1} {golstime1}!!! \nParabéns {time2}!!!")
else:
    print(f"O jogo acabou EMPATADO!!\n{time1} {golstime1} x {golstime2} {time2}")
