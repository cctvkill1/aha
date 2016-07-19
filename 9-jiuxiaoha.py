# 解救小哈 最短路径搜索
import sys
import random


def dfs(x, y, step):
    global next
    global minStep
    global n
    global m
    global endX
    global endY
    global book
    global labyrinthMap 
    if x == endX and y == endY: 
        print (step)
        if step < minStep:
            minStep = step
            print(minStep, '----over')
        return
    for k in range(4):
        tx = x + next[k][0]
        ty = y + next[k][1]

        if tx < 0 or tx >= n or ty < 0 or ty >= m:
            continue  
        if labyrinthMap[tx][ty] == 0 and book[tx][ty] == 0:
            book[tx][ty] = 1 
            dfs(tx, ty, step + 1)
            book[tx][ty] = 0 
    return

if __name__ == '__main__':
    print('解救小哈 最短路径  深度优先搜索')
    # n = random.randint(5, 10)
    # m = random.randint(5, 10)
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
    # for x in range(n):
    #     for y in range(m):
    #         # print(x,'-',y)
    #         labyrinthMap[x][y] = random.randint(0, 1)
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
    # endX = random.randint(1, n-1)
    # endY = random.randint(1, m-1)
    endX = 3
    endY = 2 
    book[startX][startY] = 1
    dfs(startX, startY, 0) 
    for x in range(n):
        print(labyrinthMap[x]) 
    print('最短路径%d步' % minStep)
    sys.exit(-1)
