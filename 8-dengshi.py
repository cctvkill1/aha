import sys
def dfs(step):
    global t  
    global g  
    global book  
    global a   
    if step==g+1:
        if a[1]*100+a[2]*10+a[3]+a[4]*100+a[5]*10+a[6]==a[7]*100+a[8]*10+a[9]:
            print('%d%d%d+%d%d%d=%d%d%d'%(a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]) ) 
            t+=1
        return
    for x in range(1,g+1):
        if book[x]==0:
            a[step] = x
            book[x] = 1
            dfs(step+1)
            book[x] = 0

if __name__ == '__main__':
    print('求值□□□+□□□=□□□   深度优先搜索')
    g = 9
    t = 0
    book = []
    a = []
    for i in range(10):
        book.append(0)
        a.append(0)
    dfs(1)
    print('一共%d种组合'%(t/2))
    sys.exit(-1)
