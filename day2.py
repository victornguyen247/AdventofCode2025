def is_invalid(num:int):
    strNum = str(num)
    n = len(strNum)
    if(n % 2 ==1 ): return False

    r = False
    i = 0 
    j = int(n/2)
    while(i < n/2):
        if strNum[i] != strNum[j]:
            return False
        i+=1 
        j+=1

    return True 

def is_invalid_v2(num :int)-> bool:
    strNum = str(num)
    n = len(strNum)

    if n < 2:
        return False
    
    invalid = True
    for l in range(1,(n//2)+1):
        if n % l != 0:
            continue
        
        invalid = True
        for i in range(l):
            for j in range(l,n-l+1,l): 
                if strNum[i] != strNum[i+j]:
                    invalid = False
                    break
            if not invalid:
                break
        if invalid:
            break
    return invalid
    

def get_invalid(start: int, end: int)->list:
    arr = []
    for i in range(start,end+1, 1):
        # if (is_invalid(i)):
        if (is_invalid_v2(i)):
            arr.append(i)
    return arr

def read_file(path: str):
    with open(path,'r') as f:
        line = f.readline()  
    lines = line.split(',')
    inputlist =[]
    for v in lines:
        s,e = v.split("-")
        s = int(s)
        e = int(e)      
        inputlist.append((s,e))
    return inputlist

def total_invalid(inputlist)-> int:
    total = 0
    for (s,e) in inputlist:
        arr = get_invalid(s,e)
        total += sum(arr)
    
    return total


if __name__ == '__main__':
    inputlist = read_file("input2-1.txt")
    print(total_invalid(inputlist))
    #4174379265 
    #34421651192