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
    i_list = [y for x,y in data]
    i_list = i_list.sort()
    j_list = [x for x,y in data] 
    j_list = j_list.sort()
    for k in range(-1,len(data)-1):
        j1, i1 = data[k]
        j2, i2 = data[k+1]
        #print(f"node {i1},{j1} and {i2},{j2}")
        if (j1 == j2):
            (i1,i2) = (i2,i1) if i2 < i1 else (i1,i2) 
            filter_l = [x for x in i_list if i1 <= x <=i2]
            for m in filter_l:
                if hor_zone.get(m) is None:
                    hor_zone[m] = list([j1])
                else:
                    hor_zone[m].append([j1])
        if (i1 == i2):
            (j1,j2) = (j2,j1) if j2 < j1 else (j1,j2) 
            filter_l = [y for y in j_list if j1 <= y <=j2]
            for m in filter_l:
                if ver_zone.get(m) is None:
                    ver_zone[m] = list([i1])
                else:
                    ver_zone[m].append([i1])            
            
    for id,val in hor_zone.items():
        if len(val)%2 == 1:
            hor_zone[id].pop(-2)
    for id,val in ver_zone.items():
        if len(val)%2 == 1:
            ver_zone[id].pop(-2)
    print(f"ver_zone: \n{ver_zone},\n hor_zone: \n{hor_zone}")
    return ver_zone, hor_zone
                    
if __name__ == "__main__":
    data = load_data("input9-1.txt")
    #print(part1(data))
    #print("data:",data)
    #part2(data)
    valid_zone(data)