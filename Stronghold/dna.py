s = input()

ans = [0, 0, 0, 0]
dna = {"A":0, "C": 1, "G":2, "T":3}

for c in s:
  ans[dna[c]] += 1

print(*ans)