text1 = input()
text2 = input()

d = 0
for i in range(len(text1)):
  if text1[i] != text2[i]:
    d += 1

print(d)
