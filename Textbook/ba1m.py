index = int(input())
k = int(input())

nuc = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
indexToNuc = ['A', 'C', 'G', 'T']

string = ""
while k > 0:
  ci = index % 4
  index //= 4
  k -= 1

  string += indexToNuc[ci]

string = string[::-1]

print(string)