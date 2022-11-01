import requests

filename = input()
f = open(f"./data/{filename}", "r")

anss = []
lineNames = []
while True:
  fileline = f.readline().strip()
  if not fileline:
    break
  lineNames.append(fileline)
  protein_name = fileline.split('_')[0]
  res = requests.get(f"https://rest.uniprot.org/uniprotkb/{protein_name}.fasta")
  output = res.text

  line_stream = output.splitlines()

  ans = []
  string = ""
  for line in line_stream:
    if line[0] == '>':
      continue
  
    string += line
  
  print(f"{protein_name} is received: {string}")
  L = len(string)
  for i in range(L - 4 + 1):
    window = string[i:i+4]

    if window[0] == "N" \
      and window[1] != "P" \
      and (window[2] == "S" or window[2] == 'T') \
      and window[3] != 'P':
      ans.append(i+1)
  anss.append(ans)
for i in range(len(anss)):
  ans = anss[i]
  if not ans:
    continue
  print(lineNames[i])
  print(" ".join(list(map(str, ans))))