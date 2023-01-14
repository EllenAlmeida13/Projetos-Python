"""
 Título: Lab 4 - Exercício 10
 Função: Ler o salário atual, o percentual de aumento e imprimir
         o valor do aumento e o novo salário
 Autora: Ruth Ellen
 Data: 18/11/2020
"""

#Entrada de Dados

s = float(input("Digite o Salário Atual: "))
p = float(input("Digite o Percentual de aumento: "))

#Cálculo e Saída de Dados

a = s * p/100
ns = s + a

print("Valor do Aumento: ",a)
print("Novo Salário: ",ns)

print("Fim do programa")
