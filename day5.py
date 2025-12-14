def prepare_data(path):
    with open(path, 'r') as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    id_ranges = []
    ids = []    
    for line in data:
        if "-" in line:
            start, end = line.split("-")
            id_ranges.append([int(start), int(end)])
        elif line != "":
            ids.append(int(line))
    return id_ranges, ids

def validate_ids(id_ranges, ids):
    num_fresh = 0
    for id in ids:
        for start, end in id_ranges:
            if start <= id  and  id <= end:
                num_fresh += 1
                break
    return num_fresh

def total_fresh_ids(id_ranges):
    id_ranges = sorted(id_ranges, key=lambda x: x[0])
    i = 0
    while i < len(id_ranges)-1:
        if (check_overlap_2ranges(id_ranges[i], id_ranges[i+1])):
            id_ranges[i] = union_2ranges(id_ranges[i], id_ranges[i+1])
            id_ranges.pop(i+1)
        else: i += 1

    print("final ranges:", id_ranges)
    total = 0
    print("===================")
    for (s, e) in id_ranges:
        print("range:", (s, e))
        total += (e - s + 1)
    return total

def check_overlap_2ranges(r1, r2):
    [s1, e1] = r1
    [s2, e2] = r2
    if (s2 <= e1 and s2 >= s1) or (s1 <= e2 and s1 >= s2) or \
        (s1 <= s2 and e2<= e1) or (s1 >= s2 and e2 >= e1):
        return True
    return False
    
def union_2ranges(r1, r2):
    ''' 2 ranges need to be overlapping or contiguous '''
    [s1, e1] = r1
    [s2, e2] = r2
    urange = [min(s1, s2), max(e1, e2)] 
    print("Union", r1, r2, ":", urange)
    return urange

if __name__ == "__main__":
    id_ranges, ids = prepare_data("input5-1.txt")
    #num_fresh = validate_ids(id_ranges, ids)
    #print(f"Number of valid IDs: {num_fresh}")
    print("total fresh ids:", total_fresh_ids(id_ranges))

