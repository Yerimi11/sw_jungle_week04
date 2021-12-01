import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    rank = [list(map(int, input().split())) for j in range(n)]
    rank.sort(key = lambda x:x[0]) 
    # print(rank)
    # [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
    # [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]
    count = 1
    for i in range(n):
        if i == 0:
            max = rank[i][1]
        elif rank[i][1] > max:
            pass
        else:
            rank[i][1] < max
            max = rank[i][1]
            count += 1
    print(count)
# 첫번째 값 기준으로 정렬하고
# 두번째 값을 비교하면서 더 큰 수가 나올 때 마다 max 갱신하고 낮은 수는 떨어뜨린다
