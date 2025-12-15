def load_data(path):
    with open(path, 'r') as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    return data

def count_tachyon(map):
    count = 0
    beam_pos = list()

    for j in range(len(map[0])):
        if map[0][j] == 'S':
            beam_pos.append(j)

    for i in range(len(map)):
        #if i %2 ==1: print(f"line {i+1}: {beam_pos}")
        pos = beam_pos.copy()
        for b in beam_pos:
            if(map[i][b] =='^'):
                count +=1
                if(map[i][b-1] != '^') and (b-1) not in pos:
                    pos.append(b-1)
                if(map[i][b+1] != '^') and (b+1) not in pos:
                    pos.append(b+1)
                pos.remove(b)
        beam_pos = pos.copy()
        if i %2 ==1:print(f"line {i+1}: {beam_pos}, {count}")

    return count

def count_split_beam(map):
    beam_pos = dict()
    for j in range(len(map[0])):
        if map[0][j] == 'S':
            beam_pos[j] = 1
    
    for i in range(0,len(map),2):
        #if i %2 ==1: print(f"line {i+1}: {beam_pos}")
        pos = beam_pos.copy()
        for b in beam_pos:
            #print(f"b:{b},pos:{pos}")
            if(map[i][b] =='^'):
                if(map[i][b-1] != '^'):
                    if pos.get(b-1) is None:
                        pos[b-1] = beam_pos[b]
                    else:
                        pos[b-1] += beam_pos[b]
                if(map[i][b+1] != '^'):
                    if pos.get(b+1) is None:
                        pos[b+1] = beam_pos[b] 
                    else:
                        pos[b+1] += beam_pos[b]
                pos.pop(b)  
        beam_pos = pos.copy()
        print(f"line {i+1}: {beam_pos} \n ---------------------------------")
    return sum(beam_pos.values())

if __name__ == "__main__":
    '''# part1
    map = load_data("input7-0.txt")     
    print(count_tachyon(map))'''

    #part2 
    map = load_data("input7-1.txt")
    print(count_split_beam(map))