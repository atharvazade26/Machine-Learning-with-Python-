def editDistance(s1, s2):

    n = len(s1)
    m = len(s2)

    dp = [[0]*(m+1) for _ in range(n+1)]

    # Base cases
    for i in range(n+1):
        dp[i][0] = i

    for j in range(m+1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, n+1):
        for j in range(1, m+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )

    return dp[n][m]


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

ans = editDistance(s1, s2)

print("Minimum Edit Distance =", ans)