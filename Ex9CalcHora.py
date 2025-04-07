#soma > entrada no padrão de horas > padrão 12horas por dia
#declarei variaveis temporaveis
hora=[15,45]
hora2=[22,20]

horasaida=[0,0]
resto=0
#-------------------
#somei horas e minutos

somaHora= hora[0]+hora2[0]
somaminuto=hora[1]+hora2[1]

horafinal=[0,0]

#----------------------

if somaminuto>59:
    resto = somaminuto%60
    somaHora+=1
    somaminuto=resto
    #print(resto)
    horafinal[1] = resto
    #horasaida=[somaHora,somaminuto]
else:
    #print(somaminuto)
    horafinal[1]=somaminuto



#-------------------------------------
horafinal[0]=somaHora
#print(horafinal)
if somaHora>24:
    horafinal[0] = (somaHora - 24)
else:
    if somaHora>12:
        horafinal[0] = (somaHora - 12)
    #erro

    else:
        horafinal[0]=somaHora


if horafinal[0]>12:
    horafinal[0]-=12



#----------------------------
if horafinal[0]<0:
    horafinal[0]=horafinal[0]*-1

print(f"Hora saída: {horafinal[0]}:{horafinal[1]}")






