import heapq
def load_data(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    data = list()
    for line in lines:
        data.append([int(val) for val in line.split(',')])    
    return data

def dis_list_asc(data):
    l = list()
    for i in range(len(data)):
        for j in range(i):
            [x1,y1,z1] = data[i]
            [x2,y2,z2] = data[j]
            dis = round(((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**(1/2),2)
            l.append([dis,data[i],data[j]])
    heapq.heapify(l)
    return l

def part1(min_heap, data,n = 1000):
    nodes = {}
    clusters = {}
    cluster_id = 1
    while n > 0:
        nodes, clusters, cluster_id,_,_ = connect(min_heap, nodes, clusters, cluster_id)
        n -= 1
    
    for node in data:
        node = str(node)
        if nodes.get(node) is None:
            nodes[node] = cluster_id
            clusters[cluster_id] = list([node])
            cluster_id += 1
    print(f"nodes: {nodes}")
    print(f"clusters: {clusters}")  
    
    largest_3 = list()
    for cluster_id in clusters.keys():
        n = len(clusters[cluster_id])
        if n not in largest_3:
            largest_3.append(n)
    largest_3 = sorted(largest_3, reverse = True)
    print("largest:", largest_3)
    product = largest_3[0] * largest_3[1] * largest_3[2]
    return product             
 
def connect(min_heap, nodes, clusters, cluster_id):
    min_dis, node1, node2 = heapq.heappop(min_heap)
    x1 = node1[0]
    x2 = node2[0]
    node1 = str(node1)
    node2 = str(node2)
    #print(f"node1: {node1}, node2: {node2}, dis:{min_dis}")
    if nodes.get(node1) == None and nodes.get(node2) == None:
        #print(f"create new cluster {cluster_id}")
        nodes[node1] = cluster_id
        nodes[node2] = cluster_id
        clusters[cluster_id]= list([node1,node2])
        #print(f"check cluster:{clusters[cluster_id]}")
        cluster_id += 1
    elif nodes.get(node1) == None and nodes.get(node2) != None:
        #print("add node1 into node 2 cluster ")
        nodes[node1] = nodes[node2]
        clusters[nodes[node2]].append(node1)
        #print("nodes:",nodes, "\n clusters:", clusters)
    elif nodes.get(node2) == None and nodes.get(node1) != None:
        #print("add node2 into node1 cluster ")
        nodes[node2] = nodes[node1]
        clusters[nodes[node1]].append(node2)
        #print("nodes:",nodes, "\n clusters:", clusters)
    else:
        if nodes[node1] != nodes[node2]:
            #print("union node2 cluster into node1")
            cluster_id_node2 = nodes[node2]
            cluster_id_node1 = nodes[node1]
            for node in clusters[cluster_id_node2]:
                nodes[node] = cluster_id_node1
                clusters[cluster_id_node1].append(node)
            clusters.pop(cluster_id_node2)  
            #print("nodes:",nodes, "\n clusters:", clusters)
        #else:
            #print("node1 and node2 same cluster")    
    return nodes, clusters, cluster_id, x1,x2
    
def part2(min_heap, n=1000):
    nodes = {}
    clusters = {}
    cluster_id = 1
    x1 = 0
    x2 =0
    while n > 0:
        nodes, clusters, cluster_id,_,_ = connect(min_heap, nodes, clusters, cluster_id)
        n -= 1
    for node in data:
        node = str(node)
        if nodes.get(node) is None:
            nodes[node] = cluster_id
            clusters[cluster_id] = list([node])
            cluster_id += 1
            
    while(len(clusters)>1):
        nodes, clusters, cluster_id, x1, x2 = connect(min_heap, nodes, clusters, cluster_id)
        print(f"x1:{x1}, x2:{x2}")
    
    return x1 * x2
    
if __name__ == "__main__": 
    data = load_data("input8-1.txt")
    #print(f"data: {data}")
    min_heap = dis_list_asc(data)
    #print(min_heap)
    #part1
    print(part1(min_heap.copy(), data, n= 10))
    #part2
    print(part2(min_heap.copy()))
    