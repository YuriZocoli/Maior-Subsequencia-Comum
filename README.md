# Calculador de LCS

Este projeto é uma interface gráfica para calcular todas as Subsequências Comuns Mais Longas (LCS) entre pares de strings.

## Descrição do Problema

Dadas duas strings, o objetivo é encontrar todas as subsequências comuns mais longas, que são sequências de caracteres na mesma ordem em ambas as strings, mas não necessariamente consecutivas.

## Solução Utilizada

- **Cálculo do Comprimento**: Usa programação dinâmica com uma tabela `dp` para determinar o tamanho da LCS.
- **Geração das LCS**: Oferece duas opções:
  - *Com backtracking*: Explora recursivamente os caminhos na tabela `dp`.
  - *Sem backtracking*: Constrói iterativamente os conjuntos de subsequências.

## Como Executar

1. **Requisitos**: Python 3.x com Tkinter.
2. **Execução**:
   - Rode com: `python Main.py`.
   - Na interface, selecione a abordagem, insira o número de pares de strings, gere os campos, digite as strings e clique em "Calcular LCS".
3. **Alternativamente**:
   - Opção 1:
     - Rode com: `python DpOnly.py` (para utilizar o codigo utilizando apenas programação dinamica)
      - Na interface, insira o número de pares de strings, gere os campos, digite as strings e clique em "Calcular LCS".
   - Opção 2:
     - Rode com: `python DpWithBacktracking.py` (para utilizar o codigo utilizando da programação dinamica junto ao backtraking)
     - Na interface, insira o número de pares de strings, gere os campos, digite as strings e clique em "Calcular LCS".