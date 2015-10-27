import random
import copy

def contract_edge(graph, x, y):
    graph[x] = graph[x] + graph[y]
    graph.pop(y)
    for i in graph:
        for j in range(len(graph[i])):
            if graph[i][j] == y:
                graph[i][j] = x
    graph[x] = filter(lambda v: v != x, graph[x])
 
def kargerMinCut(graph, seed):
    random.seed(seed)
    
    while len(graph) > 2:
        x = random.choice(graph.keys())
        y = random.choice(graph[x])
        contract_edge(graph, x, y)
        
    return len(graph.values()[0])
 
def main():
    graph = {}

    with open('kargerMinCut.txt', 'r') as f:
        lines = [line.strip().split('\t') for line in f.readlines()]
        
    for line in lines:
        nbr = map(int, line)
        graph[nbr.pop(0)] = nbr
       
    seed = 0
    answer = 200 * 200
    while True:
        min_cut = kargerMinCut(copy.deepcopy(graph), seed)
        answer = min(answer, min_cut)
        print answer
        seed += 1
     
if __name__ == '__main__':
    main()