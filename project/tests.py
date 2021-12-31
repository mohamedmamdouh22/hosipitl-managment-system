from tkinter import *

root=Tk()
root.geometry('400x400')
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)
def select(num):
    selected=e.get()
    e.delete(0,END)
    e.insert(0,selected+str(num))
def equal():
    op=e.get()
    op=eval(op)
    e.delete(0,END)
    e.insert(0,str(op))
def reset():
    e.delete(0,END)
buttons=[1,1,1,1,1,1,1,1,1,1]
buttons[0]=Button(root,text='0',padx=40,pady=20,borderwidth=5,command=lambda:select(0))
buttons[1]=Button(root,text=f'1',padx=40,pady=20,borderwidth=5,command=lambda:select(1))
buttons[2]=Button(root,text=f'2',padx=40,pady=20,borderwidth=5,command=lambda:select(2))
buttons[3]=Button(root,text=f'3',padx=40,pady=20,borderwidth=5,command=lambda:select(3))
buttons[4]=Button(root,text=f'4',padx=40,pady=20,borderwidth=5,command=lambda:select(4))
buttons[5]=Button(root,text=f'5',padx=40,pady=20,borderwidth=5,command=lambda:select(5))
buttons[6]=Button(root,text=f'6',padx=40,pady=20,borderwidth=5,command=lambda:select(6))
buttons[7]=Button(root,text=f'7',padx=40,pady=20,borderwidth=5,command=lambda:select(7))
buttons[8]=Button(root,text=f'8',padx=40,pady=20,borderwidth=5,command=lambda:select(8))
buttons[9]=Button(root,text=f'9',padx=40,pady=20,borderwidth=5,command=lambda:select(9))
reset=Button(root,text='reset',padx=95,pady=20,borderwidth=5,command=reset)
equal=Button(root,text='=',padx=105,pady=20,borderwidth=5,command=equal)
plus=Button(root,text='+',padx=40,pady=20,borderwidth=5,command=lambda:select('+'))
minus=Button(root,text='-',padx=40,pady=20,borderwidth=5,command=lambda:select('-'))

buttons[0].grid(column=0,row=4)
buttons[1].grid(column=0,row=3)
buttons[2].grid(column=1,row=3)
buttons[3].grid(column=2,row=3)
buttons[4].grid(column=0,row=2)
buttons[5].grid(column=1,row=2)
buttons[6].grid(column=2,row=2)
buttons[7].grid(column=0,row=1)
buttons[8].grid(column=1,row=1)
buttons[9].grid(column=2,row=1)
reset.grid(column=1,row=4,columnspan=2)
plus.grid(column=0,row=5)
minus.grid(column=0,row=6)
equal.grid(column=1,row=5,columnspan=2)

# creates tkinter window or root window
root.mainloop()
    