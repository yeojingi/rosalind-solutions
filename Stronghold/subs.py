text = input()
t = input()

anss = []
for i in range(len(text) - len(t) + 1):
  if t == text[i:i+len(t)]:
    anss.append(i+1)

print(*anss)