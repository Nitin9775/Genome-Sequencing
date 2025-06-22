def path_to_genome(path):
    if not path:
        return ""
    genome = path[0]
    for node in path[1:]:
        genome += node[-1]
    return genome

def string_reconstruction(Patterns):
    dB = DeBruijnFromkmers(Patterns)
    path = find_eulerian_path(dB)
    text = path_to_genome(path)
    return text

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
    return graph  # ✅ You need to return the graph for the next step

from collections import defaultdict, deque
def find_eulerian_path(adj_list):
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    nodes = set()

    adj = defaultdict(deque)
    for src, dests in adj_list.items():  # ✅ Fixed
        for dest in dests:
            adj[src].append(dest)
            out_degree[src] += 1
            in_degree[dest] += 1
            nodes.update([src, dest])

    start = None
    for node in nodes:
        if out_degree[node] - in_degree[node] == 1:
            start = node
            break
    if start is None:
        start = next(iter(nodes))

    path = []
    stack = [start]
    while stack:
        curr = stack[-1]
        if adj[curr]:
            stack.append(adj[curr].popleft())
        else:
            path.append(stack.pop())

    return path[::-1]
with open(r"C:\Users\LENOVO\Downloads\dataset_30187_7.txt", 'r') as file:
        k = int(file.readline().strip())
        Patterns = file.readline().strip().split()

# Run the string reconstruction
print("Reconstructed Genome:")
print(string_reconstruction(Patterns))
