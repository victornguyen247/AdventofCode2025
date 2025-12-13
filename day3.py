def largestNumber(strNum: str) -> int:
    if len(strNum) < 2:
        return int(strNum)
    
    if( "0" in strNum):
        print("found zero in ")
        return -1
    
    num1 = "0"
    num2 = strNum[0]
    for i in range(1,len(strNum)):
        if int(strNum[i]) > int(num2):
            num1 = num2
            num2 = strNum[i]
    
    num4 ="0"
    num3 = strNum[len(strNum)-1]
    for i in range(len(strNum)-2, -1, -1):
        if int(strNum[i]) > int(num3):
            num4 = num3
            num3 = strNum[i]

    num12 = int(num1 + num2)
    if num4 == "0":
        num34 = int(num3)
    else:
        num34 = int(num3 + num4)
    return max(num12, num34)

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
        largest = largestNumber(line)
        total += largest
    return total

if __name__ == '__main__':

    print(total_joltage("input3-1.txt"))
