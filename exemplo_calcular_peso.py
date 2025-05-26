"""
=== Calculadora de IMC (Índice de Massa Corporal) ===

Este programa calcula seu IMC e mostra sua classificação:
- Abaixo do peso: IMC menor que 18.5
- Peso normal: IMC entre 18.5 e 24.9
- Sobrepeso: IMC entre 25 e 29.9
- Obesidade: IMC 30 ou maior

Como usar:
1. Execute o programa
2. Digite seu peso em quilogramas (ex: 70.5)
3. Digite sua altura em metros (ex: 1.75)
4. O programa mostrará seu IMC e classificação

Exemplo:
- Peso: 70kg, Altura: 1.75m
  Resultado: "IMC: 22.86 - Peso normal"
"""

def calcular_imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return f"IMC: {imc:.2f} - Abaixo do peso"
    elif imc < 25:
        return f"IMC: {imc:.2f} - Peso normal"
    elif imc < 30:
        return f"IMC: {imc:.2f} - Sobrepeso"
    else:
        return f"IMC: {imc:.2f} - Obesidade"