def Compostion(k, Text):
    n = len(Text)
    kmers = []
    for i in range(n-k+1):
        kmer = Text[i:i+k]
        kmers.append(kmer)
    return kmers

k = 5
Text =  "CAATCCAAC"
print(Compostion(k, Text))   