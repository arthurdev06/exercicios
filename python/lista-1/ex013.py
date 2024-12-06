h = float(input('qual é a sua altura? '))
g = input("qual seu genero? M para masculino F para feminino ")

if g == "M":
  print(f" seu peso ideal é: {(72.7*h) - 58}") 
else:
  print(f" seu peso ideal é: {(62.1*h) - 44.7}") 