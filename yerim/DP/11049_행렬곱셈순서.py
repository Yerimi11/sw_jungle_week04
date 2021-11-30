import sys
input = sys.stdin.readline
n = int(input())
rows = []
cols = []
for _ in range(n):
    row, col = map(int, sys.stdin.readline().split())
    rows.append(row) # i
    cols.append(col) # j

dp = [[0]*(n) for _ in range(n)]
# for문 돌리기 아래->위 방향으로
for col in range(1, n):
    # for row in range(n-col, 0, -1):
    for row in range(col-1, -1, -1): # j(col)=123돌때 j-1(인덱스포함), -1(0까지돌고), -1씩 줄음
        minMulti = float('inf') # 여기서 최솟값 무한대로 셋팅
        for k in range(row, col):
            minMulti = min(minMulti, dp[row][k]+dp[k+1][col]+(rows[row]*rows[k+1]*cols[col]))
            dp[row][col] = minMulti
print(dp[0][len(cols)-1]) # 5*3*6 = 90
