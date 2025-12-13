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
        max_digit, index = maxdigit(strNum,s,e+1)
        lnum += str(max_digit)
        s = index +1
        e += 1
    return int(lnum)

def maxdigit(strNum: str,start:int, end:int):
    max_digit = 0
    index = -1
    #print(start, end)
    for i in range(start, end):
        if( int(strNum[i]) > max_digit):
            max_digit = int(strNum[i])
            index = i
            #print(f"max_digit: {max_digit}, index: {index}")
    return max_digit, index

def read_file(path: str):
    with open(path,'r') as f:
        lines = f.readlines()
    # remove newline characters
    lines = [line.strip() for line in lines]
    return lines

def total_joltage(path:str)->int:
    lines = read_file(path)
    total = 0
    for line in lines:
        #largest = largestNumber(line)
        largest = largestNum_len12(line)
        #print(f"largestNumber({line}) = {largest}")
        total += largest
    return total

def test_largestNumber():
    lines = read_file("input3-0.txt")
    for line in lines:
        result = largestNum_len12(line)
        print(f"largestNumber({line}) = {result}")

if __name__ == '__main__':

    print(total_joltage("input3-1.txt"))
    
