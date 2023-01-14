"""
 Título: Lab 4 - Exercício 3
 Função:  Ler uma temperatura em Celsius e fazer
          a conversão para Kelvin e Fahrenheit
 Autora: Ruth Ellen
 Data: 17/11/2020
"""

#Entrada de Dados

c = float(input("Digite Celsius: "))
 
#Saída de Resultados

k = c + 273.15
print("Kelvin: ",k)

f = ((9 * c) / 5) + 32
print("Fahrenheit: ",f)

print("Fim do Programa")
