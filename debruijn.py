def Composition(k, Text):
    n = len(Text)
    kmers = []
    for i in range(n - k + 1):
        kmers.append(Text[i:i + k])
    return sorted(kmers)

def DeBruijnFromText(k, Text):
    kmers = Composition(k, Text)
    graph = {}
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        if prefix in graph:
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]
    for key in sorted(graph):
        print(f"{key}: {' '.join(graph[key])}")

with open(r"C:\Users\LENOVO\Downloads\dataset_30183_6.txt", "r") as file:
    lines = file.read().strip().splitlines()
    k = int(lines[0])
    Text = ''.join(lines[1:]).replace(' ', '').strip()

DeBruijnFromText(k, Text)
