def largestNumber(strNum: str) -> int:
    if len(strNum) < 2:
        return int(strNum)
    
    if( "0" in strNum):
        print("found zero in ")
        return -1
    #print(f"strNum: {strNum}")
    
    maxdigit = 0
    maxvalue = -1
    for i in range(len(strNum)):
        maxvalue = max(maxvalue, int(str(maxdigit)+ strNum[i])) 
        if( int(strNum[i]) >= maxdigit):
            maxdigit = int(strNum[i])
        #print(f"process: {strNum[:(i+1)]}, maxvalue: {maxvalue}, maxdigit: {maxdigit}")
    #print(f"maxvalues: {maxvalue}")
    return maxvalue

def read_file(path: str):
    with open(path,'r') as f:
        lines = f.readlines()
    # remove newline characters
    lines = [line.strip() for line in lines]
    return lines

def total_joltage(path:str)->int:
    lines = read_file(path)
    total = 0
    for line in lines[:20]:
        largest = largestNumber(line)
        total += largest
    return total

if __name__ == '__main__':

    print(total_joltage("input3-0.txt"))
