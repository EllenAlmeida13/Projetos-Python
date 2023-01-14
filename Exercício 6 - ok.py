"""
 Título: Lab 4 - Exercício 6
 Função: Ler o salário de um funciónario, após alguns ajustes imprimir 
         o salário inicial, com aumento, com desconto e o salário final.
 Autora: Ruth Ellen
 Data: 18/11/2020
"""

#Entrada de Dados

s = float(input("Digite o sálario atual: "))

#Cálculo e Saída de Dados

a = s * 15/100
sa = s + a
d = sa * 8/100
sf = s + (a - d)

print("Salário Inicial: ",s)
print("Salário com Aumento: ",sa)
print("Desconto: ",d)
print("Salário Final: ",sf)

print("Fim do Programa")
