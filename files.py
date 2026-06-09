total = float(input('insira o valor da sua conta: '))

gorjeta= float (input("insira a porcentagem da gorjeta: "))

novoTotal= total * gorjeta /100 + total

clientes= int(input("insira enquantas pessoas vc ira dividir: "))

valorIndividual= novoTotal / clientes

print("R$" + str(novoTotal))
print("R$" + str(valorIndividual))