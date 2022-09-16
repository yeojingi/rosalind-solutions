from queue import PriorityQueue


f = open("./data/rosalind_gc.txt", "r")

q = PriorityQueue()
name = f.readline()[1:-1]
while True:
  strand = ""
  temp = ""
  while True:
    temp = f.readline()[:-1]
    if not temp:
      break
    elif temp[0] != ">":
      strand += temp
    else:
      nname = temp[1:]
      break


  gcs = 0
  for s in strand:
    if s == 'G' or s == 'C':
      gcs += 1
  
  q.put(( 1 - (gcs / len(strand)) , name))
  name = nname
  if not temp:
    break

res = q.get()
print(res[1], (1-res[0])*100, sep="\n")