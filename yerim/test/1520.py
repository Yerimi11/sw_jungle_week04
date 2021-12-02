import sys
input = sys.stdin.readline

# 상하좌우 방향
# 다음값이 현재 값보다 < 작을 때만 이동
# DP[N] = (n-1, n-1)까지 항상 내리막길로만 이동하는 경로의 개수

def dfs(x, y):
    if [x , y] == [N-1, M-1]:
        return dp[x][y]
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dp[-1][-1] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(dfs(0,0))