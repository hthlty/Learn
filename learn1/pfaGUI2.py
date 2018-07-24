#coding=utf-8

from functools import partial as pto
from tkinter import Button,X,Tk
from tkinter.messagebox import showinfo,showwarning,showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter':CRIT,
    'railroad crossing':WARN,
    'wrong way':CRIT,
    'merging traffic':WARN,
    'one way':REGU
}

critCB = lambda :showerror('Error','Error Button Pressed!')
warnCB = lambda :showwarning('warning','Warning Button Pressed!')
infoCB = lambda :showinfo('Info','Info Button Pressed!')

top = Tk()
top.title('Road Signs')
Button(top,text='QUIT',command=top.quit,bg='red',fg='white').pack()

myButton = pto(Button,top)
CritButton = pto(myButton,command=critCB,bg='white',fg='red')
WarnButton = pto(myButton,command=warnCB,bg='yellow')
ReguButton = pto(myButton,command=infoCB,bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X,expand=True)'\
          %(signType.title(),eachSign,'.upper()' if signType==CRIT else '.title()')
    eval(cmd)
top.mainloop()