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
    gb_tile = list() 
    for k in range(len(data)-1):
        j1, i1 = data[k]
        j2, i2 = data[k+1]
        if (j1 == j2):
            (i1,i2) = (i2,i1) if i2 < i1 else (i1,i2) 
            for m in range(i1,i2):
                gb_tile.append([m,j1])
        elif i1 == i2:
            (j1,j2) = (j2,j1) if j2 < j1 else (j1,j2) 
            for m in range(j1,j2):
                gb_tile.append([i1,m])
    gb_tile = sorted(gb_tile, key=lambda x: x[1])   
    gb_tile = sorted(gb_tile, key=lambda x: x[0])
    cp_gb = gb_tile.copy()
    for i in range(len(gb_tile)-1):
        if gb_tile[i] == gb_tile[i+1]:
            cp_gb.pop(i)
    gb_tile = cp_gb
    print(gb_tile)
    
    blist = set()
    min_i = gb_tile[0][0]
    max_i = gb_tile[len(gb_tile)-1][0]
    for node in gb_tile:
        
                   
                    
        
        

if __name__ == "__main__":
    data = load_data("input9-0.txt")
    #print(part1(data))
    part2(data)