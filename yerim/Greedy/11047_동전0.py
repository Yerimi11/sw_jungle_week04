import sys
n, money = map(int, sys.stdin.readline().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)

count = 0
for coin in coins:
    if coin == 0:
        break
    count += money // coin
    money = money % coin # 남은 잔액

print(count)

# K가 동전금액들보다 작은 경우 큰금액부터 도는게 비효율적이니 K가 동전보다 작을 경우 continue(패스 or pop)하는 조건 걸어주기