"""
=== Verificador de Estação do Ano ===

Este programa identifica a estação do ano baseado no mês:
- Verão: Dezembro, Janeiro e Fevereiro
- Outono: Março, Abril e Maio
- Inverno: Junho, Julho e Agosto
- Primavera: Setembro, Outubro e Novembro

Como usar:
1. Execute o programa
2. Digite o número do mês (1 a 12)
3. O programa mostrará a estação correspondente

Exemplo:
- Se digitar 1: "Verão"
- Se digitar 4: "Outono"
- Se digitar 7: "Inverno"
- Se digitar 10: "Primavera"
"""

def verificar_estacao():
    # Pede o mês para o usuário
    mes = int(input("Digite o número do mês (1-12): "))
    
    # Usa match/case para verificar a estação
    match mes:
        case 12 | 1 | 2:
            return "Verão"
        case 3 | 4 | 5:
            return "Outono"
        case 6 | 7 | 8:
            return "Inverno"
        case 9 | 10 | 11:
            return "Primavera"
        case _:
            return "Mês inválido!"