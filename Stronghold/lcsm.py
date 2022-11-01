name = input()
f = open(f"./data/{name}", "r")

strands = []
strand = ""

while True:
  line = f.readline()
  if not line:
    strands.append(strand)
    break
  line = line.strip()

  if line[0] == '>':
    if strand:
      strands.append(strand)
    strand = ""
    continue
  else:
    strand += line

s = {}

for i in range(len(strands[0])):
  for j in range(1, len(strands[0]) - i):
    s[strands[0][i:i+j]] = 1

print(len(strands))
for k in range(1, len(strands)):
  ns = {}
  print(k)
  for i in range(len(strands[k])):
    for j in range(1, len(strands[k]) - i):
      cur = strands[k][i:i+j]
      if s.get(cur):
        ns[cur] = 1
  s = ns

maxKey = ''
maxValue = 0
for key, value in s.items():
  if len(key) > maxValue:
    maxValue = len(key)
    maxKey = key

print(maxKey)