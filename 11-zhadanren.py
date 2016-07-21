# 再解读炸弹人（上次炸弹人解出来地图上哪一点灭最多，但是没有判断这个点是否可以走过去）利用广度优先搜索 探路
import sys
import random   

def getNum(i,j):
    global labyrinthMap
    sumNum = 0
    # 统计四个方向可以炸的敌人数
    x = i
    y = j
    while labyrinthMap[x][y]!='#':
        if(labyrinthMap[x][y]=='G'):
            sumNum += 1
        x-=1
    x = i
    y = j
    while labyrinthMap[x][y]!='#':
        if(labyrinthMap[x][y]=='G'):
            sumNum += 1
        x+=1
    x = i
    y = j
    while labyrinthMap[x][y]!='#':
        if(labyrinthMap[x][y]=='G'):
            sumNum += 1
        y-=1
    x = i
    y = j
    while labyrinthMap[x][y]!='#':
        if(labyrinthMap[x][y]=='G'):
            sumNum += 1
        y+=1

    return sumNum

if __name__ == '__main__':
    print('再解炸弹人 利用广度优先搜索探路 ')
    n = 13
    m = 13
    next = [([0] * 2) for i in range(4)]
    next[0][1] = 1
    next[1][0] = 1
    next[2][1] = -1
    next[3][0] = -1
    book = [([0] * m) for i in range(n)]
    labyrinthMap = [([0] * m) for i in range(n)]
    print(n, '-', m)
    # 地图 #是墙（可以炸穿透） G是敌人 .是空地 墙不能走不能放炸弹 敌人和空地可以走也可以放炸弹
    for x in range(n):
        for y in range(m):
            # print(x,'-',y)
            labyrinthMap[x][y] =  '#' if random.randint(0, 1) == 1 else 'G' 
    labyrinthMap[0][0] = '#'
    labyrinthMap[0][1] = '#'
    labyrinthMap[0][2] = '#'
    labyrinthMap[0][3] = '#'
    labyrinthMap[0][4] = '#'
    labyrinthMap[0][5] = '#'
    labyrinthMap[0][6] = '#'
    labyrinthMap[0][7] = '#'
    labyrinthMap[0][8] = '#'
    labyrinthMap[0][9] = '#'
    labyrinthMap[0][10] = '#'
    labyrinthMap[0][11] = '#'
    labyrinthMap[0][12] = '#'
    labyrinthMap[1][0] = '#'
    labyrinthMap[1][1] = 'G'
    labyrinthMap[1][2] = 'G'
    labyrinthMap[1][3] = '.'
    labyrinthMap[1][4] = 'G'
    labyrinthMap[1][5] = 'G'
    labyrinthMap[1][6] = 'G'
    labyrinthMap[1][7] = '#'
    labyrinthMap[1][8] = 'G'
    labyrinthMap[1][9] = 'G'
    labyrinthMap[1][10] = 'G'
    labyrinthMap[1][11] = '.'
    labyrinthMap[1][12] = '#'
    labyrinthMap[2][0] = '#'
    labyrinthMap[2][1] = '#'
    labyrinthMap[2][2] = '#'
    labyrinthMap[2][3] = '.'
    labyrinthMap[2][4] = '#'
    labyrinthMap[2][5] = 'G'
    labyrinthMap[2][6] = '#'
    labyrinthMap[2][7] = 'G'
    labyrinthMap[2][8] = '#'
    labyrinthMap[2][9] = 'G'
    labyrinthMap[2][10] = '#'
    labyrinthMap[2][11] = 'G'
    labyrinthMap[2][12] = '#'
    labyrinthMap[3][0] = '.'
    labyrinthMap[3][1] = '.'
    labyrinthMap[3][2] = '.'
    labyrinthMap[3][3] = '.'
    labyrinthMap[3][4] = '.'
    labyrinthMap[3][5] = '.'
    labyrinthMap[3][6] = '.'
    labyrinthMap[3][7] = '.'
    labyrinthMap[3][8] = '#'
    labyrinthMap[3][9] = '.'
    labyrinthMap[3][10] = '.'
    labyrinthMap[3][11] = 'G'
    labyrinthMap[3][12] = '#'
    labyrinthMap[4][0] = '#'
    labyrinthMap[4][1] = 'G'
    labyrinthMap[4][2] = '#'
    labyrinthMap[4][3] = '.'
    labyrinthMap[4][4] = '#'
    labyrinthMap[4][5] = '#'
    labyrinthMap[4][6] = '#'
    labyrinthMap[4][7] = '.'
    labyrinthMap[4][8] = '#'
    labyrinthMap[4][9] = 'G'
    labyrinthMap[4][10] = '#'
    labyrinthMap[4][11] = 'G'
    labyrinthMap[4][12] = '#'
    labyrinthMap[5][0] = '#'
    labyrinthMap[5][1] = 'G'
    labyrinthMap[5][2] = 'G'
    labyrinthMap[5][3] = '.'
    labyrinthMap[5][4] = 'G'
    labyrinthMap[5][5] = 'G'
    labyrinthMap[5][6] = 'G'
    labyrinthMap[5][7] = '.'
    labyrinthMap[5][8] = '#'
    labyrinthMap[5][9] = '.'
    labyrinthMap[5][10] = 'G'
    labyrinthMap[5][11] = 'G'
    labyrinthMap[5][12] = '#'
    labyrinthMap[6][0] = '#'
    labyrinthMap[6][1] = 'G'
    labyrinthMap[6][2] = '#'
    labyrinthMap[6][3] = '.'
    labyrinthMap[6][4] = '#'
    labyrinthMap[6][5] = 'G'
    labyrinthMap[6][6] = '#'
    labyrinthMap[6][7] = '.'
    labyrinthMap[6][8] = '#'
    labyrinthMap[6][9] = '.'
    labyrinthMap[6][10] = '#'
    labyrinthMap[6][11] = '.'
    labyrinthMap[6][12] = '#'
    labyrinthMap[7][0] = '#'
    labyrinthMap[7][1] = '#'
    labyrinthMap[7][2] = 'G'
    labyrinthMap[7][3] = '.'
    labyrinthMap[7][4] = '.'
    labyrinthMap[7][5] = '.'
    labyrinthMap[7][6] = 'G'
    labyrinthMap[7][7] = '.'
    labyrinthMap[7][8] = '.'
    labyrinthMap[7][9] = '.'
    labyrinthMap[7][10] = '.'
    labyrinthMap[7][11] = '.'
    labyrinthMap[7][12] = '#'
    labyrinthMap[8][0] = '#'
    labyrinthMap[8][1] = 'G'
    labyrinthMap[8][2] = '#'
    labyrinthMap[8][3] = '.'
    labyrinthMap[8][4] = '#'
    labyrinthMap[8][5] = 'G'
    labyrinthMap[8][6] = '#'
    labyrinthMap[8][7] = '#'
    labyrinthMap[8][8] = '#'
    labyrinthMap[8][9] = '.'
    labyrinthMap[8][10] = '#'
    labyrinthMap[8][11] = 'G'
    labyrinthMap[8][12] = '#'
    labyrinthMap[9][0] = '#'
    labyrinthMap[9][1] = '.'
    labyrinthMap[9][2] = '.'
    labyrinthMap[9][3] = '.'
    labyrinthMap[9][4] = 'G'
    labyrinthMap[9][5] = '#'
    labyrinthMap[9][6] = 'G'
    labyrinthMap[9][7] = 'G'
    labyrinthMap[9][8] = 'G'
    labyrinthMap[9][9] = '.'
    labyrinthMap[9][10] = 'G'
    labyrinthMap[9][11] = 'G'
    labyrinthMap[9][12] = '#'
    labyrinthMap[10][0] = '#'
    labyrinthMap[10][1] = 'G'
    labyrinthMap[10][2] = '#'
    labyrinthMap[10][3] = '.'
    labyrinthMap[10][4] = '#'
    labyrinthMap[10][5] = 'G'
    labyrinthMap[10][6] = '#'
    labyrinthMap[10][7] = 'G'
    labyrinthMap[10][8] = '#'
    labyrinthMap[10][9] = '.'
    labyrinthMap[10][10] = '#'
    labyrinthMap[10][11] = 'G'
    labyrinthMap[10][12] = '#'
    labyrinthMap[11][0] = '#'
    labyrinthMap[11][1] = 'G'
    labyrinthMap[11][2] = 'G'
    labyrinthMap[11][3] = '.'
    labyrinthMap[11][4] = 'G'
    labyrinthMap[11][5] = 'G'
    labyrinthMap[11][6] = 'G'
    labyrinthMap[11][7] = '#'
    labyrinthMap[11][8] = 'G'
    labyrinthMap[11][9] = '.'
    labyrinthMap[11][10] = 'G'
    labyrinthMap[11][11] = 'G'
    labyrinthMap[11][12] = '#'
    labyrinthMap[12][0] = '#'
    labyrinthMap[12][1] = '#'
    labyrinthMap[12][2] = '#'
    labyrinthMap[12][3] = '#'
    labyrinthMap[12][4] = '#'
    labyrinthMap[12][5] = '#'
    labyrinthMap[12][6] = '#'
    labyrinthMap[12][7] = '#'
    labyrinthMap[12][8] = '#'
    labyrinthMap[12][9] = '#'
    labyrinthMap[12][10] = '#'
    labyrinthMap[12][11] = '#'
    labyrinthMap[12][12] = '#'
    startX = startY = 3
    # for x in range(n):
    #     if labyrinthMap[0][x]=='G':
    #         startX = x
    #         startY = 0
    #         break
    # print(startX,'==',startY)
    minStep = 99999999 
    mx = 0
    my = 0
    maxNum = 0
    book[startX][startY] = 1
    qList = []
    row = {'x': startX, 'y': startY}
    qList.append(row)
    flag = 0
    while len(qList) != 0: 
        for k in range(4):
            tx =  qList[0]['x']+next[k][0]
            ty =  qList[0]['y']+next[k][1]
            if tx < 0 or tx >= n or ty < 0 or ty >= m:
                continue 
            if labyrinthMap[tx][ty] == '.' and book[tx][ty] == 0:
                book[tx][ty] = 1
                row = {'x': tx, 'y': ty}
                qList.append(row) 
                sumNum = getNum(tx,ty)
                # print(sumNum)
                if (sumNum>maxNum):
                    maxNum = sumNum
                    mx = tx
                    my = ty
        del qList[0]

    for x in range(n):
        print(labyrinthMap[x])
    # print(book)
    # print(qList)

    print('最佳位置：将炸弹放置在(%d,%d)处，可以消灭%d个敌人' % (mx,my,maxNum))
    sys.exit(-1)
