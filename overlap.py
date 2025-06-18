def Overlap(Patterns):
    Overlap_graph = {}
    k = len(Patterns[0])
    for pattern in Patterns:
        suffix = pattern[1:k]
        overlaps = []
        for candidate in Patterns:
            if pattern != candidate and suffix == candidate[0:k-1]:
                overlaps.append(candidate)
        if overlaps:
            Overlap_graph[pattern] = overlaps
    return Overlap_graph

Patterns = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT", "GGCAC"]
graph = Overlap(Patterns)

for key in graph:
    print(f"{key}: {' '.join(graph[key])}")
