m = 204
n = 19
list1 = [m,n]
while list1[-2]%list1[-1] != 1:
    list1.append(list1[-2]%list1[-1])

b,c = -1*(list1[-2]//list1[-1]),1

while len(list1) > 2:
    b,c= c - b*(list1[-3]//list1[-2]),b
    list1.pop()
print(c%list1[1])
