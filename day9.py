
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
    ver_zone, hor_zone = valid_zone(data)
    #print("ver_zone:", ver_zone)
    #print("hor_zone:", hor_zone)
    max_rec = 0
    for a in range(1,len(data)-1):
        for b in range(a):
            j1, i1 = data[a]
            j2, i2 = data[b]
            #print(f"node {i1},{j1} -- {i2},{j2}")
            (i1,i2) = (i1,i2) if i1 < i2 else (i2,i1)
            (j1,j2) = (j1,j2) if j1 < j2 else (j2,j1)
            valid = False
            for k in range(0,len(hor_zone[i1]),2):
                f = hor_zone[i1][k]
                s = hor_zone[i1][k+1]
                if f <= j1 and j2 <= s:
                    valid = True
                    break
            if not valid: continue
            valid = False
            for k in range(0,len(hor_zone[i2]),2):
                f = hor_zone[i2][k]
                s = hor_zone[i2][k+1]
                if f <= j1 and j2 <= s:
                    valid = True
                    break
            if not valid: continue
            valid = False
            for k in range(0,len(ver_zone[j1]),2):
                f = ver_zone[j1][k]
                s = ver_zone[j1][k+1]
                if f <= i1 and i2 <= s:
                    valid = True
                    break
            if not valid: continue
            valid = False
            for k in range(0,len(ver_zone[j2]),2):
                f = ver_zone[j1][k]
                s = ver_zone[j1][k+1]
                if f <= i1 and i2 <= s:
                    valid = True
                    break
            if not valid: continue 
            
            area = (abs(j2 - j1) +1) * (abs(i2 - i1) +1)
            #print(f"node: {data[a]},{data[b]}, area = {area}")
            max_rec = max(max_rec, area)
    print(max_rec)
    return max_rec

def valid_zone(data):
    """data -> vertical_ranges, horizontal_ranges"""
    ver_zone = {}
    hor_zone = {}
    i_list = list()
    j_list = list()
    for j,i in data:
        if j not in j_list:
            j_list.append(j)
        if i not in i_list:
            i_list.append(i)
    for k in range(-1,len(data)-1):
        j1, i1 = data[k]
        j2, i2 = data[k+1]
        #print(f"node {i1},{j1} and {i2},{j2}")
        if (j1 == j2):
            (i1,i2) = (i2,i1) if i2 < i1 else (i1,i2) 
            filter_l = [x for x in i_list if i1 <= x <=i2]
            #print(f"filter: {filter_l}")
            for m in filter_l:
                if hor_zone.get(m) is None:
                    hor_zone[m] = list([j1])
                else:
                    hor_zone[m].append(j1)
        elif (i1 == i2):
            (j1,j2) = (j2,j1) if j2 < j1 else (j1,j2) 
            filter_l = [y for y in j_list if j1 <= y <=j2]
            #print(f"filter: {filter_l}")
            for m in filter_l:
                if ver_zone.get(m) is None:
                    ver_zone[m] = list([i1])
                else:
                    ver_zone[m].append(i1)                     
    for id,val in hor_zone.items():
        if len(val)%2 == 1:
            hor_zone[id] = sorted(hor_zone[id])
            hor_zone[id].pop(-2)
        else: 
            hor_zone[id] = sorted(hor_zone[id])
    for id,val in ver_zone.items():
        if len(val)%2 == 1:
            ver_zone[id] = sorted(ver_zone[id])
            ver_zone[id].pop(-2)
        else:
            ver_zone[id] = sorted(ver_zone[id])
    
    return ver_zone, hor_zone

def sort_pair(a: int, b :int):
    return (a,b) if a < b else (b,a)

def check_collapse(edges, rec: tuple):
    (min_x, min_y, max_x, max_y) = rec
    for e in edges:
        (x1,y1,x2,y2) = e
        if (min_x < x2 and max_x > x1 and min_y < y2 and max_y > y1):
            return True
    return False    

def part2_optimal(data: list):
    edges= list()
    for k in range(-1,len(data)-1):
        x1,y1 = data[k]
        x2,y2 = data[k+1]
        edges.append((min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2)))
    
    max_area = 0
    for i in range(1,len(data)):
        for j in range(i):
            x1,y1 = data[i]
            x2,y2 = data[j]
            (x1,x2) = sort_pair(int(x1),int(x2))
            (y1,y2) = sort_pair(int(y1), int(y2))
            if not check_collapse(edges, (x1,y1,x2,y2)):
                area = abs(x2-x1+1) * abs(y2 -y1+1)
                max_area = max(max_area, area)
    return max_area

if __name__ == "__main__":
    data = load_data("input9-1.txt")
    #print(part1(data))
    #print("data:",data)
    print(part2_optimal(data))
    
    # wrong: 1516832966
    #        1613305596