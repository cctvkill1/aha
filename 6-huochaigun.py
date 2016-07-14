
import sys
def countNum(x):
    num = 0
    numArr = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    while (int(x /10) !=0):
        num += numArr[x % 10]
        x = int(x / 10)
    num += numArr[x]
    return num

if __name__ == '__main__':
    print('火柴棍等式')
    m = 18 
    total = 0
    for x in range(0,1112):
        for y in range(0,1112):
            z = x + y
            # m 减去 加号和等号的4根
            if countNum(x)+countNum(y)+countNum(z) == m-4:
                print('%d+%d=%d' %(x , y , z))
                total+=1
    print('一共%d种不同的等式'%total)
    sys.exit(-1)
