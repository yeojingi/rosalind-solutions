name = input()
f = open(f"./data/{name}", "r")

X = f.readline().strip()
f.readline()

Sigma = f.readline().strip().split()
f.readline()

pi = f.readline().strip()
f.readline()
States = f.readline().strip().split()
f.readline()

header = f.readline().strip().split()
matrix = {}
while True:
  row = f.readline()
  if not row:
    break

  row = row.strip().split()
  matrix[row[0]] = { header[i] : float(row[i+1]) for i in range(len(row[1:]))}

possibility = 1
for i in range(len(X)):
  possibility *= matrix[ pi[i] ][ X[i] ]

print(possibility)