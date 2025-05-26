# Módulo 02 - Mentoria 03

Este projeto contém exemplos práticos de estruturas condicionais em Python, focando em if/elif/else e match/case.

## Conteúdo do Projeto

O projeto inclui vários exemplos práticos de estruturas condicionais:

### Exemplos de Condicionais
- `exemplo_verificar_idade.py`: Verificação de faixas etárias usando if/elif/else
- `exemplo_calcular_peso.py`: Cálculo de IMC com estruturas condicionais
- `exemplo_verificar_estacao.py`: Verificação de estações usando match/case
- `exemplo_menu_principal.py`: Menu integrado com todos os exemplos

## Requisitos

- Python 3.10 ou superior (para suporte ao match/case)
- Nenhuma dependência externa necessária

## Como Executar

### Usando Make

O projeto inclui um Makefile com comandos simples:

```bash
# Executar o menu principal
make run

# Limpar arquivos temporários
make clean
```

### Execução Direta

Alternativamente, você pode executar os exemplos diretamente:

1. Clone o repositório
2. Execute o menu principal:
   ```bash
   python exemplo_menu_principal.py
   ```
3. Ou execute exemplos individuais:
   ```bash
   python exemplo_verificar_idade.py
   python exemplo_calcular_peso.py
   python exemplo_verificar_estacao.py
   ```

## Estrutura do Projeto

- `Makefile`: Comandos para executar o projeto
- Arquivos de exemplo: Demonstrações práticas de estruturas condicionais

## Exemplos Detalhados

### Verificação de Idade
O arquivo `exemplo_verificar_idade.py` demonstra:
- Uso de if/elif/else para verificar faixas etárias
- Condições:
  ```python
  if idade < 0:
      # Idade inválida
  elif idade < 18:
      # Menor de idade
  elif idade < 65:
      # Adulto
  else:
      # Idoso
  ```

### Cálculo de IMC
O arquivo `exemplo_calcular_peso.py` mostra:
- Cálculo de IMC com estruturas condicionais
- Condições:
  ```python
  if imc < 18.5:
      # Abaixo do peso
  elif imc < 25:
      # Peso normal
  elif imc < 30:
      # Sobrepeso
  else:
      # Obesidade
  ```

### Verificação de Estações
O arquivo `exemplo_verificar_estacao.py` demonstra:
- Uso do match/case para verificar estações
- Condições:
  ```python
  match mes:
      case 12 | 1 | 2:
          # Verão
      case 3 | 4 | 5:
          # Outono
      case 6 | 7 | 8:
          # Inverno
      case 9 | 10 | 11:
          # Primavera
      case _:
          # Mês inválido
  ```

### Menu Principal
O arquivo `exemplo_menu_principal.py` integra:
- Todos os exemplos em um menu interativo
- Navegação usando match/case
- Padrão consistente de saída

## Estruturas Condicionais Utilizadas

### if/elif/else
- Usado para verificar condições em sequência
- Apenas um bloco é executado
- Útil para decisões com múltiplas opções
- Exemplo: verificação de idade e cálculo de IMC

### match/case
- Introduzido no Python 3.10
- Similar ao switch/case de outras linguagens
- Mais limpo para múltiplas condições
- Suporta padrões complexos
- Exemplo: verificação de estações do ano

## Padrão de Saída
Todos os exemplos seguem o mesmo padrão de saída:
1. Título do programa
2. Entrada do usuário
3. Processamento
4. Resultado formatado

## Debugging (Depuração)

### O que é Debugging?
Debugging é como ser um detetive do código! É o processo de encontrar e corrigir erros (bugs) no seu programa. Imagine que você está seguindo um mapa e encontra um caminho fechado - debugging é como encontrar uma rota alternativa.

### Como Fazer Debug no VS Code/Cursor

1. **Configurar o Debug**
   - O arquivo `.vscode/launch.json` já está configurado para o menu principal
   - Você pode adicionar mais configurações para outros arquivos

2. **Iniciar o Debug**
   - Pressione F5 ou clique no ícone de "Play" com o inseto (🐞)
   - Selecione "Python: Menu Principal" na lista de configurações

3. **Pontos de Interrupção (Breakpoints)**
   - Clique na linha onde quer parar (aparece um ponto vermelho)
   - O programa vai parar nessa linha durante a execução

4. **Controles do Debug**
   - ▶️ Continue (F5): Continua a execução
   - ⤵️ Step Over (F10): Executa a linha atual
   - ⤵️ Step Into (F11): Entra dentro da função
   - ⤴️ Step Out (Shift+F11): Sai da função atual
   - ⏹️ Stop (Shift+F5): Para a execução

5. **Painel de Debug**
   - VARIABLES: Mostra todas as variáveis e seus valores
   - WATCH: Adicione variáveis para monitorar
   - CALL STACK: Mostra onde você está no código
   - BREAKPOINTS: Lista todos os pontos de parada

6. **Dicas Rápidas**
   - Passe o mouse sobre as variáveis para ver seus valores
   - Use o console de debug para testar expressões
   - Os valores das variáveis são atualizados em tempo real

