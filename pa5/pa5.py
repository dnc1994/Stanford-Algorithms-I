class Graph(object):
    def __init__(self):
        self.edges = {}
        self.dists = {}
        
        
    def add_edge(self, x, y, v):
        if not x in self.edges:
            self.edges[x] = []
        self.edges[x].append(y)
        self.dists[(x, y)] = v


def dijkstra(graph, source):
    dists = {source: 0}
    nodes = graph.edges.keys()
    
    while nodes:
        min_node = None
        for node in nodes:
            if node in dists:
                if min_node is None or dists[node] < dists[min_node]:
                    min_node = node
        if min_node is None:
            break
            
        nodes.remove(min_node)
        
        for edge in graph.edges[min_node]:
            weight = dists[min_node] + graph.dists[(min_node, edge)]
            if edge not in dists or weight < dists[edge]:
                dists[edge] = weight
     
    return dists


def main():
    source = 1
    goal = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    graph = Graph()
    
    with open('dijkstraData.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip().split('\t')
        x = int(line[0])
        for o in line[1:]:
            y, v = map(int, o.split(','))
            graph.add_edge(x, y, v)
            
    dists = dijkstra(graph, source)
    print ','.join(map(str, [dists[i] for i in goal]))
    
    
if __name__ == '__main__':
    main()