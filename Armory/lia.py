k, N = map(int, input().split())

def ncr(n, r):
  numerator = 1
  denominator = 1
  for i in range(r):
    numerator *= n-i
    denominator *= i+1
  return numerator / denominator

ans = 0
for i in range(N, 2**k+1):
  ans += ncr(2**k, i) * (0.25) ** i * (0.75) ** (2**k - i)

print(ans)