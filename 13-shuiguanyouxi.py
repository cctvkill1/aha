#  水管游戏
import sys
import random
import queue


def dfs(x, y, front):
    global n
    global m
    global a
    global book
    global s
    global flag
    if x == n-1 and y == m:
        flag = 1
        for i in range(len(s)):
            print('%d %d' % (s[i]['x'], s[i]['y']))
        return
    if x<0 or x>n-1 or y<0 or y>m-1 :
        return 
    if book[x][y]==1:
        return
    book[x][y]=1
    row = {'x':x,'y':y}
    s.append(row);
    # 当前管道是直的
    if a[x][y] >=5 and a[x][y]<=6:
        if front == 1:
            dfs(x,y+1,1)
        if front == 2:
            dfs(x+1,y,2)
        if front == 3:
            dfs(x,y-1,3)
        if front == 4:
            dfs(x-1,y,4)
    # 当前管道是弯的
    if a[x][y]>=1 and a[x][y]<=4:
        if front == 1:
            dfs(x+1,y,2)
            dfs(x-1,y,4)
        if front == 2:
            dfs(x,y+1,1)
            dfs(x,y-1,3)
        if front == 3:
            dfs(x-1,y,4)
            dfs(x+1,y,2)
        if front == 4:
            dfs(x,y+1,1)
            dfs(x,y-1,3)
    book[x][y] = 0
    s.pop()
    return

if __name__ == '__main__':
    flag = 0
    # n = random.randint(5, 10)
    # m = random.randint(5, 10)
    n = 5
    m = 4
    book = [([0] * m) for i in range(n)]
    a = [([0] * m) for i in range(n)]
    a[0][0] = 5
    a[0][1] = 3
    a[0][2] = 5
    a[0][3] = 3
    a[1][0] = 1
    a[1][1] = 5
    a[1][2] = 3
    a[1][3] = 0
    a[2][0] = 2
    a[2][1] = 3
    a[2][2] = 5
    a[2][3] = 1
    a[3][0] = 6
    a[3][1] = 1
    a[3][2] = 1
    a[3][3] = 5
    a[4][0] = 1
    a[4][1] = 5
    a[4][2] = 5
    a[4][3] = 4
    s = []
    dfs(0, 0, 1)
    if(flag == 0):
        print('没有找到出路')

    sys.exit(-1)
