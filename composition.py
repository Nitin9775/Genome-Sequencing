def Compostion(k, Text):
    n = len(Text)
    kmers = []
    for i in range(n-k+1):
        kmer = Text[i:i+k]
        kmers.append(kmer)
        sorted_kmers = sorted(kmers)
    return sorted_kmers

k = 100
with open(r"C:\Users\LENOVO\Downloads\dataset_30153_3 (4).txt", "r") as file:
    contents = file.read()         # Read the entire content
    Text = contents

print(*Compostion(k, Text))   