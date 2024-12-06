x = float(input("Quanto pesam os peixes? "))
m = 50.0

if x > m:
  a = (x-m) 
  print(f"o excesso é: {a} e voce vai ter que pagar R${a*4} pelo peso excedente")
else:
  print("voce esta dentro do limite")
