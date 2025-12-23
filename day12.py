from collections import defaultdict
def load_data(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    presents = defaultdict(list)
    for i in range(0,30,5):
        shape = list()
        for a in range(3):
            r = list()
            for b in range(3):
                if lines[i+1+a][b] == '#':
                    r.append(1)
                elif lines[i+1+a][b] == '.':
                    r.append(0)
            shape.append(r)
        presents[int(lines[i][0])] = shape
        
    rule = list()
    for i in range(30,len(lines)):
        print(lines[i])
        if len(lines[i]) > 1:
            size, requirement = lines[i].split(':')
            size = [int(x) for x in size.split('x')]
            requirement = [int(x) for x in requirement.split()]
            rule.append([size, requirement])
    return presents, rule

def part1(presents, rule):
    

if __name__ == "__main__":
    print(load_data('input12-0.txt'))
            