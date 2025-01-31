import keyboard
import win32api
import win32con
import time
import threading
import sys
#Usage:wechat game Jump assistant. 
#Usage:put mouse on the center of head, press F11,then focus the mouse on the target, press F12.
ScreenScale=1.5  
mysteriousconstant=269*1.5/ScreenScale##ratio of distance/time,fit in 150% scale in screen setting.
cnt = 0
mancurrentpos = (0,0)
targetpos = (0,0)
ss = 0
def mouse_click_now(t):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0) #鼠标左键按下
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0) #鼠标左键抬起
def exec():
    global ss
    while True:
        if ss == 0:
            time.sleep(0.5)
        else:
            mouse_click_now(ss)
            ss = 0
term = False
def click(x):
    global mancurrentpos,targetpos,ss,cnt,term
    if x.scan_code == 87:#key F11
        mancurrentpos = win32api.GetCursorPos()
    if x.scan_code == 88:#key F12
        a = win32api.GetCursorPos()
        b0 = mancurrentpos
        b=(b0[0],b0[1]+90/ScreenScale)  #head to foot
        if mancurrentpos[0]==0 and mancurrentpos[1]==0:
            return
        c=(a[0]-b[0],a[1]-b[1])
        x0=3**(-0.5)*c[0]+c[1]
        y0=c[1]-3**(-0.5)*c[0]
        dist=(x0**2+y0**2)**0.5
        ss=dist/mysteriousconstant
        mancurrentpos = [0 ,0]
t1=threading.Thread(target = exec)
t1.daemon = True
t1.start()
keyboard.hook(click)
