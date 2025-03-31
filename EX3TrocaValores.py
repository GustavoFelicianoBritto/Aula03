from time import process_time_ns

A= int(input("Digite o valor para A: "))
B = int(input("Digite o valor para B: "))

print(f"Inicialmente o valor de A era {A}\n"
      f"Inicialmente o valor de B era {B} ")

aux = A
A = B
B= aux

print(f"Agora o valor de A é {A}\n"
      f"Agora o valor de B é {B} ")
