# -*- encoding: utf8 -*-
import random
print( "小主，来玩几盘石头剪刀布吧！")
list1 = ["剪刀","石头","布"]
#list2 = ["输", "打平", "赢"]
#print( ipad)
flag = True
while flag == True:
    r = input("你出啥？(剪刀是'1',石头是'2',布是'3')")
    ipad = random.choice(list1)
    win = 0
    if r == "0":
        print( "输入错了。")
    else:
        try:
            if ipad == "剪刀":
                if r == "1":
                    win = 1
                elif r == "2":
                    win = 2
            elif ipad == "石头":
                if r == "2":
                    win = 1
                elif r == "3":
                    win = 2
            elif ipad == "布":
                if r == "1":
                    win = 2
                if r == "3":
                    win = 1
            if win == 0:
                print( "你出的是" + list1[int(r)-1], ",我出的是" + ipad, ",你输了。再来一盘吧。")
            elif win == 1:
                print( "你出的是" + list1[int(r)-1], ",我出的是" + ipad, ",我们打平了。再来一盘吧。")
            elif win == 2:
                print( "你出的是" + list1[int(r)-1], ",我出的是" + ipad, ",你赢了。再来一盘吧。")
        except:
            print( "输入错了。")
