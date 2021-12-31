from tkinter import *

root=Tk()
root.title('simple calculator')
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)
def select(number):
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current)+str(number))      
def reset_button():
        e.delete(0,END)
def add_but():
        first=e.get()
        global f_num
        f_num=int(first)
        e.delete(0,END)
def equal_but():
        second=e.get()
        e.delete(0,END)
        e.insert(0,int(second)+f_num)

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
reset=Button(root,text='reset',padx=95,pady=20,borderwidth=5,command=reset_button)
equal=Button(root,text='=',padx=105,pady=20,borderwidth=5,command=equal_but)
plus=Button(root,text='+',padx=40,pady=20,borderwidth=5,command=add_but)


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
equal.grid(column=1,row=5,columnspan=2)
root.mainloop()
    
