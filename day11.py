from collections import defaultdict
def load_graph(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        
    graph = defaultdict(list)
    for l in lines:
        node, out_node = l.split(':')
        out_node.replace('\n','')
        #out_node = out_node[1:]
        out_node.strip()
        out_node = out_node.split()
        graph[node] = out_node
    return graph

def part1(graph: dict):
    weight = defaultdict(int)
    queue = list()
    queue.append('you')
    weight['you'] = 1
    while len(queue) > 0:
        #print(queue)
        node = queue.pop(0)
        for neighbor in graph[node]:
            if  weight.get(neighbor) is None:
                queue.append(neighbor)
            weight[neighbor] += weight[node]
    return weight['out']

def num_way(graph:dict, node1:str, node2: str):
    weight = defaultdict(int)
    queue = list()
    queue.append(node1)
    weight[node1] = 1
    while len(queue) > 0:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if  weight.get(neighbor) is None:
                queue.append(neighbor)
            weight[neighbor] += weight[node]
    #print(weight)
    return weight[node2]

def part2(graph: dict):
    '''svr2fft = num_way(graph, 'svr', 'fft')
    fft2dac = num_way(graph, 'fft', 'dac')
    dac2out = num_way(graph, 'dac', 'out')
    print(f"svr {svr2fft} fft {fft2dac} dac {dac2out} out")
    svr2out = svr2fft * fft2dac * dac2out'''
    svr2fft = num_way(graph, 'svr', 'dac')
    fft2dac = num_way(graph, 'dac', 'fft')
    dac2out = num_way(graph, 'fft', 'out')
    print(f"svr {svr2fft} fft {fft2dac} dac {dac2out} out")
    svr2out = svr2fft * fft2dac * dac2out
    return svr2out

def count_paths(graph):
    from functools import lru_cache

    @lru_cache(None)
    def dfs(node, seen_fft, seen_dac):
        if node == "out":
            return 1 if seen_fft and seen_dac else 0

        total = 0
        for nxt in graph[node]:
            total += dfs(
                nxt,
                seen_fft or nxt == "fft",
                seen_dac or nxt == "dac"
            )
        return total

    return dfs("svr", False, False)

if __name__ == "__main__":
    graph= load_graph("input11-1.txt")
    #print(graph)
    print(part2(graph))
    
    #print(count_paths(graph))
    #821705306760   
    #1222161754320
    #294310962265680