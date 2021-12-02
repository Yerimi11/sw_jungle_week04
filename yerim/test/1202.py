import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewelry = [0]
for _ in range(N):
    jewelry.append(list(map(int, input().split())))
bag = [0] # bag = [0, 10, 2]
for _ in range(K):
    bag.append(int(input().strip()))
bag.sort() # 작은 무게 넣을 수 있는 가방 부터 채움
ans = 0 # bag = [0, 2, 10]

for weight in bag[1:]: # [1:] 인덱스 무시
    dp = [[0] * (weight+1) for _ in range(N+1)] # 가방 하나마다의 테이블 만듦 2+1X3+1, 10+1X3+1

    for i in range(1, N+1):
        w, v = jewelry[i]
        for j in range(1, weight+1): # 가방 하나의 무게 : weight. 한 가방에 넣을 무게
            if j < w: # j : 최대무게, w : 물건 무게 / 무게가 가방에 넣을 수 있는 크기보다 작을 때만 넣기
                dp[i][j] = dp[i-1][j]
            else: # 가방 최대 무게가 물건 무게보다 클 때,
                if dp[i-1][j][0] > v + dp[i-1][j-w][0]: # 0번째 무게 가방?
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j][0] = v + dp[i-1][j-w][0]
                    dp[i][j][1] = str(i) + dp[i-1][j-w][1]
    ans += dp[N][weight][0]
    a = list(map(int,dp[N][weight][1])) # 가방에 넣은 보석들 인덱스 번호
    for p in range(a):
        del jewelry[p]
print(ans)