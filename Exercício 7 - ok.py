"""
 Título: Lab 4 - Exercício 7
 Função: Ler o peso e altura de um indivíduo e imprimir seu IMC
 Autora: Ruth Ellen
 Data: 18/11/2020
"""

#Entrada de Dados

p = float(input("Digite seu peso(kg): "))
a = float(input("Digite sua altura(m): "))

#Cálculo e Saída de Dados

imc = p/(a**2)

print("IMC: ",imc)

if imc < 18.5:
    print("Peso Baixo")
    
if imc >= 18.5 and imc <= 24.9:
    print("Peso Normal")
    
if imc >= 25.0 and imc <= 29.9:
    print("Sobrepeso")
    
if imc >= 30.0 and imc <= 34.9:
    print("Obesidade (Grau 1)")
    
if imc >= 35.0 and imc <= 39.9:
    print("Obesidade (Grau 2)")
    
if imc >= 40.0:
    print("Obesidade (Grau 3)")


print("Fim do programa")
