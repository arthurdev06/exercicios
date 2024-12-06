x = int(input("quanto voce ganha por hora trabalhada? "))
y = int(input("quantas voce trabalha por mes? "))
salario = x*y
porcentagem = 0.11+0.08+0.05
liquido = (((salario)*(porcentagem))-(salario))*-1
print(f"seu salario bruto é: {salario}")
print(f"seu salario líquido é: {liquido}")
