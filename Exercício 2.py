"""
 Título: Lab 4 - Exercício 2
 Função: Ler o valor das quatro variáveis
         e calcular x e y a partir da equação dada
 Autora: Ruth Ellen
 Data: 17/11/2020
"""

#Entrada de Dados

a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
d = float(input("Digite d: "))

p = 3.141592

#Saída do Resultado

x = (b / (a + c) + 4 * a - p) / ((d - 2 * a) / (3 + c))
print("x: ",x)

y = (p - b**3 - 4 * a *c + 2 * a**2) / (2 * a/(b + 1)**2)
print("y: ",y)

print("Fim do Programa")
