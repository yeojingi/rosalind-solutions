from Bio import Entrez
f = open("./data/rosalind_gbk.txt", "r")
genus = f.readline().strip()
fromDate = f.readline().strip()
endDate = f.readline().strip()

Entrez.email = "businessjingi@gmail.com"
handle = Entrez.esearch(db="nucleotide", term=f'"{genus}"[Organism] AND ("{fromDate}"[Publication Date] : "{endDate}"[Publication Date])')
record = Entrez.read(handle)
print(record["Count"])