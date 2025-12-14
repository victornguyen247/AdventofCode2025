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
    valid_ids = {}
    for (start, end) in id_ranges:
        for id_ in range(start, end + 1):
            if valid_ids.get(id_) is None:
                valid_ids[id_] = True
    
    num_fresh = 0
    for id_ in ids:
        if valid_ids.get(id_) == True:
            num_fresh += 1

    return num_fresh

if __name__ == "__main__":
    id_ranges, ids = prepare_data("input5-0.txt")
    num_fresh = validate_ids(id_ranges, ids)
    print(f"Number of valid IDs: {num_fresh}")


