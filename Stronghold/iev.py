name = input()
f = open(f"./data/{name}", "r")
arr = list(map(int, f.readline().strip().split()))

possis = [1, 1, 1, 3/4, 1/2, 0]

ans = 0
for i in range(6):
  ans += arr[i] * possis[i] * 2

print(ans)