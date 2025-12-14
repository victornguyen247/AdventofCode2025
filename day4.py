def accessible(map, posy:int, posx:int) -> bool:
    adjecent_positions = [
        (posx - 1, posy -1),
        (posx    , posy -1),
        (posx + 1, posy -1),
        (posx - 1, posy    ),
        (posx + 1, posy    ),
        (posx - 1, posy +1),
        (posx    , posy +1),
        (posx + 1, posy +1),
    ]
    count = 0
    for (x, y) in adjecent_positions:
        if 0 <= x < len(map[0]) and 0 <= y < len(map):
            if map[y][x] == '@':
                count += 1
    return True if count <4 else False

def total_accessible(map) -> int:
    total = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '@' and accessible(map, y, x):
                total += 1
    return total
def prepare_map(path: str) -> list:
    with open(path, 'r') as f:
        map = f.read_lines()
    return map

if __name__ == "__main__":
    map = prepare_map('input4-0.txt')
    print(total_accessible(map))