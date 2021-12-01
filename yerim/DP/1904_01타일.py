import sys
n = int(sys.stdin.readline())
if n == 1:
    print(1)
elif n == 2:
    print(2)

else:
    dp = [0] * 1000001

    dp[0] = 1
    dp[1] = 2
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

    # result = dp[n-1] % 15746
    print(dp[n-1]%15746)