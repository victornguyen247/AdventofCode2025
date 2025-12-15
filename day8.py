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

def total_clusters(n:int = 1000, min_heap, data):
    clusters = list()
    while n > 0:
        min_dis, node1, node2 = heapq.heappop(min_heap)
        
        n -= 1
    
if __name__ == "__main__":
    #part1
    data = load_data("input8-0.txt")
    min_heap = dis_list_asc(data)
    