def largestNumber(strNum: str) -> int:
    if len(strNum) ==0:
        return -1
    if len(strNum) < 2:
        return int(strNum)

    maxdigit = 0
    maxvalue = -1
    for i in range(len(strNum)):
        maxvalue = max(maxvalue, int(str(maxdigit)+ strNum[i])) 
        if( int(strNum[i]) >= maxdigit):
            maxdigit = int(strNum[i])
        #print(f"process: {strNum[:(i+1)]}, maxvalue: {maxvalue}, maxdigit: {maxdigit}")
    print(f"maxvalues: {maxvalue}")
    return maxvalue

def largestNum_len12(strNum: str) -> int:
    if len(strNum) ==0:
        return -1
    if len(strNum) <= 12:
        return int(strNum)
    
    lnum = ""
    s = 0
    e = len(strNum) - 12
    for i in range(12):
        maxdigit, index = maxdigit(strNum,s,e)
        lnum += str(maxdigit)
        s = index
        e += 1
    return int(lnum)

def maxdigit(strNum: str,start:int, end:int):
    maxdigit = 0
    index = -1
    for i in range(start, end+1):
        if( int(strNum[i]) >= maxdigit):
            maxdigit = int(strNum[i])
            index = i
    return maxdigit, index

def read_file(path: str):
    with open(path,'r') as f:
        lines = f.readlines()
    # remove newline characters
    lines = [line.strip() for line in lines]
    return lines

def total_joltage(path:str, end:int = 100)->int:
    lines = read_file(path)
    total = 0
    for line in lines[:end]:
        largest = largestNumber(line)
        total += largest
    return total

def test_largestNumber():
    lines = read_file("test3-0.txt")
    for line in lines:
        result = largestNum_len12(line)
        print(f"largestNumber({line}) = {result}")

if __name__ == '__main__':

    #print(total_joltage("input3-1.txt", 20))
    print(total_joltage("input3-0.txt"))
