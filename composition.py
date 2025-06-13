def Compostion(k, Text):
    n = len(Text)
    kmers = []
    for i in range(n-k+1):
        kmer = Text[i:i+k]
        kmers.append(kmer)
    return kmers

with open(r"C:\Users\LENOVO\Downloads\dataset_30153_3 (6).txt", "r") as file:
    lines = file.read().strip().splitlines()
    k = int(lines[0])
    Text = ''.join(lines[1:]).replace(' ', '').strip()

print(*Compostion(k, Text))