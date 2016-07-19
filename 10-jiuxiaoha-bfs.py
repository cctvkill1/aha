# 解救小哈 最短路径搜索  广度优先搜索
import sys
import random
from collections import deque


def bfs(x, y, step):
    global next
    global minStep
    global n
    global m
    global endX
    global endY
    global book
    global labyrinthMap
    # print(step)
    print(labyrinthMap[x][y])
    if x == endX and y == endY: 
        if step < minStep:
            minStep = step
            pritn(minStep, '----over')
        return
    for k in range(4):
        tx = x + next[k][0]
        ty = y + next[k][1]
        if tx < 0 or tx >= n or ty < 0 or ty >= m:
            continue
        if labyrinthMap[tx][ty] == 0 and book[tx][ty] == 0:
            book[tx][ty] = 1
            # print(book)
            dfs(tx, ty, step + 1)
            book[tx][ty] = 0
    print('for-over')
    return

if __name__ == '__main__':
    print('解救小哈 最短路径  广度优先搜索')
    n = 5
    m = 4
    next = [([0] * 2) for i in range(4)]
    next[0][1] = 1
    next[1][0] = 1
    next[2][1] = -1
    next[3][0] = -1
    book = [([0] * m) for i in range(n)]
    labyrinthMap = [([0] * m) for i in range(n)]
    print(n, '-', m)
    # 迷宫地图 0是空地 1是障碍物
    labyrinthMap[0][0] = 0
    labyrinthMap[0][1] = 0
    labyrinthMap[0][2] = 1
    labyrinthMap[0][3] = 0
    labyrinthMap[1][0] = 0
    labyrinthMap[1][1] = 0
    labyrinthMap[1][2] = 0
    labyrinthMap[1][3] = 0
    labyrinthMap[2][0] = 0
    labyrinthMap[2][1] = 0
    labyrinthMap[2][2] = 1
    labyrinthMap[2][3] = 0
    labyrinthMap[3][0] = 0
    labyrinthMap[3][1] = 1
    labyrinthMap[3][2] = 0
    labyrinthMap[3][3] = 0
    labyrinthMap[4][0] = 0
    labyrinthMap[4][1] = 0
    labyrinthMap[4][2] = 0
    labyrinthMap[4][3] = 1
    startX = startY = 0
    minStep = 99999999
    endX = 3
    endY = 2
    book[startX][startY] = 1
    qList = []
    row = {'x': startX, 'y': startY, 'f': 0, 's': 0}
    qList.append(row)
    flag = 0
    while len(qList) != 0:
        for k in range(4):
            tx =  qList[0]['x']+next[k][0]
            ty =  qList[0]['y']+next[k][1]
            if tx < 0 or tx >= n or ty < 0 or ty >= m:
                continue
            if labyrinthMap[tx][ty] == 0 and book[tx][ty] == 0:
                book[tx][ty] = 1
                row = {'x': tx, 'y': ty, 'f': 0, 's': qList[0]['s']+1}
                qList.append(row) 
            if tx == endX and ty == endY: 
                flag = 1
                break
        if flag==1:
            break            
        del qList[0]

    for x in range(n):
        print(labyrinthMap[x])
    print(book)
    print(qList)
    if(len(qList)==0):
        print('无最短路径')
    else:
        print('最短路径%d步' % qList[len(qList)-1]['s'])
    sys.exit(-1)
