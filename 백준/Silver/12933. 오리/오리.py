record = list(input().strip())
n = 0
while True:
    idx = 0 # quack 따지는 인덱스
    idx2 = 0 # 걍 인덱스
    check = ['q', 'u', 'a', 'c', 'k']
    delete = []
    checkflag = 0
    
    for i in range(len(record)):
        if record[i] == check[idx]:
            delete.append(i)
            idx+=1
            if idx == 5:
                for j in range(5):
                    temp = delete[j]
                    record[temp] = '!'
                checkflag = 1
                delete = []
                idx = 0
                    
    if checkflag == 1:
        n+= 1
    else:
        break
        
for i in record:
    if i != '!':
        n = -1
        break
print(n)
        
        
    