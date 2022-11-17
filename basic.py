def sequence_alignment(x, y, alpha, DNA, delta):
    m = len(x)
    n = len(y)

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i * delta
    
    for i in range(n+1):
        dp[0][i] = i * delta

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1] + alpha[DNA[x[i-1]]][DNA[y[j-1]]],
                                dp[i-1][j] + delta,
                                dp[i][j-1] + delta)
                
    print(dp[m][n])
    return dp

def form_sequence(dp):
    return ""

def get_penalty():
    DNA = {}
    DNA['A'], DNA['C'], DNA['T'], DNA['G'] = 0, 1, 2, 3
    return [[0,110,48,94], [110,0,118,48], [48,118,0,110], [94,48,110,0]], DNA, 30

def main():
    s1 = "ACACTGACTACTGACTGGTGACTACTGACTGG"
    s2 = "TATTATACGCTATTATACGCGACGCGGACGCG"

    alpha, DNA, delta = get_penalty()

    dp = sequence_alignment(s1, s2, alpha, DNA, delta)
    form_sequence(dp)

main()