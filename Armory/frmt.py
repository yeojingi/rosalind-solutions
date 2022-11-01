import math
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id="JQ290344 JX569368 BT149867 JN573266 JX914595 JX308817 BT149866 JX317645".split(), rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))

minLength = math.inf
minIndex = 0
for i in range(len(records)):
  currentLength = len(records[i].seq)
  
  if minLength > currentLength:
    minLength = currentLength
    minIndex = i

print (records[minIndex].format("fasta"))