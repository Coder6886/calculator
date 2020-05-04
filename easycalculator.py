# -*- encoding: utf8 -*-
name = "小主"
error = "输入错了！您可以往里输入'help'哦"
def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    return ans
def divPrime(num):
    lt = []
    times = []
    print (num, "=",end='')
    while num != 1:
        for i in range(2, int(num)+1):
            if i not in lt and num % i == 0: 
                lt.append(i)
                times.append(1)
                num = num / i 
                break
            elif i in lt and num % i == 0: 
                times[lt.index(i)] += 1
                num = num / i 
                break
    for i in range(0, len(lt)-1):
        if times[i] != 1:
            print(lt[i], "^", times[i], 'x',end='')
        else:
            print(lt[i], "x",end='')
    
    if times[-1] != 1:
        print(lt[-1] ,"^", times[-1])
    else:
        print( lt[-1])
    
def gcd(a,b) :
    k = min(a,b)
    a = max(a,b)
    b = k
    while max(a,b) % min(a,b) != 0:
        k = min(a,b)
        a = max(a,b)%k
        b = k
    return min(a,b)
def lcm(a,b):
    return a*b/gcd(a,b)

flag = True
while flag == True:
    r = input(name+", 有吩咐吗?")
    try:
        if r[-1] == "!":
            try:
                print( factorial(int(r[:-1])))
            except:
                print( "")
        elif r[:5] == "divP(" and r[-1] == ")":
            try:
                divPrime(int(r[5:-1]))
            except:
                print (error)
        elif r[:4] == "gcd(" and r[-1] == ")":
            try:
                for i in range(5, len(r)-1):
                    if r[i] == ",":
                        a = int(r[4:i])
                        b = int(r[i+1:len(r)-1])
                        break
                print (gcd(a,b))
            except:
                print (error)
        elif r[:4] == "lcm(" and r[-1] == ")":
            try:
                for i in range(5, len(r)-1):
                    if r[i] == ",":
                        a = int(r[4:i])
                        b = int(r[i+1:len(r)-1])
                        break
                print( lcm(a,b))
            except:
                print (error)
        elif r == "help":
            print( "n的阶乘 = n!")
            print( "把n因式分解= divP(n)")
            print( "m和n的最大公因数 = gcd(m,n)")
            print( "m和n的最小公倍数 = lcm(m,n)")
            print( "把名字变成'name' = change(name)")
            print( "关闭计算器 = close")
        elif r[:7] == "change(" and r[-1] == ")":
            try:
                name = r[7:-1]
                print( "OK")
            except:
                print( error)
        elif r == "close":
            print( "OK")
            flag = False
        else:
            print( error)
    except:
        print( error)
    
