num = 14
magic = []
def printmagic(magic):
    for i in range(len(magic)):
        for j in range(len(magic)):
            print (" "*(len(str(num**2)) + 1 - len(str(magic[i][j]))) + str(magic[i][j]),end = '')
        print ("")
def look(magic):
    for i in range(len(magic)):
        if sum(magic[i]) != 0.5*num*(num ** 2 + 1):
            return False
    for i in range(len(magic)):
        s = 0
        for j in range(len(magic)):
            s += magic[i][j]
        if s != 0.5*num*(num ** 2 + 1):
            return False
    s = 0
    for i in range(len(magic)):
        s += magic[i][i]
    if s != 0.5*num*(num ** 2 + 1):
        return False
    s = 0
    for i in range(len(magic)):
        s += magic[i][num-i-1]
    if s != 0.5*num*(num ** 2 + 1):
        return False
    return True
for i in range(num):
    magic.append([])
    for j in range(num):
        magic[i].append(0)
def odd(num,magic):
    count = 1
    i = 0
    j = int(num/2-0.5)

    while count != num**2 + 1:
        magic[i][j] = count
        if i == 0 and j != num - 1:
            i = num-1
            j += 1
        elif i != 0 and j == num - 1:
            i -= 1
            j = 0
        elif (i == 0 and j == num - 1):
            i += 1
        elif (magic[i-1][j+1] != 0):
            i += 1
        else:
            i -= 1
            j += 1
        count += 1
def even_even(num, magic):
    count = 1
    i = 0
    j = 0
    while count != num ** 2 + 1:
        if (j < num/4) or (j > num - num/4-1):
            magic[i][j] = num**2 + 1 - count
        else:
            magic[i][j] = count

        if j == num - 1:
            j = 0
            i += 1
        else:
            j += 1
        count += 1

def even_odd(num,magic):
    a = []
    for i in range(num):
        a.append([])
        for j in range(num):
            a[i].append(0)
    for i in range(int(len(magic)/2)):
        for j in range(int(len(magic)/2)):
            a[i][j] = 0
    odd(int(num/2), a)
    for i in range(int(len(magic)/2)):
        for j in range(int(len(magic)/2)):
            magic[i][j] = a[i][j]
            magic[i+int(len(magic)/2)][j] = int(a[i][j] + 3*(num/2)**2)
            magic[i][j+int(len(magic)/2)] = int(a[i][j] + 2*(num/2)**2)
            magic[i+int(len(magic)/2)][j+int(len(magic)/2)] = int(a[i][j] + (num/2)**2)
    m = (num // 2 -1) // 2
    for i in range(len(magic)//2):
        if i == (len(magic)//2 - 1)//2:
            for j in range(1,m+1):
                t = magic[(len(magic)//2 - 1)//2][j]
                magic[(len(magic)//2 - 1)//2][j] = magic[len(magic)-(len(magic)//2 - 1)//2 - 1][j]
                magic[len(magic)-(len(magic)//2 - 1)//2 - 1][j] = t
        else:
            for j in range(m):
                t = magic[i][j]
                magic[i][j] = magic[i+len(magic)//2][j]
                magic[i+len(magic)//2][j] = t
    for i in range(len(magic)//2):
        if i == (len(magic)//2 - 1) // 2:
            for j in range(len(magic)-2,len(magic)-1-m,-1):
                t = magic[(len(magic)//2 - 1)//2][j]
                magic[(len(magic)//2 - 1)//2][j] = magic[len(magic)-(len(magic)//2 - 1)//2 - 1][j]
                magic[len(magic)-(len(magic)//2 - 1)//2 - 1][j] = t
        else:
            for j in range(len(magic)-1,len(magic)-m,-1):
                t = magic[i][j]
                magic[i][j] = magic[i+len(magic)//2][j]
                magic[i+len(magic)//2][j] = t

if num % 2 == 1:
    odd(num, magic)
elif num % 4 == 2:
    even_odd(num, magic)
else:
    even_even(num, magic)
print(look(magic))
printmagic(magic)


