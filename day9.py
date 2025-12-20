def load_data(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    data = list([[int(val) for val in line.split(',')] for line in lines])
    return data 

def part1(data):
    max_rec = 0
    for a in range(len(data)):
        for b in range(a-1):
            j1, i1 = data[a]
            j2, i2 = data[b]
            area = (abs(j2 - j1) +1) * (abs(i2 - i1) +1)
            #print(f"node: {data[a]},{data[b]}, area = {area}")
            max_rec = max(max_rec, area)
    return max_rec

def part2(data):
    valid_list = valid_zone(data)
    max_rec = 0
    for a in range(1,len(data)-1):
        for b in range(a):
            j1, i1 = data[a]
            j2, i2 = data[b]
            #print(f"node ({j1},{i1}):({j2},{i2})")
            valid = True
            for i in range(min(i1,i2),max(i1,i2)+1):
                ranges = blist[i]
                for k in range(0,len(ranges),2):
                    c = ranges[k]
                    d = ranges[k+1]
                    #print(f"+ row{i} range: {c},{d}")
                    min_j = min(j1,j2)
                    max_j = max(j1,j2)
                    if ranges[k] > min_j or max_j > ranges[k+1]:
                        valid = False 
                        break
                if not valid:
                    break
            if valid:
                area = (abs(j2 - j1) +1) * (abs(i2 - i1) +1)
                #print(f"node: {data[a]},{data[b]}, area = {area}")
                max_rec = max(max_rec, area)
    print(max_rec)
    return max_rec

def valid_zone(data):
    ver_zone = {}
    hor_zone = {}
    for k in range(-1,len(data)-1):
        j1, i1 = data[k]
        j2, i2 = data[k+1]
        #print(f"node {i1},{j1} and {i2},{j2}")
        if (j1 == j2):
            if ver_zone.get(j1) is None:
                ver_zone[j1] = list([min(i1,i2), max(i1,i2)])
            else:
                ver_zone[j1].append([min(i1,i2), max(i1,i2)])
        elif(i1 == i2):
            if hor_zone.get(i1) is None:
                hor_zone[i1] = list([min(j1,j2), max(j1,j2)])
            else:
                hor_zone[i1].append([min(j1,j2), max(j1,j2)])    
    
    '''#print("green_red tiles:",gr_tile)
    blist = {}
    for node in gr_tile:
        i,j = node 
        if blist.get(i) is None:
            blist[i]= list([j])
        else:
            blist[i].append(j)
    #print("black list:",blist)
    for id,val in blist.items():
        if len(val)%2==1:
            blist[id].pop(-2)'''
    return ver_zone, hor_zone
    
def part2_2(data):
    ver_zone, hor_zone = valid_zone(data)
    for a in range(1,len(data)-1):
        for b in range(a):                 
    
if __name__ == "__main__":
    data = load_data("input9-1.txt")
    #print(part1(data))
    #print("data:",data)
    part2(data)