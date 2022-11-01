name = input()
f = open(f"./data/{name}", "r")

x = f.readline().strip(); f.readline()
xs = len(f.readline().strip().split()); f.readline()
paths = f.readline().strip().split(); f.readline()
transition_header = f.readline().strip().split()
transition = {}

for _ in range(len(paths)):
  row = f.readline().strip().split()
  transition[row[0]] = { transition_header[n-1] : float(row[n]) for n in range(1, len(row))}

f.readline()
emission_header = f.readline().strip().split()
emission = {}
for _ in range(len(paths)):
  row = f.readline().strip().split()
  emission[row[0]] = { emission_header[n-1] : float(row[n]) for n in range(1, len(row))}

p = 1

def emit(i, s):
  return emission[s][x[i]]

dp = [{path: 0 for path in paths} for _ in range(len(x))]

for j in paths:
  dp[0][j] = emission[j][x[0]]

string = {path: "" for path in paths}
for i in range(1, len(x)):
  newString = {path: "" for path in paths}
  for now in paths:
    p_cand = 0
    maxChar = ""
    for before in paths:
      p_before = dp[i-1][before]
      x_cur = x[i]
      p_cur = p_before * transition[before][now] * emission[now][x_cur]
      if p_cur > p_cand:
        p_cand = p_cur
        maxChar = before
    dp[i][now] = p_cur
    newString[now] = string[maxChar] + now
  string = newString
  print(string)
  print(dp[i])

print(*dp, sep="\n")