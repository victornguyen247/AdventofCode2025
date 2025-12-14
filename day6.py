import re
import math
def prepare_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines if line.strip()]
    data =[]
    for line in lines:
        data.append(re.split(r"\s+", line))
    return data

def total_answers(data):
    total =0
    for j in range(len(data[0])):
        if(data[len(data)-1][j] == '+'):
            for i in range(len(data)-1):
                total += int(data[i][j])
        elif(data[len(data)-1][j] == '*'):
            prod =1
            for i in range(len(data)-1):
                prod *= int(data[i][j])
            total += prod
    return total

def check_valid_data(data):
    rows = len(data)
    cols = len(data[0])
    for i in range(len(data)):
        if len(data[i]) != cols:
            return False
    return True

def load_data(path):
    with open(path, 'r') as file:
        data = file.readlines()
    for i in range(len(data)):
        if data[i].endswith('\n'):
            data[i] = data[i][:-1]
    return data

def total_v2(data):
    total = 0
    queue = list()
    for j in range(len(data[0])-1,-1,-1):
        num = ""
        for i in range(len(data)-1):
            if (data[i][j] != ' '):
                num += data[i][j]
        num.strip()
        if (len(num)>0):
            queue.append(int(num))
        if (data[len(data)-1][j] == "+"):
            total += sum(queue)
            queue.clear()
        elif(data[len(data)-1][j] == "*"):
            total += math.prod(queue)
            queue.clear()
    
    return total

if __name__ == "__main__":
    '''#path1
    data = prepare_data('input6-1.txt')
    #print(check_valid_data(data))
    print(total_answers(data))'''

    #path2
    data = load_data('input6-1.txt')
    print(total_v2(data))
