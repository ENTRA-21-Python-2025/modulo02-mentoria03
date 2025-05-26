"""
=== Menu Principal de Exemplos ===

Este programa é um menu que integra três exemplos diferentes:

1. Verificar Idade
   - Verifica sua faixa etária
   - Mostra se você é menor de idade, adulto ou idoso

2. Calcular IMC
   - Calcula seu Índice de Massa Corporal
   - Mostra sua classificação (abaixo do peso, normal, etc.)

3. Verificar Estação do Ano
   - Identifica a estação do ano
   - Baseado no mês que você informar

Como usar:
1. Execute o programa
2. Escolha uma opção (1 a 4)
3. Siga as instruções de cada programa
4. Pressione Enter para voltar ao menu
5. Escolha 4 para sair

Exemplo de uso:
1. Digite 1 para verificar idade
2. Digite sua idade
3. Veja o resultado
4. Pressione Enter
5. Escolha outra opção ou saia
"""

from exemplo_verificar_idade import verificar_idade
from exemplo_calcular_peso import calcular_imc
import exemplo_verificar_estacao


def exibir_menu():
    print("\n=== Menu Principal ===")
    print("1. Verificar idade")
    print("2. Calcular IMC")
    print("3. Verificar estação do ano")
    print("4. Sair")
    return input("\nEscolha uma opção (1-4): ")

def main():
    while True:
        opcao = exibir_menu()
        
        match opcao:
            case '1':
                print("\n=== Verificador de Idade ===")
                resultado = verificar_idade()
                print(f"\nResultado: {resultado}")
            case '2':
                print("\n=== Calculadora de IMC ===")
                resultado = calcular_imc()
                print(f"\nResultado: {resultado}")
            case '3':
                print("\n=== Verificador de Estação do Ano ===")
                resultado = exemplo_verificar_estacao.verificar_estacao()
                print(f"\nEstação: {resultado}")
            case '4':
                print("\nPrograma finalizado!")
                break
            case _:
                print("\nOpção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main() 