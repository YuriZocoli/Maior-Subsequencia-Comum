def calcularComprimentoLCS(string1, string2):
    """
    Calcula a tabela de comprimentos da Subsequência Comum Mais Longa (LCS)
    entre duas strings usando programação dinâmica.
    """
    # Obtém os comprimentos das duas strings
    len_string1, len_string2 = len(string1), len(string2)

    # Cria a tabela DP inicializada com zeros
    dp = [[0] * (len_string2 + 1) for _ in range(len_string1 + 1)]

    # Preenche a tabela DP iterando sobre cada caractere das duas strings
    for i in range(1, len_string1 + 1):
        for j in range(1, len_string2 + 1):

            # Se os caracteres são iguais, adiciona 1 ao valor da diagonal superior esquerda
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            # Se são diferentes, escolhe o maior valor entre o de cima e o da esquerda
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Retorna a tabela DP completa
    return dp

def all_lcs_with_backtranking(string1, string2, len_dp):
    def is_subsequence(sub, string):
        it = iter(string)
        return all(c in it for c in sub)

    def backtrack(i, j, current):
        if i == 0 or j == 0:
            if len(current) == lcs_len and is_subsequence(current, string2):
                result.add(current)
            return
        if string1[i-1] == string2[j-1]:
            backtrack(i-1, j-1, string1[i-1] + current)
        else:
            if len_dp[i-1][j] > len_dp[i][j-1]:
                backtrack(i-1, j, current)
            elif len_dp[i][j-1] > len_dp[i-1][j]:
                backtrack(i, j-1, current)
            else:
                backtrack(i-1, j, current)
                backtrack(i, j-1, current)

    result = set()
    lcs_len = len_dp[len(string1)][len(string2)]
    backtrack(len(string1), len(string2), "")
    return result

def all_lcs_without_backtraking(string1, string2, len_dp):
    n, m = len(string1), len(string2)
    
    # Construir tabela dp com os conjuntos de LCS
    result_dp = [[set() for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        result_dp[i][0].add("")  # Borda: LCS com string vazia é ""
    for j in range(m + 1):
        result_dp[0][j].add("")  # Borda: LCS com string vazia é ""
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i-1] == string2[j-1]:
                # Se os caracteres são iguais, extendemos as sequências de dp[i-1][j-1]
                for seq in result_dp[i-1][j-1]:
                    result_dp[i][j].add(seq + string1[i-1])
            else:
                # Se diferentes, incluímos sequências do maior comprimento
                if len_dp[i-1][j] == len_dp[i][j]:
                    result_dp[i][j].update(result_dp[i-1][j])
                if len_dp[i][j-1] == len_dp[i][j]:
                    result_dp[i][j].update(result_dp[i][j-1])
    
    return result_dp[n][m]

def main():
    code_type = None
    while not code_type == 1 and not code_type == 2:
        print("selecione a abordagem a ser utilizada:")
        print("1 - Programacao dinamica com backtraking")
        print("2 - Programacao dinamica sem backtraking")
        code_type = int(input())
        if not code_type == 1 and not code_type == 2:
            print("opcao invalida!")
    
    print("quantos conjuntos de dados serao processados")
    D = int(input())
    if code_type == 1:
        for d in range(D):
            s1 = input().strip()
            s2 = input().strip()
            dp = calcularComprimentoLCS(s1, s2)
            lcs = all_lcs_with_backtranking(s1, s2, dp)
            if lcs:
                for sub in sorted(lcs):
                    print(sub)
            if d < D - 1:
                print()
    else:
        for d in range(D):
            s1 = input().strip()
            s2 = input().strip()
            dp = calcularComprimentoLCS(s1, s2)
            lcs = all_lcs_without_backtraking(s1, s2, dp)
            if lcs:
                for sub in sorted(lcs):
                    print(sub)
            if d < D - 1:
                print()

if __name__ == "__main__":
    main()