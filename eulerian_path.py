from collections import defaultdict, deque

def parse_input_file(filename):
    adj_list = defaultdict(list)
    with open(r"C:\Users\LENOVO\Downloads\dataset_30187_6.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if not line or ':' not in line:
                continue
            src, dests = line.split(':')
            src = int(src.strip())
            dest_nodes = list(map(int, dests.strip().split()))
            adj_list[src] = dest_nodes
    return adj_list

def find_eulerian_path(adj_list):
    graph = defaultdict(deque)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    nodes = set()

    for src, dests in adj_list.items():
        for dest in dests:
            graph[src].append(dest)
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
        if graph[curr]:
            stack.append(graph[curr].popleft())
        else:
            path.append(stack.pop())

    return path[::-1]

if __name__ == '__main__':
    filename = 'graph.txt'  # Change to your file name
    adj_list = parse_input_file(filename)
    path = find_eulerian_path(adj_list)
    print("Eulerian Path:")
    print(" ".join(map(str, path)))
