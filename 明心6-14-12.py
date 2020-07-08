#题：将1~9各用一次组成两个数（一个五位数和一个四位数），使其中一个数是另一个数的9倍。求出所有满足条件的解
for i in range(2,10):
    for j in range(1,10):
        if i == j:
            continue
        for k in range(1,10):
            if k == i or k == j:
                continue
            n = 9-((i+j+k)%9)
            if n == i or n == j or n == k or n == 5:
                continue
            list1 = [i,j,k,n,0]
            for s in str(9*(i*1000+j*100+k*10+n)):
                if int(s) in list1:
                    break
                list1.append(int(s))
            else:
                print str(i)+str(j)+str(k)+str(n),str(9*(i*1000+j*100+k*10+n))
