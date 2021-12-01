import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if w > j: # 넣을 무게가 j값보다 크면 (w=6일 때 j=0~5값들)
            dp[i][j] = dp[i-1][j] # 그 이전의 위치(i,j)들은 바로 윗줄 값으로 써주기
        else: # 윗줄값과 새로 v더한 값과 비교 후 max값으로 갱신
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v) # [i-1]로 해줘야 중복갱신 안됨

print(dp[n][k])

# 물건을 1개만 넣어야하는데 n=5일때 5개까지 들어가는 오류 발생 => 2차원배열로 만들기

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