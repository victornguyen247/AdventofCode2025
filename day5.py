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
        else:
            ids.append(int(line))
    return id_ranges, ids



