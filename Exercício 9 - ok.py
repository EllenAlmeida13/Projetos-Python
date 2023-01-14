"""
 Título: Lab 4 - Exercício 9
 Função: Ler o salário atual de um funcionário e mostrar seu
         novo salário que sofreu reajuste de 25%
 Autora: Ruth Ellen
 Data: 18/11/2020
"""

#Entrada de Dados

s = float(input("Digite o Salário Atual: "))

#Cálculo e Saída de Dados

ns = s + (s * 25/100)

print("Novo Salário: ",ns)
print("Fim do programa")
