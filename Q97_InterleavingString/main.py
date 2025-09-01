def isInterleave(s1, s2, s3):
    n, m, l = len(s1), len(s2), len(s3)

    # If total length doesn't match, impossible
    if n + m != l:
        return False

    # dp[i][j] → can we form s3[:i+j] using s1[:i] and s2[:j]
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n + 1):
        for j in range(m + 1):
            if i > 0 and s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                dp[i][j] = True
            if j > 0 and s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                dp[i][j] = True

    return dp[n][m]


s1 = input("Enter string s1: ").strip()
s2 = input("Enter string s2: ").strip()
s3 = input("Enter string s3: ").strip()

if isInterleave(s1, s2, s3):
    print("✅ Yes, s3 is an interleaving of s1 and s2.")
else:
    print("❌ No, s3 is NOT an interleaving of s1 and s2.")
