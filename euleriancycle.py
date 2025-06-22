def read_graph(filename):
    graph = {}
    with open(r"C:\Users\LENOVO\Downloads\dataset_30187_2.txt", 'r') as file:
        for line in file:
            if ':' in line:
                parts = line.strip().split(':')
                node = int(parts[0].strip())
                neighbors = list(map(int, parts[1].strip().split())) if parts[1].strip() else []
                graph[node] = neighbors
    return graph

def eulerian_cycle_directed(graph):
    graph_copy = {node: edges[:] for node, edges in graph.items()}
    start_node = next((node for node in graph_copy if graph_copy[node]), None)
    if start_node is None:
        return []

    cycle = []
    stack = [start_node]

    while stack:
        current = stack[-1]
        if graph_copy.get(current):
            next_node = graph_copy[current].pop()
            stack.append(next_node)
        else:
            cycle.append(stack.pop())

    cycle.reverse()
    return cycle

def main():
    graph = read_graph('input.txt')
    cycle = eulerian_cycle_directed(graph)
    print(' '.join(map(str, cycle)))

if __name__ == '__main__':
    main()
