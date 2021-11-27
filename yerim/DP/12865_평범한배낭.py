import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k+1)

for i in range(n): # w, v
    w, v = map(int, input().split())
    for j in range(w, k+1): # w무게 번째 부터 k번째까지
        # dp[j] = max(dp[j], dp[j-w]+v)
        max_value = dp[j-w] + v
        if dp[j] < max_value:
            dp[j] = max_value

print(dp) # 물건을 1개만 넣어야하는데 n=5일때 5개까지 들어가는 오류 발생

# 반례 
# 3 5
# 4 2
# 3 4
# 1 5
# => 9

# 5 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# => 15