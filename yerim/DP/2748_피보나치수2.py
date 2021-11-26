import sys
n = int(sys.stdin.readline())

# DP = Memoization
memoization = [0] * (n+1)
memoization[1] = 1
for i in range(2, n+1):
    memoization[i] = memoization[i-2] + memoization[i-1]

print(memoization[n])