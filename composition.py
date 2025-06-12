def Compostion(k, Text):
    n = len(Text)
    kmers = []
    for i in range(n-k+1):
        kmer = Text[i:i+k]
        kmers.append(kmer)
    sorted_kmers = sorted(kmers)
    return sorted_kmers

k = 5
Text =  "CAATCCAAC"
print(Compostion(k, Text))   