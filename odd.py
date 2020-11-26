num = 20
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
def odd(num):
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
#odd(num)
def even_even(num):
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
#even_even(num)
#def even_odd(num):
    
    




























