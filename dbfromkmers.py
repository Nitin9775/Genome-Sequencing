def DeBruijnFromkmers(Patterns):
    graph = {}
    for kmer in Patterns:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        if prefix in graph:
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]
    for key in sorted(graph):
        print(f"{key}: {' '.join(graph[key])}")

with open(r"C:\Users\LENOVO\Downloads\dataset_30184_8.txt", "r") as file:
    content = file.read()

Patterns = content.split()

DeBruijnFromkmers(Patterns)