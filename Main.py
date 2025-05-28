def calcularComprimentoLCS(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    print(dp)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp

def all_lcs(s1, s2, dp):
    def is_subsequence(sub, string):
        it = iter(string)
        return all(c in it for c in sub)

    def backtrack(i, j, current):
        if i == 0 or j == 0:
            if len(current) == lcs_len and is_subsequence(current, s2):
                resultado.add(current)
            return
        if s1[i-1] == s2[j-1]:
            backtrack(i-1, j-1, s1[i-1] + current)
        else:
            if dp[i-1][j] > dp[i][j-1]:
                backtrack(i-1, j, current)
            elif dp[i][j-1] > dp[i-1][j]:
                backtrack(i, j-1, current)
            else:
                backtrack(i-1, j, current)
                backtrack(i, j-1, current)

    resultado = set()
    lcs_len = dp[len(s1)][len(s2)]
    backtrack(len(s1), len(s2), "")
    return resultado

def main():
    D = int(input())
    for d in range(D):
        s1 = input().strip()
        s2 = input().strip()
        dp = calcularComprimentoLCS(s1, s2)
        lcs = all_lcs(s1, s2, dp)
        if lcs:
            for sub in sorted(lcs):
                print(sub)
        if d < D - 1:
            print()

if __name__ == "__main__":
    main()