pattern = input()
d = int(input())

neighbors = []

def rec(string, i, n):
  nucleotides = ['A', 'C', 'G', 'T']
  if i >= len(pattern):
    neighbors.append(string)
    return 
  
  for nuc in nucleotides:
    if nuc == pattern[i]:
      rec(string + nuc, i+1, n)
    elif n > 0:
      rec(string + nuc, i+1, n-1)

rec("", 0, d)
f = open("./data/ba1n_output.txt", "w")
f.write("\n".join(neighbors))