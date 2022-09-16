s = input()
map = {}

for c in s:
  if not map.get(c):
    map[c] = 1
    continue
  map[c] += 1

print(f"{map['A']} {map['C']} {map['G']} {map['T']}")