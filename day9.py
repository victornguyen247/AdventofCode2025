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

from collections import defaultdict
import bisect

# ------------------------------------------------------------
# Step 1: Build filled polygon interior (scanline fill)
# ------------------------------------------------------------

def build_inside_intervals(data):
    """
    Returns:
        inside[y] = sorted list [x1, x2, x3, x4, ...]
        meaning intervals [x1,x2), [x3,x4), ...
    """
    edges = []
    n = len(data)

    # build edges
    for i in range(n):
        x1, y1 = data[i]
        x2, y2 = data[(i + 1) % n]
        if y1 == y2:
            continue  # horizontal edges ignored for scanline
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        edges.append((x1, y1, y2))

    inside = defaultdict(list)

    min_y = min(y for _, y in data)
    max_y = max(y for _, y in data)

    for y in range(min_y, max_y):
        xs = []
        for x, y1, y2 in edges:
            if y1 <= y < y2:
                xs.append(x)
        xs.sort()
        for i in range(0, len(xs), 2):
            inside[y].append(xs[i])
            inside[y].append(xs[i + 1])

    return inside


# ------------------------------------------------------------
# Step 2: Main Part 2 logic
# ------------------------------------------------------------

def part2_2(data):
    inside = build_inside_intervals(data)

    # group red points by row
    reds_by_y = defaultdict(list)
    for x, y in data:
        reds_by_y[y].append(x)

    for y in reds_by_y:
        reds_by_y[y].sort()

    ys = sorted(reds_by_y.keys())
    max_area = 0

    # try all pairs of red rows
    for i in range(len(ys)):
        y1 = ys[i]
        for j in range(i + 1, len(ys)):
            y2 = ys[j]
            height = y2 - y1
            if height <= 0:
                continue

            # intersect inside intervals for rows y1 .. y2-1
            current = None
            valid = True

            for y in range(y1, y2):
                if y not in inside:
                    valid = False
                    break
                intervals = inside[y]

                if current is None:
                    current = intervals[:]
                else:
                    new = []
                    p1 = p2 = 0
                    while p1 < len(current) and p2 < len(intervals):
                        a1, a2 = current[p1], current[p1 + 1]
                        b1, b2 = intervals[p2], intervals[p2 + 1]
                        lo = max(a1, b1)
                        hi = min(a2, b2)
                        if lo < hi:
                            new.extend([lo, hi])
                        if a2 < b2:
                            p1 += 2
                        else:
                            p2 += 2
                    current = new
                    if not current:
                        valid = False
                        break

            if not valid:
                continue

            # choose widest rectangle using red corners
            top = reds_by_y[y1]
            bot = reds_by_y[y2]

            for k in range(0, len(current), 2):
                L, R = current[k], current[k + 1]

                # leftmost red >= L
                i1 = bisect.bisect_left(top, L)
                j1 = bisect.bisect_left(bot, L)
                if i1 >= len(top) or j1 >= len(bot):
                    continue

                # rightmost red <= R
                i2 = bisect.bisect_right(top, R) - 1
                j2 = bisect.bisect_right(bot, R) - 1
                if i2 < 0 or j2 < 0:
                    continue

                x_left = max(top[i1], bot[j1])
                x_right = min(top[i2], bot[j2])

                if x_left < x_right:
                    area = (x_right - x_left) * height
                    max_area = max(max_area, area)

    return max_area



                    
if __name__ == "__main__":
    data = load_data("input9-1.txt")
    #print(part1(data))
    #print("data:",data)
    print(part2_2(data))
    
    # wrong: 1516832966