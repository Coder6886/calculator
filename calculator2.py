# -*- encoding: utf8 -*-

print("用完了以后一定要关闭计算器(/)哦。")
print("/ = close")
print("0 = gcd")
print("1 = lcm")
print("2 = factorial")
print("3 = divPrime")
print("4 = primes until")
def List(n):
    list1 = [2]   
    if n == 1:
        return []
    if n == 2:
        return [2]
    for i in range(3,n+1,2):
        for j in list1:
            if i % j == 0:
                break
        else:
             list1.append(i)
    return list1
def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    return ans
def divPrime(num):
    lt = []
    times = []
    print(num, "=",)
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
            print(lt[i], "^", times[i], 'x',)
        else:
            print(lt[i], "x",)
    
    if times[-1] != 1:
        print(lt[-1] ,"^", times[-1])
    else:
        print(lt[-1])
    
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
    try:
        r = input(">")
##        print (r)
##        print (r[:1])
        if r[:2] == "0 ":
            try:
                for i in range(2,len(r)):
                    if r[i] == " ":
                        a = int(r[2:i])
                        b = int(r[i+1:len(r)])
                        break
                print(gcd(a,b))
            except:
                print("err")
                
        elif r[:2] == "1 ":
            try:
                for i in range(2,len(r)):
                    if r[i] == " ":
                        a = int(r[2:i])
                        b = int(r[i+1:len(r)])
                        break
                print(lcm(a,b))
            except:
                print("err")
        elif r[:2] == "2 ":
            try:
                print(factorial(int(r[2:len(r)])))
            except:
                print("err")
        elif r[:2] == "3 ":
            try:
                divPrime(int(r[2:len(r)]))
            except:
                print("err")
        elif r[:2] == "4 ":
            try:
                print(List(int(r[2:len(r)])))
            except:
                print("err")
        elif r == "/":
            flag = False

        elif r == "?":
            print("用完了以后一定要关闭计算器(/)哦。")
            print("/ = close")
            print("0 = gcd")
            print("1 = lcm")
            print("2 = factorial")
            print("3 = divPrime")
            print("4 = primes until")

        else:
            try:
                print(eval(r))
            except:
                print("err")
    except:
        print("err")
