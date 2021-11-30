import sys 
def dfs(root, src, visited, cost=0):
    global curr_min
    # 속도 향상을 위해 cost가 현재 최소값을 넘어가면 즉시 종료 
    if cost > curr_min:
        return
    # 모든 노드를 방문하면 마지막 노드에서 첫 노드로 이동할 수 있으면 curr_min업데이트
    if sum(visited) == n:
        if cost_matrix[src][root]:
            curr_min = min(cost + cost_matrix[src][root], curr_min)
        return
    
    for dst in range(n):
        if visited[dst] or not cost_matrix[src][dst]:
            continue
        visited[dst] = True
        dfs(root, dst, visited, cost + cost_matrix[src][dst])
        visited[dst] = False
        
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    # 비용행렬을 만든다. 
    cost_matrix = []
    for _ in range(n):
        rows = list(map(int, input().split()))
        cost_matrix.append(rows)
    
    visited = [False] * (n+1)
    curr_min = float("inf")
    # 모든 경로를 탐색하기 위해 dfs수행
    for root in range(n):
        visited[root] = True
        dfs(root, root, visited)
        visited[root] = False
    
    print(curr_min)
    
