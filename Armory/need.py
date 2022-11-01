import math
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id="JX205496.1 JX469991.1".split(), rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))

print(1)
print(records[0].seq)
print(2)
print(records[1].seq)