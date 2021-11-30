# 함수 구현에 필요한 것
# 1. 재귀의 깊이를 알 수 있는 변수(어디까지 탐색하고있는 중인지)
# 2. 지금까지 경로의 합을 저장하는 변수
# 3. 재귀의 깊이를 이용해 끝까지 도달했을 경우 함수를 리턴할 수 있는 조건문
# (또한 여기서 전체의 합을 total_min에 업데이트)

# 함수 최적화에 필요한 것
# 1. 다음에 가고 싶은 경로의 길이 없는 경우(cost = 0) return
# 2. 합의 최솟값을 구하는 중인데, 지금까지의 경로와 다음 경로의 합을 더해서 최솟값보다 클 경우 더 볼 필요 없이 return

# 변수 설명
# past : 내가 이전에 방문했던 노드의 위치(인덱스)
# start : 이 경로의 맨 처음 방문한 노드의 위치(인덱스)
# count : 탐색을 어느 정도의 깊이까지 갔는지 카운트하는 변수
# total_cost : 지금까지의 모든 경로의 합을 저장한 변수
# 배열 읽는 법 : paths[출발지][도착지]

import sys

def dfs(past = 0, start = 0, count = 0, total_cost = 0):
    global total_min

    # 지금까지의 비용의 합계가 최솟값보다 클 경우 return
    if total_min < total_cost:
        return

    # 모든 노드를 방문한 경우 최솟값을 계산하고 return
    if count == n:
        # 다음 경로에 길이 없는 경우
        if not paths[past][start] == 0:
        # 마지막 노드에서 첫 노드로 돌아가는 과정까지 합쳐서 최솟값을 결정
            total_min = min(total_min, total_cost + paths[past][start])
        return

    for i in range(n):
        # 이번 노드를 방문하지 않았고 다음 노드가 길이 뚫려있는 경우 알고리즘 진행
        if visits[i] == False and paths[past][i] != 0:
            # 첫 노드일 경우, 다음 경로에 길이 없는 경우 패스, 다음 노드까지의 합이 최솟값보다 큰 경우
            if count == 0:
                start = i       # 첫 노드의 시작 위치를 저장
                past = i        # 현재 0으로 초기화되어있지만 첫 노드가 아닌 다른 노드에서 시작할 수도 있으니 첫 노드 위치를 넣어서 초기화

            visits[i] = True
            dfs(i, start, count + 1, total_cost + paths[past][i])
            visits[i] = False
    

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())

    paths = []
    visits = [False] * n
    total_min = 100000001
    for _ in range(n):
        paths.append(list(map(int, input().split())))
    
    dfs()
    print(total_min)