f = open('./data/rosalind_ba10a (1).txt', 'r')
string = f.readline()[:-1]
f.readline()
chars = f.readline()[:-1].split()
f.readline()
header = f.readline()[:-1].split()

chrToInt = {}
for i in range(len(header)):
  chrToInt[header[i]] = i

possibilites = {}

while True:
  line = f.readline()
  if not line:
    break

  line = line[:-1].split()
  char = line[0]
  possis = list(map(float, line[1:]))
  possibilites[char] = possis

ans = 1 / len(chars)
for i in range(len(string)-1):
  ans *= possibilites[string[i]][chrToInt[string[i+1]]]
print(ans)