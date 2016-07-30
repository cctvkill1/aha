# 宝岛探险 深度优先搜索 (Floodfill漫水填充法也称种子填充法)
import sys
import random


def dfs(x, y,color):
    global next  
    global book
    global mapList 
    global sumNum  
    mapList[x][y] = color
    for k in range(4):
        tx = x + next[k][0]
        ty = y + next[k][1]
        if tx < 0 or tx >= n or ty < 0 or ty >= m:
            continue  
        if mapList[tx][ty] > 0 and book[tx][ty] == 0:
            book[tx][ty] = 1 
            mapList[tx][ty] = color
            sumNum+=1
            dfs(tx, ty,color) 
    return

if __name__ == '__main__':
    print('宝岛探险 深度优先搜索(Floodfill漫水填充法也称种子填充法)')
    n = 10
    m = 10
    next = [([0] * 2) for i in range(4)]
    next[0][1] = 1
    next[1][0] = 1
    next[2][1] = -1
    next[3][0] = -1
    book = [([0] * m) for i in range(n)]
    mapList = [([0] * m) for i in range(n)]
    print(n, '-', m)
    # 地图 0是海洋 大于0的是陆地
    for x in range(n):
        for y in range(m):
            # print(x,'-',y)
            mapList[x][y] = random.randint(0, 2) 
    num = 0
    sumNum = 0  

    for x in range(n):
        for y in range(m): 
            if(mapList[x][y]>0):
                book[x][y] = 1 
                num-=1# 这里是小于零的数 不然mapList染色大于0 循环后会乱
                dfs(x, y,num)  
                print('岛大小为%d' % sumNum)
                sumNum = 0  
    
    for x in range(n):
        print(mapList[x])  
    print('一共有%d个岛' %-num)
    sys.exit(-1)