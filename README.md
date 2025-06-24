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
    
## Detalhes Técnicos

### Como a programação dinâmica foi aplicada na solução?

A programação dinâmica foi utilizada para calcular o comprimento da Subsequência Comum Mais Longa (LCS) entre duas strings. Criamos uma tabela bidimensional `dp` onde `dp[i][j]` representa o comprimento da LCS entre os prefixos `string1[0..i-1]` e `string2[0..j-1]`. A tabela é preenchida iterativamente:
- Se os caracteres `string1[i-1]` e `string2[j-1]` são iguais, `dp[i][j] = dp[i-1][j-1] + 1`.
- Caso contrário, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

Essa abordagem evita recalcular subproblemas, armazenando resultados intermediários para uso futuro.

### Por que o uso de backtracking é necessário neste problema?

O backtracking é necessário na versão "com backtracking" para gerar todas as possíveis LCS a partir da tabela `dp`. Embora a tabela forneça o comprimento da LCS, ela não indica diretamente quais caracteres compõem as subsequências. O backtracking explora recursivamente os caminhos na tabela `dp`, reconstruindo as LCS ao retroceder a partir do final das strings, garantindo que todas as combinações válidas sejam encontradas.

### Houve desafios na implementação? Quais? Como foram superados?

Sim, houve desafios na implementação, sofremos bastante com:
- **Cumprimento dos requisitos lógicos**: Aplicação da logica de programação dinamica e backtraking
- **Interface gráfica**: Implementar uma interface que interaja com o usuario sem utilização de linguagem de marcação (como por exemplo html), que é o tipo de linguagem para interface que os integrantes mais tem costume.
- **Rolagem do mouse**: Fazer a rolagem funcionar corretamente sobre os campos de entrada e resultados.

Esses desafios foram superados:
- Estudo do problema e como aplicar a logica sobre ele.
- Estudo de codigos já feitos com interface grafica em python para melhor entendimento e visualização da solução.
- Vinculando eventos de rolagem dinamicamente aos widgets com o método `_on_mousewheel`, infelizmente a abordagem utilizada funciona apenas para windows e mac não tendo o resultado esperado em linux (caso que a rolagem não funciona).

### Qual é a complexidade da solução proposta?

A complexidade varia dependendo da abordagem utilizada. Estabeleceremos previamente que a importância das duas soluções gira em torno da geração da matriz DP e da extração de todas as subsequências LCS possíveis. Por isso, em ambos os casos, duas funções serão escolhidas como as mais importantes e necessárias para o cálculo da complexidade.

#### Versão utilizando apenas programação dinâmica

Considerando a regra estabelecida, as seguintes funções são as mais importantes para o estudo da complexidade:
- `calculateLcsLength`
- `all_lcs_without_backtracking`

**Sobre o `calculateLcsLength`:**
1. **Inicialização da matriz dp**:  
   `dp = [[0] * (len_string2 + 1) for _ in range(len_string1 + 1)]`  
   São criadas `(n + 1)` linhas, cada uma com `(m + 1)` elementos.  
   **Custo**: O(n * m)
2. **Preenchimento da matriz com dois for**:  
   ```python
   for i in range(1, len_string1 + 1):
       for j in range(1, len_string2 + 1):
           if string1[i-1] == string2[j-1]:
               dp[i][j] = dp[i-1][j-1] + 1
           else:
               dp[i][j] = max(dp[i-1][j], dp[i][j-1])
   ```  
   Dois laços aninhados de tamanho \(n\) e \(m\). Cada operação interna é constante O(1).  
   **Custo total**: O(n * m)
3. **Complexidade de tempo final da função**: O(n * m)

**Sobre o `all_lcs_without_backtracking`:**
1. **Inicialização da matriz de conjuntos**:  
   ```python
   result_dp = [[set() for _ in range(m + 1)] for _ in range(n + 1)]
   ```
   Criação de (n * m) conjuntos (vazios inicialmente).  
   **Custo**: O(n * m)
2. **Inicialização das bordas com conjunto contendo string vazia**:  
   ```python
   for i in range(n + 1): result_dp[i][0].add("")
   for j in range(m + 1): result_dp[0][j].add("")
   ```  
   Operações simples, cada uma de custo O(1), repetidas (n + m) vezes.  
   **Custo**: O(n + m)
3. **Preenchimento da matriz com subconjuntos de LCSs**:  
   ```python
   for i in range(1, n + 1):
       for j in range(1, m + 1):
           if string1[i-1] == string2[j-1]:
               for seq in result_dp[i-1][j-1]:
                   result_dp[i][j].add(seq + string1[i-1])
           else:
               if len_dp[i-1][j] == len_dp[i][j]:
                   result_dp[i][j].update(result_dp[i-1][j])
               if len_dp[i][j-1] == len_dp[i][j]:
                   result_dp[i][j].update(result_dp[i][j-1])
   ```  
   **Ponto de atenção**: Cada célula `result_dp[i][j]` pode armazenar diversas strings. O número de subsequências pode crescer exponencialmente em alguns casos, especialmente quando existem muitas LCSs de mesmo tamanho.
   
    Se houver até (k) LCSs no pior caso por célula, assim o seguinte resultado pode ser obtido:  

   **Complexidade de tempo final**: O(n * m * k), onde (k) é o número máximo de subsequências armazenadas por célula.

**Complexidade Total da abordagem**: O(n * m * k)

#### Versão utilizando programação dinâmica e backtracking

Considerando a regra estabelecida, as seguintes funções são as mais importantes para o estudo da complexidade:
- `calculateLcsLength` (idêntica à outra abordagem, custo O(n * m))
- `all_lcs_with_backtracking`

**Sobre o `all_lcs_with_backtracking`:**  
O cálculo se concentra no backtracking, pois é onde reside a essência do método:

1. **Caso Base**:  
   ```python
   if i == 0 or j == 0:
       if len(current) == lcs_len and is_subsequence(current, string2):
           result.add(current)
   ```  
   Quando algum índice chega a zero, indica o fim do caminho na matriz. Se a string `current` tiver tamanho igual ao da LCS e for subsequência de `string2`, ela é adicionada ao conjunto.  
   **Complexidade Local**: O(m) devido ao custo de `is_subsequence`:  
   ```python
   it = iter(string)
   return all(c in it for c in sub)
   ```  
   Loop simples com custo \(m\).

2. **Caso – Caracteres Diferentes (Pior Caso)**:  
   ```python
   if len_dp[i-1][j] > len_dp[i][j-1]:
       backtrack(i-1, j, current)  # Caminha para cima ↑
   elif len_dp[i][j-1] > len_dp[i-1][j]:
       backtrack(i, j-1, current)  # Caminha para esquerda ←
   else:
       backtrack(i-1, j, current)
       backtrack(i, j-1, current)
   ```  
   Se ambos os valores forem diferentes, dois caminhos podem ser explorados, sendo este o pior caso. No pior cenário (exemplo: "aaaaa" x "bbbbb"), toda bifurcação é explorada, podendo chegar a \(2^(n + m)\). Considerando que o caso base sempre será explorado ao fim, isso adiciona um custo O(m).  
   **Complexidade Total da função**: O(2^(n + m) * m)

**Complexidade Total da abordagem**: O(2^(n + m) * m)