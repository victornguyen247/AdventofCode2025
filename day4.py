def accessible(map, posi:int, posj:int) -> bool:
    adjecent_positions = [
        (posi - 1, posj -1),
        (posi    , posj -1),
        (posi + 1, posj -1),
        (posi - 1, posj    ),
        (posi + 1, posj    ),
        (posi - 1, posj +1),
        (posi    , posj +1),
        (posi + 1, posj +1),
    ]
    count = 0
    for (i, j) in adjecent_positions:
        if 0 <= i < len(map) and 0 <= j < len(map[0]):
            if map[i][j] == '@':
                count += 1
    return True if count <4 else False

def total_accessible(map) -> int:
    total = 0
    list_accessible = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '@' and accessible(map, i,j):
                list_accessible.append((i,j))
                total += 1
    
    #show_map(map, list_accessible)
    return total

def total_accessible_2(map) -> int:
    total = -1
    list_accessible = []
    
    while len(list_accessible)>0 or total==-1: 
        total = max(0,total)
        list_accessible = []
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == '@' and accessible(map, i,j):
                    list_accessible.append((i,j))
                    total += 1
        map = remove_accessible(map, list_accessible)

    #show_map(map, list_accessible)
    return total

def prepare_map(path: str) -> list:
    with open(path, 'r') as f:
        map = f.readlines()
    map = [list(line.strip()) for line in map]
    return map

def remove_accessible(map, marklist):
    for (i,j) in marklist:
        map[i][j] = '.'
    return map

def show_map(map, marklist):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (i,j) in marklist:
                print('X', end='')
            else:
                print(map[i][j], end='')
        print()

if __name__ == "__main__":
    map = prepare_map('input4-1.txt')
    print(total_accessible(map))
    print(total_accessible_2(map))