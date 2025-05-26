"""
=== Verificador de Idade ===

Este programa verifica em qual faixa etária você se encaixa:
- Menor de idade: menos de 18 anos
- Adulto: entre 18 e 64 anos
- Idoso: 65 anos ou mais

Como usar:
1. Execute o programa
2. Digite sua idade quando pedir
3. O programa mostrará sua faixa etária

Exemplo:
- Se digitar 15: "Você é menor de idade"
- Se digitar 25: "Você é adulto"
- Se digitar 70: "Você é idoso"
"""

def verificar_idade():
    idade = int(input("Digite sua idade: "))
    if idade < 0 or idade > 101:
        return "Idade inválida!"
    elif idade < 18:
        return "Você é menor de idade"
    elif idade < 65:
        return "Você é adulto"
    else:
        return "Você é idoso"

