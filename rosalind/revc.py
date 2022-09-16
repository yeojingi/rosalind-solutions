s = input()

c = ""

comp = {"A": "T", "T": "A", "C": "G", "G": "C"}

for i in range(len(s)):
  c += comp[s[-i-1]]

print(c)