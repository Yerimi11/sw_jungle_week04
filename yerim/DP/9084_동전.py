import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(m + 1):
            # a_(i-k) 를 만드는 방법이 존재한다면 
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수를 더한다.
            if i >= coin:
                dp[i] += dp[i - coin]

    print(dp[m])