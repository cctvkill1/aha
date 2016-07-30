# 宝岛探险 广度优先搜索 (队列版)
import sys
import random 
import queue

if __name__ == '__main__':
    print('宝岛探险 广度优先搜索')
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
    q = queue.Queue(maxsize = n*m+1)
    book[startX][startY] = 1  
    row = {'x': startX, 'y': startY}
    q.put(row)
    sumNum += 1
    flag = 0
    while q.qsize() != 0:
        now = q.get()
        print(now,q.qsize(),q.qsize())
        nowX = now['x']
        nowY = now['y']
        for k in range(4): 
            tx = nowX + next[k][0]
            ty = nowY + next[k][1]
            # 是否越界
            if tx < 0 or tx >= n or ty < 0 or ty >= m:
                continue
            if labyrinthMap[tx][ty] > 0 and book[tx][ty] == 0:
                book[tx][ty] = 1
                row = {'x': tx, 'y': ty}
                q.put(row)
                sumNum+=1
        

    for x in range(n):
        print(labyrinthMap[x])  
    print('小岛大小为%d' % sumNum)
    sys.exit(-1)
