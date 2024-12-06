x = float(input("qual é a área em metros quadrados a ser pintada? "))
ln = x/3
preço = 80
litros = 18
  
if ln > litros:
  print(f"voce precisará de {ln/litros} latas e custará {(ln/litros)*preço}")
else:
  print("voce não tem litros sufiscientes para comprar uma lata") 






