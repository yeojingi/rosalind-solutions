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

ans = ""
for i in range(len(x)):
  maxChar = ''
  maxPoss = 0
  for j in paths:
    curP = emit(i, j)
    if i > 0:
      curP *= transition[j][ans[-1]]
    if maxPoss < curP:
      maxPoss = curP
      maxChar = j
  ans += maxChar

print(ans)