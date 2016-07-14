import sys
def dfs(step):
    global t  
    global g  
    global book  
    global a   
    if step==g+1:
        for x in range(1,g+1):
            print('%d'%a[x], end='') 
        print('\n')
        t+=1
        return
    for x in range(1,g+1):
        if book[x]==0:
            a[step] = x
            book[x] = 1
            dfs(step+1)
            book[x] = 0

if __name__ == '__main__':
    print('全队列-深度优先搜索')
    g = 5
    t = 0
    book = []
    a = []
    for i in range(10):
        book.append(0)
        a.append(0)
    dfs(1)
    print('一共%d种组合'%t)
    sys.exit(-1)
