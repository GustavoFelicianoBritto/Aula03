horas=[14,5]
minutos=[57,44]

for i in range (len(horas)):
    if horas[i] > 12:
        horas [i] -=12

totalHoras= horas[0] + horas[1]
totalMinutos = minutos[0] + minutos[1]

if totalMinutos > 59:
    totalHoras+=1
    totalMinutos -=60

if totalHoras>12:
    totalHoras-=12

print(f"{totalHoras}:{totalMinutos:02d} PM")
