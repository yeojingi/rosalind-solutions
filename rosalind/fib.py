n, k = map(int, input().split(' '))

i = 1
nums = 1
dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
  dp[i] = dp[i-1] + k * dp[i-2]

print(dp[n])