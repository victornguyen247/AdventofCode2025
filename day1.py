import math
def find_password():
    input_list = get_input_list('day1_1.txt')
    #input_list = ["L68", "L30","R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    current = 50
    count = 0
    for line in input_list:
        if line[0] == "R":
            current += int(line[1:])
            current = current % 100
        elif line[0] == "L":
            current -= int(line[1:])
            if current < 0:
                current  = current % 100
        if current == 0:
            count += 1
    return count

def find_password2(input_list):
    current = 50
    count = 0
    for line in input_list:
        if line[0] == "R":
            current += int(line[1:])
            count += current // 100
            current = current % 100

        elif line[0] == "L":
            n = int(line[1:])
            count += ((100 - current) + n) // 100
            current = (current - n) % 100
    return count

def find_password3(input_list):    
    current = 50
    count = 0

    for line in input_list:
        direction = line[0]
        n = int(line[1:])

        if direction == "R":
            # zero is (100 - current) steps ahead
            first = (100 - current) % 100
            if first == 0:
                first = 100
            if n >= first:
                count += 1 + (n - first) // 100
            current = (current + n) % 100

        else:  # L
            # zero is current steps behind
            first = current
            if first == 0:
                first = 100
            if n >= first:
                count += 1 + (n - first) // 100
            current = (current - n) % 100

    return count

def get_input_list(path):
    with open(path, 'r') as file:
        input_list = file.readlines()
    return input_list   

if __name__ == '__main__':
    input_list = get_input_list('day1_1.txt')
    #input_list = ["L68", "L30","R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    print(find_password3(), find_password2(), (True if find_password2() == find_password3() else False ))
