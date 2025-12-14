def prepare_data(path):
    with open(path, 'r') as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    id_ranges = []
    ids = []    
    for line in data:
        if "-" in line:
            start, end = line.split("-")
            id_ranges.append((int(start), int(end)))
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
    union = set()
    for (start, end) in id_ranges:
        merged = False
        for r in id_ranges:
            if check_overlap_2ranges((start, end), r):
                (start, end) = union_2sets((start, end), r)
                merged = True

def check_overlap_2ranges(r1, r2):
    (s1, e1) = r1
    (s2, e2) = r2
    if (s2 <= e1 and s2 >= s1) or (s1 <= e2 and s1 >= s2):
        return True
    return False
    
def union_2ranges(r1, r2):
    ''' 2 ranges need to be overlapping or contiguous '''
    (s1, e1) = r1
    (s2, e2) = r2
    urange = (min(s1, s2), max(e1, e2)) 
    return urange

if __name__ == "__main__":
    id_ranges, ids = prepare_data("input5-1.txt")
    num_fresh = validate_ids(id_ranges, ids)
    print(f"Number of valid IDs: {num_fresh}")


