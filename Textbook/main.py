from ba1h import approximate_pattern_matching

if __name__ == '__main__':
  filename = input()
  f = open(f"./data/{filename}", "r")
  # Pattern = f.readline().strip()
  pattern = f.readline().strip()
  dna = f.readline().strip()
  d = int(f.readline().strip())
  # k = int(f.readline().strip())
  # k, L, t = map(int, f.readline().strip().split())
  res = approximate_pattern_matching(pattern, dna, d)
  print(res)