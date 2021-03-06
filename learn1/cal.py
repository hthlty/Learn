#coding=utf-8

import tkinter
import math

#主窗口
root = tkinter.Tk()
root.minsize(320,420)
root.title('计算器')
shownum = tkinter.StringVar()
shownum.set(0)

numstrlist=[]  #存储数据，符号
isjisuan=False #运算标志

def pressnum(num):  #按下数字
    global isjisuan
    if isjisuan==True:
        shownum.set('0')
        isjisuan=False
    oldnum=shownum.get()
    if oldnum=='0':
        shownum.set(num)
    else:
        if num=='+/-':
            if oldnum.startswith('-'):
                shownum.set(oldnum[1:])
            else:
                shownum.set('-'+oldnum)
        else:
            shownum.set(oldnum+num)

def presssign(sign):
    global numstrlist
    global isjisuan
    oldnum = shownum.get()
    numstrlist.append(oldnum)
    numstrlist.append(sign)
    isjisuan=True
    print(numstrlist)

def equal(sign):
    global numstrlist
    if sign=='=':
        oldnum = shownum.get()
        numstrlist.append(oldnum)
        print(numstrlist)
        resu1 = ''.join(numstrlist)
        result = eval(resu1)
        print(result)
        shownum.set(result)
        numstrlist.clear()
    if sign=='1/x':
        oldnumm = shownum.get()
        result = 1/float(oldnum)
        print(result)
        shownum.set(result)
    if sign=='√':
        oldnum = shownum.get()
        result = math.sqrt(float(oldnum))
        print(result)
        shownum.set(result)

def gui0():
    global numstrlist
    global isjisuan
    numstrlist.clear()
    isjisuan=False
    shownum.set(0)

#文本框输入
label = tkinter.Label(root,textvariable=shownum,bg='gray',\
                      font=('宋体',20),anchor='e',bd=5,fg='gold')
label.place(x=20,y=10,width=280,height=50)

#第一行
btn1=tkinter.Button(text='MC',bg='#988',bd=2)
btn1.place(x=10,y=70,width=50,height=50)
btn2=tkinter.Button(text='MR',bg='#988',bd=2)
btn2.place(x=70,y=70,width='50',height=50)
btn3=tkinter.Button(text='MS',bg='#988',bd=2)
btn3.place(x=130,y=70,width='50',height=50)
btn4=tkinter.Button(text='M+',bg='#988',bd=2)
btn4.place(x=190,y=70,width='50',height=50)
btn5=tkinter.Button(text='M-',bg='#988',bd=2)
btn5.place(x=250,y=70,width='50',height=50)

#第二行
btn2_1 =tkinter.Button(text ='del',bg='#988',bd=3)
btn2_1.place(x=10,y =130,width =50,height=50)
btn2_2 =tkinter.Button(text ='CE',bg='#988',bd=3,command=lambda:gui0())#CE是清除全部数字，但不影响以前的计算
btn2_2.place(x=70,y =130,width =50,height=50)
btn2_3 =tkinter.Button(text ='C',bg='#988',bd=3,command=lambda:gui0())#C健是重新开始计算，和ESC键是一样的功能
btn2_3.place(x=130,y =130,width =50,height=50)
btn2_4 =tkinter.Button(text ='+/-',bg='#988',bd=3,command=lambda:pressnum('+/-'))
btn2_4.place(x=190,y =130,width =50,height=50)
btn2_5 =tkinter.Button(text ='√',bg='#988',bd=3,command=lambda:equal('√'))#--------√开平方
btn2_5.place(x=250,y =130,width =50,height=50)
#第三行
btn3_1 =tkinter.Button(text ='7',bg='#aaaaaa',bd=3,command=lambda:pressnum('7'))
btn3_1.place(x=10,y =190,width =50,height=50,)
btn3_2 =tkinter.Button(text ='8',bg='#aaaaaa',bd=3,command=lambda:pressnum('8'))
btn3_2.place(x=70,y =190,width =50,height=50)
btn3_3 =tkinter.Button(text ='9',bg='#aaaaaa',bd=3,command=lambda:pressnum('9'))
btn3_3.place(x=130,y =190,width =50,height=50)
btn3_4 =tkinter.Button(text ='/',bg='#708069',command=lambda:presssign('/'))
btn3_4.place(x=190,y =190,width =50,height=50)
btn3_5 =tkinter.Button(text ='%',bg='#708069',command=lambda:presssign('%'))
btn3_5.place(x=250,y =190,width =50,height=50)
# 第四行
btn4_1 = tkinter.Button(text='4', bg='#aaaaaa', bd=3, command=lambda: pressnum('4'))
btn4_1.place(x=10, y=250, width=50, height=50)
btn4_2 = tkinter.Button(text='5', bg='#aaaaaa', bd=3, command=lambda: pressnum('5'))
btn4_2.place(x=70, y=250, width=50, height=50)
btn4_3 = tkinter.Button(text='6', bg='#aaaaaa', bd=3, command=lambda: pressnum('6'))
btn4_3.place(x=130, y=250, width=50, height=50)
btn4_4 = tkinter.Button(text='*', bg='#708069', command=lambda: presssign('*'))
btn4_4.place(x=190, y=250, width=50, height=50)
btn4_5 = tkinter.Button(text='1/x', bg='#708069', command=lambda: equal('1/x'))  # ----------------------------------倒数
btn4_5.place(x=250, y=250, width=50, height=50)
# 第五行
btn5_1 = tkinter.Button(text='1', bg='#aaaaaa', bd=3, command=lambda: pressnum('1'))
btn5_1.place(x=10, y=310, width=50, height=50)
btn5_2 = tkinter.Button(text='2', bg='#aaaaaa', bd=3, command=lambda: pressnum('2'))
btn5_2.place(x=70, y=310, width=50, height=50)
btn5_3 = tkinter.Button(text='3', bg='#aaaaaa', bd=3, command=lambda: pressnum('3'))
btn5_3.place(x=130, y=310, width=50, height=50)
btn5_4 = tkinter.Button(text='-', bg='#708069', command=lambda: presssign('-'))
btn5_4.place(x=190, y=310, width=50, height=50)
btn5_5 = tkinter.Button(text='=', bg='#708069', command=lambda: equal('='))
btn5_5.place(x=250, y=310, width=50, height=110)
# 第六行
btn6_1 = tkinter.Button(text='0', bg='#aaaaaa', bd=3, command=lambda: pressnum('7'))
btn6_1.place(x=10, y=370, width=110, height=50)
btn6_3 = tkinter.Button(text='.', bg='#708069', command=lambda: pressnum('.'))
btn6_3.place(x=130, y=370, width=50, height=50)
btn6_4 = tkinter.Button(text='+', bg='#708069', command=lambda: presssign('+'))
btn6_4.place(x=190, y=370, width=50, height=50)

root.mainloop()