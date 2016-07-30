# 宝岛探险 深度优先搜索 (染色)
import sys
import random


def dfs(x, y,color):
    global next  
    global book
    global labyrinthMap 
    global sumNum  
    for k in range(4):
        tx = x + next[k][0]
        ty = y + next[k][1]
        if tx < 0 or tx >= n or ty < 0 or ty >= m:
            continue  
        if labyrinthMap[tx][ty] > 0 and book[tx][ty] == 0:
            book[tx][ty] = 1 
            labyrinthMap[tx][ty] = color
            sumNum+=1
            dfs(tx, ty,color)
            # book[tx][ty] = 0 
            # 这步一定不能要 不然那死递归里了 
    return

if __name__ == '__main__':
    print('宝岛探险 深度优先搜索')
    n = 10
    m = 10
    next = [([0] * 2) for i in range(4)]
    next[0][1] = 1
    next[1][0] = 1
    next[2][1] = -1
    next[3][0] = -1
    book = [([0] * m) for i in range(n)]
    labyrinthMap = [([0] * m) for i in range(n)]
    print(n, '-', m)
    # 地图 0是海洋 大于0的是陆地
    for x in range(n):
        for y in range(m):
            # print(x,'-',y)
            labyrinthMap[x][y] = random.randint(0, 10)
    startX = 6
    startY = 8
    sumNum = 0   
    dfs(startX, startY,-1) 
    
    for x in range(n):
        print(labyrinthMap[x])  
    print('小岛大小为%d' % sumNum)
    sys.exit(-1)