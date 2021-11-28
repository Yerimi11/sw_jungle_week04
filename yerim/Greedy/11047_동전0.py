import sys
n, money = map(int, sys.stdin.readline().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)

count = 0
# while money == 0:
for coin in coins:
    if coin == 0:
        break
    count += money // coin
    money = money % coin # 남은 잔액

print(count)