import pickle
import sys
import threading

t = 0
f = None
visited = None
scc_size = 0

def DFS(graph, x):
    global visited
    global f
    global t

    visited[x] = True
    
    for y in graph[x]:
        if not visited[y]:
            DFS(graph, y)
            
    f[t] = x
    t += 1
    
def DFS2(graph, x):
    global visited
    global scc_size

    visited[x] = True
    
    for y in graph[x]:
        if not visited[y]:
            DFS2(graph, y)
            
    scc_size += 1
    
def First_DFS(graph):
    global visited
    global f
    global t
    
    t = 0
    n = len(graph)
    f = [None] * n
    visited = [False] * n
    
    for x in reversed(range(n)):
        if not visited[x]:
            DFS(graph, x)

def Second_DFS(graph):
    global visited
    global f
    global scc_size
    
    n = len(graph)
    visited = [False] * n
    scc = []
    
    for i in reversed(range(n)):
        if not visited[f[i]]:
            scc_size = 0
            DFS2(graph, f[i])
            scc.append(scc_size)
    
    return scc

def build_graph():
    graph = []
    graph_rev = []
    
    with open('SCC.txt', 'r') as f:
        
        line = f.readline()
        count = 0
        while line:
            count += 1
            if count % 100000 == 0:
                print 'line ~ %d loaded' % count
        
            x, y = map(int, line.strip().split(' '))
            
            while len(graph) < max(x, y):
                graph.append([])
            while len(graph_rev) < max(x, y):
                graph_rev.append([])
                
            graph[x-1].append(y-1)
            graph_rev[y-1].append(x-1)
            
            line = f.readline()
            
    return graph, graph_rev
    
def main(build=False):
    if build:
        graph, graph_rev = build_graph()
        pickle.dump(graph, open('graph.dump', 'w'))
        pickle.dump(graph_rev, open('graph_rev.dump', 'w'))
    
    graph = pickle.load(open('graph.dump', 'r'))
    graph_rev = pickle.load(open('graph_rev.dump', 'r'))
    First_DFS(graph_rev)
    scc = Second_DFS(graph)
    print sorted(scc, reverse=True)[:5]
    
if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target = main)
    thread.start()