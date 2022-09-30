f = open('./data/rosalind_fibd.txt', 'r')
N, M = list(map(int, f.readline().strip().split(' ')))

dp = [0] * (N+1)
idp = [0] * (N+1)
idp[1] = 1

for i in range(2, N+1):
  idp[i] = dp[i-1]
  dp[i] = dp[i-1] + idp[i-1]
  if i - M >= 0:
    dp[i] -= idp[i-M]

# print(dp)
# print(idp)
print(dp[N] + idp[N])