import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import date

con = sqlite3.connect("hospital.db")
cur = con.cursor()

x = 0
string_name = ""

root = Tk()
root.geometry("1400x800")
root.title("HOSPITAL")
root.resizable(width=False, height=False)


#root.iconbitmap(r"F:\CPH1911\2nd et python project\icon.ico")
class HoverButton(Button):
    def init(self, master, **kw):
        Button.init(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
class Start:
    def __init__(self,root):
        self.root = root
        
        self.Start_frame = Frame(self.root,width=1400,height=800)
        self.Start_frame.place(x=0,y=0)
        self.welcome = Label(self.Start_frame,text="WELCOME",font=("Goudy Stout",40),fg="black")
        self.welcome.place(x=450,y=10)
        #background img
        self.bg_main=PhotoImage(file='back.png')
        self.bg1_m=self.bg_main.subsample(1,1)
        self.bg=Label(self.Start_frame,image=self.bg1_m)
        self.bg.place(x=0,y=0)
        # image main
        self.mainbackground = PhotoImage(file="backmain.PNG")
        self.mainbackground.subsample(5,5)  #size of image
        self.Labelmainbackground = Label(self.Start_frame,image=self.mainbackground)
        self.Labelmainbackground.place(x=250,y=100)
        # button login
        self.logbutton = HoverButton(self.Start_frame,text="LOG IN",bg="#68ece8",font=("Arial",30),fg="black", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",cursor="mouse",command=self.__login)
        self.logbutton.place(x=400,y=650)
        # button exit
        self.exit = HoverButton(self.Start_frame,text="EXIT",bg="#68ece8",font=("Arial",30),fg="black",activeforeground='red', relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",cursor="mouse",command=quit)
        self.exit.place(x=850,y=650)

    def __login(self):

        self.Start_frame.place_forget()
        self.bg_frame=Frame(root,width=1400,height=800)
        self.bg_frame.place(x=0,y=0)
        self.bg=PhotoImage(file='back.png')
        self.bg1=self.bg.subsample(1,1)
        self.bg_lab=Label(self.bg_frame,image=self.bg1).place(x=0,y=0)

        self.framelogin = Frame(self.bg_frame, bg="white",width=500,height=800,highlightbackground='#888',highlightthickness=1)
        self.framelogin.place(x=500,y=0)

        self.loginphoto =PhotoImage(file="login.png")
        self.loginphoto1=self.loginphoto.subsample(3,3)
        self.loginphotolabel = Label(self.framelogin,image=self.loginphoto1).place(x=25,y=20)

        self.lab1in = Label(self.framelogin, text="User Name", font=('arial', 20),bg='white')
        self.lab1in.place(x=180, y=280)
        self.ent1in = Entry(self.framelogin, font=('arial', 20))
        self.ent1in.place(x=80, y=320)
        self.ent1in.focus()
        self.lab2in = Label(self.framelogin, text="Password", font=('arial', 20),bg='white')
        self.lab2in.place(x=180, y=390)
        self.ent2in = Entry(self.framelogin, font=('arial', 20), show="*")
        self.ent2in.place(x=80, y=430)
        self.butin = Button(self.framelogin,bg='limegreen', text="LOG IN", font=('arial', 20),command=self.__check)
        self.butin.place(x=190, y=550)
        self.resetin = Button(self.framelogin, text="EXIT",activebackground='red', font=('arial', 20),command=quit)
        self.resetin.place(x=90, y=680)
        self.sign_in_ret = Button(self.framelogin, text="RETURN", font=('arial', 20),cursor='exchange',command=self.__return_to_start)
        self.sign_in_ret.place(x=280, y=680)

    def __return_to_start(self):
        self.bg_frame.place_forget()
        self.Start_frame.pack()








    def __check(self):
        cur.execute(f"select User_Name from Logins where User_Name = '{self.ent1in.get()}' ")
        result_username = cur.fetchone()
        if result_username == None:
            messagebox.showerror("HOSPITAL","WRONG USER NAME")


        elif result_username != None :
            cur.execute(f"select Password from Logins where Password = {self.ent2in.get()}")
            result_pass = cur.fetchone()
            if result_pass == None:
                messagebox.showerror("HOSPITAL","WRONG PASSWORD")

            else :
                messagebox.showinfo("HOSPITAL","WELCOME "+ self.ent1in.get())
                self.framelogin.place_forget()
                person()

    def return_fromAllClasses(self):
        doctor().doc_frame.place_forget()
        medical_store().medical_frame.place_forget()
        person().main.place(x=0,y=0)


class person(Start):

    def __init__(self):

        self.main = Frame(root,width =1400,height=800)
        self.main.place(x=0,y=0)
        #background
        self.__upper=Frame(self.main,width=1400,height=90,bg='white')
        self.__upper.place(x=0,y=0)
        self.__pulse=PhotoImage(file='pulse.png')
        self.__pulse_1=self.__pulse.subsample(3,3)
        self.l_pulse=Label(self.__upper,image=self.__pulse_1,text='EL NOUR',compound=RIGHT,bg='white',fg='dark red',font=('Cooper Black',40)).place(x=10,y=10)
        self.__side = Frame(self.main,width=350,height=600,bg='white',highlightbackground='#999',highlightthickness=1)
        self.__side.place(x=10,y=150)
        self.middle = Frame(self.main,width=1000,height=900)
        self.middle.place(x=320,y=90)
        self.__pro = PhotoImage(file="doctor.png")
        self.__profile = self.__pro.subsample(1,1)
        self.__profile_label = Label(self.__side,image=self.__profile).place(x=40,y=20)
        global x

        if x==0:
            self.__user_label = Label(self.__side,text=ob.ent1in.get(),font=("arial",20))
            self.__user_label.place(x=100,y=280)
        else:
            self.__user_label = Label(self.__side, text=string_name, font=("arial", 20))
            self.__user_label.place(x=100, y=280)



        self.__setting = Button(self.__side,text="Setting", font=("arial",20),command=self.setting).place(x=20,y=400)
        self.__logout = Button(self.__side, text="Log out", font=("arial", 20),command=self.return_to_start).place(x=160, y=400)
        self.__return_fromCl = Button(self.__side, text="RETURN TO MAIN", font=("arial", 15),command=self.return_fromAllClasses).place(x=50, y=500)

        #middle fram
        self.doc_i=PhotoImage(file='doc.png')
        self.doc_img=self.doc_i.subsample(3,3)
        self.__doctor=Button(self.middle,text='DOCTOR',bg='white', relief = RAISED, overrelief = SUNKEN,command=self.doctor,height=300,width=250,compound=TOP,image=self.doc_img,fg='black',borderwidth=3,font=('arial',20))
        self.__doctor.place(x=50,y=50)
        self.pat_i=PhotoImage(file='patent.png')
        self.pat_img=self.pat_i.subsample(3,3)
        self.__patent=Button(self.middle,text='PATIENT',bg='white', relief = RAISED, overrelief = SUNKEN,image=self.pat_img,height=300,width=250,compound=TOP,fg='black',borderwidth=3,font=('arial',20),command=self.patient)
        self.__patent.place(x=380,y=50)
        self.staff_i=PhotoImage(file='staff.png')
        self.staff_img=self.staff_i.subsample(3,3)
        self.__staff=Button(self.middle,image=self.staff_img,compound=TOP,text='STAFF',height=300,width=250, relief = RAISED,command=self.staff, overrelief = SUNKEN,fg='black',bg='white',borderwidth=3,font=('arial',20))
        self.__staff.place(x=700,y=50)
        #lower icons

        self.nurse_i=PhotoImage(file='nurse.png')
        self.nurse_img=self.nurse_i.subsample(3,3)
        self.__nurse=Button(self.middle,text='NURSES',bg='white',image=self.nurse_img,command=self.nurse,height=300,width=250,compound=TOP, relief = RAISED, overrelief = SUNKEN,fg='black',borderwidth=3,font=('arial',20))
        self.__nurse.place(x=180,y=400)
        self.medical_i=PhotoImage(file='medical.png')
        self.medical_img=self.medical_i.subsample(3,3)
        self.__medical=Button(self.middle,image=self.medical_img,compound=TOP,text='MEDICAL STORE',command=self.medical, relief = RAISED, overrelief = SUNKEN,height=300,width=250,fg='black',bg='white',borderwidth=3,font=('arial',15))
        self.__medical.place(x=550,y=400)


    def return_to_start(self):
        self.main.place_forget()
        #self.__side.place_forget()
        Start.__init__(self,root)
        
        
    def doctor(self):
        doctor()

    def patient(self):
        patient()
    def staff(self):
        staff()
    def nurse(self):
        nurse()
    def medical(self):
        medical_store()
    def setting(self):
        self.middle.place_forget()

        self.setting_frame = Frame(self.main,width=950,height=700,bg="#f1f1f1")
        self.setting_frame.place(x=370,y=100)
        self.username_label = Label(self.setting_frame,text="USER NAME",font=("arial",20)).place(x=130,y=80)
        self.username_entry = Entry(self.setting_frame,font=("arial",20),borderwidth=2)
        self.username_entry.place(x=130,y=130)
        self.username_entry.focus()

        self.pass_label = Label(self.setting_frame, text="PASSWORD", font=("arial", 20)).place(x=130, y=200)
        self.pass_entry = Entry(self.setting_frame, font=("arial", 20),borderwidth=2)
        self.pass_entry.place(x=130, y=250)
        self.submit = Button(self.setting_frame, text="SUBMIT", font=("arial", 20),borderwidth=2,command=self.change).place(x=250,y=300)


    def change(self):
        global x
        global string_name
        if  x== 0:
            cur.execute(f"update logins set user_name ='{self.username_entry.get()}' where user_name = '{ob.ent1in.get()}' ")
            cur.execute(f"update logins set password ={self.pass_entry.get()} where password = {ob.ent2in.get()} ")
            x = 1
            self.changname = self.username_entry.get()
            self.changepass = self.pass_entry.get()
            con.commit()
            messagebox.showinfo("HOSPITAL", "OK")
            self.new_label = Label(self.__side, text=self.username_entry.get(), font=("arial", 20))
            self.new_label.place(x=100, y=280)
            self.setting_frame.place_forget()
            self.middle.place(x=320, y=90)

            self.__user_label.place_forget()


            string_name = self.changname


        else:
            self.new_label.place_forget()
            cur.execute(f"update logins set user_name ='{self.username_entry.get()}' where user_name = '{self.changname}' ")
            cur.execute(f"update logins set password ={self.pass_entry.get()} where password = {self.changepass} ")
            self.changname = self.username_entry.get()
            self.changepass = self.pass_entry.get()
            con.commit()
            messagebox.showinfo("HOSPITAL", "OK")
            self.new_label = Label(self.__side, text=self.username_entry.get(), font=("arial", 20))
            self.new_label.place(x=100, y=280)
            self.setting_frame.place_forget()
            self.middle.place(x=320, y=90)

            self.__user_label.place_forget()
            string_name = self.changname


        #self.__upper.pack()
    #add new person
    def add(self):
        self.new_fram=Frame(self.main,width=1000,height=800,bg="#f1f1f1")
        self.new_fram.place(x=320,y=100)
        self.middle.place_forget()
        self.add_person=Frame(self.new_fram,width=1000,highlightbackground="#cc0000", highlightthickness=3,height=800)
        self.add_person.place(x=50,y=10)
        self.add_name=Label(self.add_person,text='Name',font=('times',20))
        self.add_name.place(x=20,y=40)
        self.add_entery_n=Entry(self.add_person,font=('times',20),borderwidth=2)
        self.add_entery_n.place(x=20,y=80)
        self.add_age=Label(self.add_person,text='Age',font=('times',20))
        self.add_age.place(x=20,y=140)
        self.add_entery_a=Entry(self.add_person,font=('times',20),borderwidth=2)
        self.add_entery_a.place(x=20,y=190)

    def search(self):

        self.search_frame=Frame(self.main,width=1000,height=700)
        self.search_frame.place(x=320,y=90)
        self.middle.place_forget()
        self.search_id=Frame(self.search_frame,width=1000,height=700)
        self.search_id.place(x=20,y=90)
        self.id=Label(self.search_id,text='ID',font=('Cambria',20))
        self.id.place(x=20,y=10)
        self.id_entery=Entry(self.search_id,borderwidth=2,font=('times',20))
        self.id_entery.place(x=20,y=70)
        self.search_butt=Button(self.search_id,text='Search',font=('times',15),borderwidth=2,command=self.get_info)
        self.search_butt.place(x=350,y=65)



    def get_info(self):

        self.fetch_frame = Frame(self.search_id,width=1000,height=500,bg="#eec4ce",highlightbackground="#cc0000", highlightthickness=3)
        self.fetch_frame.place(x=0,y=150)
        self.display_name=Label(self.fetch_frame,text='NAME',font=('times',20),width=10)
        self.display_name.place(x=30,y=80)
        self.display_age=Label(self.fetch_frame,text='AGE',font=('times',20),width=10)
        self.display_age.place(x=30,y=140)

    def update_info(self):
        self.update_frame=Frame(self.main,width=1000,height=800,bg="#f1f1f1")
        self.update_frame.place(x=320,y=90)
        self.middle.place_forget()
        #self.update_frame1=Frame(self.update_frame,width=1000,height=800)
        #self.update_frame1.place(x=20,y=90)
        self.id_update=Label(self.update_frame,text='ID',font=('Cambria',20))
        self.id_update.place(x=20,y=90)
        self.id_entery_update=Entry(self.update_frame,borderwidth=2,font=('times',20))
        self.id_entery_update.place(x=20,y=150)

    def update_with_data(self):
        self.correct_id_frame = Frame(self.update_frame, width=1000, height=800)
        self.correct_id_frame.place(x=20, y=200)
        self.labeltit = Label(self.update_frame, text="CHOOSE TO UPDATE", font=("Forte", 30), fg="black")
        self.labeltit.place(x=300,y=230)

        self.button_update_name = Button(self.correct_id_frame, text="NAME", relief=RAISED, overrelief=SUNKEN,
                                         bg="#1fc585", font=("Arial", 30),command=self.update_name)
        self.button_update_name.place(x=150, y=140)

        self.button_update_age = Button(self.correct_id_frame, text="AGE", relief=RAISED, overrelief=SUNKEN,command=self.update_age,
                                         bg="#1fc585", font=("Arial", 30))
        self.button_update_age.place(x=400, y=140)
        self.button_update_age = Button(self.correct_id_frame, text="Gender", relief=RAISED, overrelief=SUNKEN,command=self.update_gender,
                                         bg="#1fc585", font=("Arial", 30))
        self.button_update_age.place(x=600, y=140)



        self.button_update_return = Button(self.correct_id_frame, text="RETURN", relief=RAISED, overrelief=SUNKEN,command=self.out_of_edit,
                                           bg="#1fc585", font=("Arial", 30))
        self.button_update_return.place(x=680, y=300)



    def out_of_edit(self):
        self.update_frame.place_forget()
        self.doc_frame.place(x=500, y=90)



    def update_gender(self):
        self.correct_id_frame.place_forget()
        self.labeltit.place_forget()
        self.correct_frame = Frame(self.update_frame, width=1000, height=800)
        self.correct_frame.place(x=20, y=200)
        self.var=StringVar(self.correct_frame,'1')
        self.gender_l=Label(self.correct_frame,text="Gender",font=('times',20)).place(x=20,y=100)
        self.male=Radiobutton(self.correct_frame,text='male',font=('times',20),variable=self.var,value='male')
        self.male.place(x=20,y=200)
        self.female=Radiobutton(self.correct_frame,text='female',font=('times',20),variable=self.var,value='female')
        self.female.place(x=160,y=200)
        self.sub=Button(self.correct_frame,text='Submit',command=self.save_gender,font=('times',25)).place(x=20,y=300)
        self.sub=Button(self.correct_frame,text='Return',command=self.return_from_updateIn,font=('times',25)).place(x=210,y=300)
    def update_name(self):
        self.correct_id_frame.place_forget()
        self.labeltit.place_forget()
        self.correct_frame = Frame(self.update_frame, width=1000, height=800)
        self.correct_frame.place(x=20, y=200)
        self._up_name_label = Label(self.correct_frame, text="ENTER NEW NAME", font=("Arial", 20)).place(x=20, y=100)
        self._up_name_entry = Entry(self.correct_frame, font=("Arial", 20))
        self._up_name_entry.place(x=350, y=100)
        self._up_name_button = Button(self.correct_frame, text="SUBMIT", font=("Arial", 30), relief=RAISED,command=self.save_name,
                                      overrelief=SUNKEN, bg="#1fc585")
        self._up_name_button.place(x=200, y=300)
        self.button_update_return_fromIn = Button(self.correct_frame, text="RETURN", relief=RAISED,
                                                  overrelief=SUNKEN,
                                                  command=self.return_from_updateIn,
                                                  bg="#1fc585", font=("Arial", 30))
        self.button_update_return_fromIn.place(x=430, y=300)



    def update_age(self):
        self.correct_id_frame.place_forget()
        self.labeltit.place_forget()
        self.correct_frame = Frame(self.update_frame, width=1000, height=800)
        self.correct_frame.place(x=20, y=200)
        self._up_age_label = Label(self.correct_frame, text="ENTER NEW AGE", font=("Arial", 20)).place(x=20, y=100)
        self._up_age_entry = Entry(self.correct_frame, font=("Arial", 20))
        self._up_age_entry.place(x=350, y=100)
        self._up_age_button = Button(self.correct_frame, text="SUBMIT", font=("Arial", 30), relief=RAISED,command=self.save_age,
                                    overrelief=SUNKEN, bg="#1fc585")
        self._up_age_button.place(x=200, y=300)
        self.button_update_return_fromIn = Button(self.correct_frame, text="RETURN", relief=RAISED,
                                                  overrelief=SUNKEN,
                                                  command=self.return_from_updateIn,
                                                  bg="#1fc585", font=("Arial", 30))
        self.button_update_return_fromIn.place(x=430, y=300)

    def update_salary(self):
        self.correct_id_frame.place_forget()
        self.labeltit.place_forget()
        self.correct_frame = Frame(self.update_frame, width=1000, height=800)
        self.correct_frame.place(x=20, y=200)
        self._up_salary_label = Label(self.correct_frame, text="ENTER NEW SALARY ", font=("Arial", 20)).place(x=20,
                                                                                                             y=100)
        self._up_salary_entry = Entry(self.correct_frame, font=("Arial", 20))
        self._up_salary_entry.place(x=400, y=100)
        self._up_salary_button = Button(self.correct_frame, text="SUBMIT", font=("Arial", 30), relief=RAISED,command=self.save_salary,
                                        overrelief=SUNKEN, bg="#1fc585")
        self._up_salary_button.place(x=200, y=300)
        self.button_update_return_fromIn = Button(self.correct_frame, text="RETURN", relief=RAISED,
                                                  overrelief=SUNKEN,
                                                  command=self.return_from_updateIn,
                                                  bg="#1fc585", font=("Arial", 30))
        self.button_update_return_fromIn.place(x=430, y=300)



    def update_major(self):
        self.correct_id_frame.place_forget()
        self.labeltit.place_forget()
        self.correct_frame = Frame(self.update_frame, width=1000, height=800)
        self.correct_frame.place(x=20, y=200)
        self._up_major_label = Label(self.correct_frame, text="ENTER NEW MAJOR", font=("Arial", 20)).place(x=20, y=100)
        self._up_major_entry = Entry(self.correct_frame, font=("Arial", 20))
        self._up_major_entry.place(x=300, y=100)
        self._up_major_button = Button(self.correct_frame, text="SUBMIT", font=("Arial", 30), relief=RAISED,command=self.save_major,
                                      overrelief=SUNKEN, bg="#1fc585")
        self._up_major_button.place(x=200, y=300)
        self.button_update_return_fromIn = Button(self.correct_frame, text="RETURN", relief=RAISED,
                                                  overrelief=SUNKEN,
                                                  command=self.return_from_updateIn,
                                                  bg="#1fc585", font=("Arial", 30))
        self.button_update_return_fromIn.place(x=430, y=300)

    def delete(self):
        self.delete_frame=Frame(self.main,width=1000,height=800,bg="#f1f1f1")
        self.delete_frame.place(x=320,y=90)
        self.middle.place_forget()
        self.delete_id=Frame(self.delete_frame,width=1000,height=900)
        self.delete_id.place(x=20,y=90)
        self.id_delete=Label(self.delete_id,text='ID',font=('Cambria',20))
        self.id_delete.place(x=20,y=90)
        self.id_delete_update=Entry(self.delete_id,borderwidth=2,font=('times',20))
        self.id_delete_update.place(x=20,y=150)
        self.delete_butt=Button(self.delete_id,text='DELETE',font=('times',15),borderwidth=2,command=self.msg)
        self.delete_butt.place(x=350,y=145)
        self.delete_buttret = Button(self.delete_id, text='RETURN', font=('times', 15), borderwidth=2, command=self.ret_del)
        self.delete_buttret.place(x=500, y=145)

    def msg(self):
        messagebox.showinfo("HOSPITAL","DELETED SUCCESSFULLY")
    def ret_del(self):
        self.delete_id.place_forget()
        self.delete_frame.place_forget()
        doctor().doc_frame.place(x=500, y=90)

    def return_from_updateIn(self):
        self.correct_frame.place_forget()
        self.correct_id_frame.place(x=20, y=200)
        self.labeltit.place(x=300,y=230)
#doctor class
class doctor(person):
    def __init__(self):
        super().__init__()
        self.middle.place_forget()
        self.doc_frame=Frame(self.main,height=800,width=1000)
        self.doc_frame.place(x=500,y=90)
        #add button
        self.add_i=PhotoImage(file='add.png')
        self.add_img=self.add_i.subsample(3,3)
        self.__add=Button(self.doc_frame,text='ADD',bg='white',height=300,fg='green',width=250,compound=TOP,cursor = 'cross', bd = 3 , relief = RAISED, overrelief = SUNKEN,image=self.add_img,borderwidth=3,font=('arial',20),command=self.add)
        self.__add.place(x=50,y=50)
        #search button
        self.search_i=PhotoImage(file='search.png')
        self.search_img=self.search_i.subsample(3,3)
        self.__search=Button(self.doc_frame,text='SEARCH',bg='white',height=300,width=250,compound=TOP,image=self.search_img, relief = RAISED, overrelief = SUNKEN,fg='sky blue',borderwidth=3,font=('arial',20),command=self.search)
        self.__search.place(x=450,y=50)
        #edit button
        self.edit_i=PhotoImage(file='edit.png')
        self.edit_img=self.edit_i.subsample(3,3)
        self.__edit=Button(self.doc_frame,text='EDIT',bg='white',command=self.update_info,height=300,width=250,compound=TOP, relief = RAISED, overrelief = SUNKEN,image=self.edit_img,fg='grey',borderwidth=3,font=('arial',20))
        self.__edit.place(x=50,y=400)
        #delet button
        self.delete_i=PhotoImage(file='delete.png')
        self.delete_img=self.delete_i.subsample(3,3)
        self.__delete=Button(self.doc_frame,text='DELETE',bg='white',fg='red',command=self.delete,height=300,width=250, relief = RAISED, overrelief = SUNKEN,compound=TOP,image=self.delete_img,borderwidth=3,font=('arial',20))
        self.__delete.place(x=450,y=400)
        #return button

        #add new doctor to database
    def add(self):
        super().add()
        self.add_label = Label(self.add_person,text="ADD DOCTOR",font=("Forte",30),fg="black").place(x=250,y=20)
        self.add_salary=Label(self.add_person,text='Salary',font=('times',20))
        self.add_salary.place(x=20,y=250)
        self.add_entery_s=Entry(self.add_person,font=('times',20),borderwidth=2)
        self.add_entery_s.place(x=20,y=300)
        
        self.add_major=Label(self.add_person,text='Major',font=('times',20))
        self.add_major.place(x=20,y=350)
        self.add_entery_m=Entry(self.add_person,font=('times',20),borderwidth=2)
        self.add_entery_m.place(x=20,y=400)
 
        self.v = StringVar(self.add_person, "1")
        self.gender_l=Label(self.add_person,text="Gender",font=('times',20)).place(x=20,y=480)
        self.male=Radiobutton(self.add_person,text='male',font=('times',20),variable=self.v,value='male')
        self.male.place(x=20,y=530)
        self.female=Radiobutton(self.add_person,text='female',font=('times',20),variable=self.v,value='female')
        self.female.place(x=150,y=530)
        self.add_button=Button(self.add_person,text='Add',font=('times',20),command=self.submit)
        self.add_button.place(x=20,y=600)
        self.addRet_button = Button(self.add_person, text='Return', font=('times', 20), command=self.back)
        self.addRet_button.place(x=200, y=600)
    def submit(self):
        if(self.add_entery_n.get() and self.add_entery_a.get() and self.add_entery_s.get() and self.add_entery_m.get()):
            messagebox.showinfo('hospital'.upper(),'Doctor added successfully')
            name=self.add_entery_n.get()
            age=self.add_entery_a.get()
            salary=self.add_entery_s.get()
            major=self.add_entery_m.get()
            gender=self.v.get()
            cur.execute(f"INSERT INTO doctors (name,age,salary,major,gender) VALUES ('{name}',{age},{salary}, '{major}','{gender}')")
            con.commit()
            self.add_person.place_forget()
            self.new_fram.place_forget()
            self.doc_frame.place(x=500,y=90)

        else:
            messagebox.showerror('hospital'.upper(),'please,fill all inputs')
    def back(self):
        self.add_person.place_forget()
        self.new_fram.place_forget()
        self.doc_frame.place(x=500,y=90)
    def search(self):

        super().search()
        self.search_buttRet = Button(self.search_id, text='Return', font=('times', 15), borderwidth=2,
                                     command=self.return_doctor_fun)
        self.search_buttRet.place(x=550, y=65)

    def get_info(self):

        cur.execute(f"select id from doctors where id = {self.id_entery.get()} ")
        result = cur.fetchone()
        if result:
            cur.execute(f"select * from doctors where id = {self.id_entery.get()}")
            name, age, id, salary, major,gender = cur.fetchone()

            super().get_info()
            self.fetch_doctor_name = Label(self.fetch_frame, text=name, font=("times", 20), width=10, )
            self.fetch_doctor_name.place(x=220, y=80)
            self.fetch_doctor_age = Label(self.fetch_frame, text=age, font=("times", 20), width=10).place(x=220, y=140)
            self.display_id = Label(self.fetch_frame, text="ID", font=("times", 20), width=10).place(x=30, y=200)
            self.fetch_doctor_id = Label(self.fetch_frame, text=id, font=("times", 20), width=10).place(x=220, y=200)
            self.fetch_doctor_salary = Label(self.fetch_frame, text=salary, font=("times", 20), width=10).place(x=220,
                                                                                                                y=260)
            self.display_salary = Label(self.fetch_frame, text="SALARY", font=("times", 20), width=10).place(x=30,
                                                                                                             y=260)
            self.fetch_doctor_major = Label(self.fetch_frame, text=major, font=("times", 20), width=10).place(x=220,
                                                                                                              y=320)
            self.display_major = Label(self.fetch_frame, text="MAJOR", font=("times", 20), width=10).place(x=30, y=320)
            self.fetch_doctor_gender = Label(self.fetch_frame, text=gender, font=("times", 20), width=10).place(x=220,
                                                                                                              y=370)
            self.display_gender = Label(self.fetch_frame, text="GENDER", font=("times", 20), width=10).place(x=30, y=370)




        else:

            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self.search_id.place_forget()
            self.search_frame.place_forget()

            self.doc_frame.place(x=500, y=90)

    def search_again(self):
        self.fetch_frame.place_forget()
        self.search()

    def return_doctor_fun(self):
        self.search_id.place_forget()
        self.search_frame.place_forget()

        self.doc_frame.place(x=500, y=90)

    def update_info(self):
        super().update_info()
        self.update_butt = Button(self.update_frame, text='Search', font=('times', 15), borderwidth=2, command=self.update_with_data)
        self.update_butt.place(x=350, y=140)
    def update_with_data(self):
        cur.execute(f"select id from doctors where id = {self.id_entery_update.get()} ")
        result = cur.fetchone()
        if result:
            super().update_with_data()
            self.button_update_salary = Button(self.correct_id_frame, text="SALARY", relief=RAISED, overrelief=SUNKEN,
                                           command=self.update_salary,
                                           bg="#1fc585", font=("Arial", 30))
            self.button_update_salary.place(x=120, y=300)

            self.button_update_major = Button(self.correct_id_frame, text="MAJOR", relief=RAISED, overrelief=SUNKEN,
                                          command=self.update_major,
                                          bg="#1fc585", font=("Arial", 30))
            self.button_update_major.place(x=400, y=300)

        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self.update_frame.place_forget()

            self.doc_frame.place(x=500, y=90)

    def update_name(self):
        super().update_name()
    def return_from_updateIn(self):
        super().return_from_updateIn()

    def save_name(self):
        cur.execute(
            f"update doctors set name= '{self._up_name_entry.get()}'where id = {self.id_entery_update.get()} ")
        con.commit()
        self.return_from_updateIn()

    def update_gender(self):
        super().update_gender()
    def save_gender(self):
        cur.execute(
            f"update doctors set gender= '{self.var.get()}'where id = {self.id_entery_update.get()} ")
        con.commit()
        self.return_from_updateIn()
    def update_age(self):
        super().update_age()
    def save_age(self):
        cur.execute(
            f"update doctors set age= {self._up_age_entry.get()} where id = {self.id_entery_update.get()} ")
        con.commit()
        self.return_from_updateIn()



    def update_major(self):
        super().update_major()
    def save_major(self):
        cur.execute(
            f"update doctors set major= '{self._up_major_entry.get()}' where id = {self.id_entery_update.get()} ")
        con.commit()
        self.return_from_updateIn()

    def update_salary(self):
        super().update_salary()
    def save_salary(self):
        cur.execute(
            f"update doctors set salary= {self._up_salary_entry.get()} where id = {self.id_entery_update.get()} ")
        con.commit()
        self.return_from_updateIn()

    def delete(self):
        super().delete()

    def msg(self):
        cur.execute(f"select id from doctors where id = {self.id_delete_update.get()} ")
        result = cur.fetchone()
        if result:
            cur.execute(f"delete from doctors where Id={self.id_delete_update.get()}")
            con.commit()
            super().msg()
            super().ret_del()

        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            super().ret_del()

class patient(person):
    def __init__(self):
        super().__init__()
        self.middle.place_forget()
        self.doc_frame = Frame(self.main, height=800, width=1000)
        self.doc_frame.place(x=500, y=90)
        # add button
        self.add_i = PhotoImage(file='add.png')
        self.add_img = self.add_i.subsample(3, 3)
        self.__add = Button(self.doc_frame, text='ADD', bg='white', height=300, fg='green', width=250, compound=TOP,
                            cursor='cross', bd=3, relief=RAISED, overrelief=SUNKEN, image=self.add_img, borderwidth=3,
                            font=('arial', 20), command=self.add)
        self.__add.place(x=50, y=50)
        # search button
        self.search_i = PhotoImage(file='search.png')
        self.search_img = self.search_i.subsample(3, 3)
        self.__search = Button(self.doc_frame, text='SEARCH', bg='white', height=300, width=250, compound=TOP,
                               image=self.search_img, relief=RAISED, overrelief=SUNKEN, fg='sky blue', borderwidth=3,
                               font=('arial', 20), command=self.search)
        self.__search.place(x=450, y=50)
        # edit button
        self.edit_i = PhotoImage(file='edit.png')
        self.edit_img = self.edit_i.subsample(3, 3)
        self.__edit = Button(self.doc_frame, text='EDIT', bg='white', command=self.update_info, height=300, width=250,
                             compound=TOP, relief=RAISED, overrelief=SUNKEN, image=self.edit_img, fg='grey',
                             borderwidth=3, font=('arial', 20))
        self.__edit.place(x=50, y=400)
        # delet button
        self.delete_i = PhotoImage(file='delete.png')
        self.delete_img = self.delete_i.subsample(3, 3)
        self.__delete = Button(self.doc_frame, text='DELETE', bg='white', fg='red', command=self.delete, height=300,
                               width=250, relief=RAISED, overrelief=SUNKEN, compound=TOP, image=self.delete_img,
                               borderwidth=3, font=('arial', 20))
        self.__delete.place(x=450, y=400)
    def add(self):
        super().add()
        self.today=date.today()
        self.tx=Label(self.add_person,text='date of entery'.capitalize(),font=('times',20)).place(x=20,y=280)
        self.day_l=Label(self.add_person,text='day',font=('times',20)).place(x=20,y=340)
        self.day=Entry(self.add_person,font=('times',15))
        self.day.place(x=80,y=344)
        self.month_l=Label(self.add_person,text='month',font=('times',20)).place(x=270,y=340)
        self.month=Entry(self.add_person,font=('times',15))
        self.month.place(x=380,y=344)
        self.year_l=Label(self.add_person,text='year',font=('times',20)).place(x=600,y=340)
        self.year=Entry(self.add_person,font=("times",15))
        self.year.place(x=690,y=344)
        self.v = StringVar(self.add_person, "1")
        self.gender_l=Label(self.add_person,text="Gender",font=('times',20)).place(x=20,y=400)
        self.male=Radiobutton(self.add_person,text='male',font=('times',20),variable=self.v,value='male')
        self.male.place(x=20,y=450)
        self.female=Radiobutton(self.add_person,text='female',font=('times',20),variable=self.v,value='female')
        self.female.place(x=150,y=450)
        self.sub=Button(self.add_person,text='submit',command=self.submit,font=('times',25)).place(x=20,y=520)
        self.sub=Button(self.add_person,text='Return',command=self.back,font=('times',25)).place(x=250,y=520)
    def back(self):
            self.add_person.place_forget()
            self.new_fram.place_forget()
            self.doc_frame.place(x=500,y=90)
    def submit(self):
        if(self.add_entery_n.get() and self.add_entery_a.get() and self.day.get() and self.month.get() and self.year.get(),self.v.get()):
            messagebox.showinfo('hospital'.upper(),'Patient added successfully')
            name=self.add_entery_n.get()
            age=self.add_entery_a.get()
            gender=self.v.get()
            days=self.today.day-int(self.day.get())
            months=self.today.month-int(self.month.get())
            years=self.today.year-int(self.year.get())
            if days<0:
                days=days+30
                months=months-1
            if months<0:
                months=months+12
                years=years-1
            cost=(days+months*30+years*365)*2000
            entery_date=f"{self.day.get()} " +r"/"+ f"{self.month.get()}"+"/"  +f"{self.year.get()}"
            
            cur.execute(f"INSERT INTO patient (name,bill,entery_date,age,gender) VALUES ('{name}',{cost},'{entery_date}', '{age}','{gender}')")
            con.commit()
            self.add_person.place_forget()
            self.new_fram.place_forget()
            self.doc_frame.place(x=500,y=90)
            

        else:
            messagebox.showerror('hospital'.upper(),'please,fill all inputs')

            

    def search(self):

        super().search()
        self.search_buttRet = Button(self.search_id, text='Return', font=('times', 15), borderwidth=2,
                                     command=self.return_patient_fun)
        self.search_buttRet.place(x=550, y=65)

    def get_info(self):


        cur.execute(f"select id from patient where id = {self.id_entery.get()} ")
        result = cur.fetchone()
        if result:
            cur.execute(f"select * from patient where id = {self.id_entery.get()}")
            name, id, bill,entery_date,age,gender = cur.fetchone()

            super().get_info()
            self.fetch_patient_name = Label(self.fetch_frame, text=name, font=("times", 20),width=10,)
            self.fetch_patient_name.place(x=220, y=80)
            self.fetch_patient_age = Label(self.fetch_frame,text=age,font=("times",20),width=10).place(x=220,y=140)
            self.display_id =Label(self.fetch_frame,text="ID",font=("times",20),width=10).place(x=30,y=200)
            self.fetch_patient_id = Label(self.fetch_frame,text=id,font=("times",20),width=10).place(x=220,y=200)
            self.fetch_patient_bill = Label(self.fetch_frame,text=bill,font=("times",20),width=10).place(x=220,y=260)
            self.display_salary = Label(self.fetch_frame, text="BILL", font=("times", 20),width=10).place(x=30, y=260)
            self.fetch_patient_entery = Label(self.fetch_frame,text=entery_date,font=("times",20),width=10).place(x=220,y=320)
            self.display_entery =Label(self.fetch_frame,text="DATE",font=("times",20),width=10).place(x=30,y=320)
            self.fetch_patient_gender = Label(self.fetch_frame,text=gender,font=("times",20),width=10).place(x=220,y=377)
            self.display_gender =Label(self.fetch_frame,text="GENDER",font=("times",20),width=10).place(x=30,y=377)



        else:

            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self.search_id.place_forget()
            self.search_frame.place_forget()

            self.doc_frame.place(x=500, y=90)


    def search_again(self):
        self.fetch_frame.place_forget()
        self.search()

    def return_patient_fun(self):
        self.search_id.place_forget()
        self.search_frame.place_forget()

        self.doc_frame.place(x=500,y=90)



    def update_info(self):
        super().update_info()
        self.update_butt = Button(self.update_frame, text='Search', font=('times', 15), borderwidth=2, command=self.update_with_data)
        self.update_butt.place(x=350, y=140)
    def update_with_data(self):
        cur.execute(f"select id from patient where id = {self.id_entery_update.get()} ")
        result = cur.fetchone()
        if result:
            super().update_with_data()


            self.button_update_bill = Button(self.correct_id_frame, text="bill".upper(), relief=RAISED, overrelief=SUNKEN,
                                           command=self.update_bill,
                                           bg="#1fc585", font=("Arial", 30))
            self.button_update_bill.place(x=120, y=300)

            self.button_update_date = Button(self.correct_id_frame, text="entery".upper(), relief=RAISED, overrelief=SUNKEN,
                                          command=self.update_entery_date,
                                          bg="#1fc585", font=("Arial", 30))
            self.button_update_date.place(x=350, y=300)




        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self.update_frame.place_forget()

            self.doc_frame.place(x=500, y=90)

        
    def update_name(self):
        super().update_name()

    def return_from_updateIn(self):
        super().return_from_updateIn()

    def save_name(self):
        cur.execute(
            f"update patient set name= '{self._up_name_entry.get()}'where id = {self.id_entery_update.get()} ")
        con.commit()
        self.return_from_updateIn()

    def update_age(self):
        super().update_age()
    def save_age(self):
        cur.execute(
            f"update patient set age= {self._up_age_entry.get()} where id = {self.id_entery_update.get()} ")
        con.commit()
        self.return_from_updateIn()


    def update_gender(self):
        super().update_gender()
    def save_gender(self):
        cur.execute(
            f"update patient set gender= '{self.var.get()}' where id = {self.id_entery_update.get()} ")
        con.commit()
        self.return_from_updateIn()

    def update_entery_date(self):
        self.correct_id_frame.place_forget()
        self.labeltit.place_forget()
        self.correct_frame = Frame(self.update_frame, width=1000, height=800)
        self.correct_frame.place(x=20, y=200)
        self._up_date_label = Label(self.correct_frame, text="ENTER NEW DATE", font=("Arial", 20)).place(x=20, y=100)
        self._up_date_entry = Entry(self.correct_frame, font=("Arial", 20))
        self._up_date_entry.place(x=300, y=100)
        self._up_date_button = Button(self.correct_frame, text="SUBMIT", font=("Arial", 30), relief=RAISED,
                                       command=self.save_entery_date,
                                       overrelief=SUNKEN, bg="#1fc585")
        self._up_date_button.place(x=200, y=300)
        self.button_update_return_fromIn = Button(self.correct_frame, text="RETURN", relief=RAISED,
                                                  overrelief=SUNKEN,
                                                  command=self.return_from_updateIn,
                                                  bg="#1fc585", font=("Arial", 30))
        self.button_update_return_fromIn.place(x=430, y=300)
    def save_entery_date(self):
        cur.execute(
            f"update patient set entery_date= {self._up_date_entry.get()} where id = {self.id_entery_update.get()} ")
        con.commit()
        self.return_from_updateIn()

    def update_bill(self):
        self.correct_id_frame.place_forget()
        self.labeltit.place_forget()
        self.correct_frame = Frame(self.update_frame, width=1000, height=800)
        self.correct_frame.place(x=20, y=200)
        self._up_bill_label = Label(self.correct_frame, text="ENTER NEW BILL", font=("Arial", 20)).place(x=20, y=100)
        self._up_bill_entry = Entry(self.correct_frame, font=("Arial", 20))
        self._up_bill_entry.place(x=300, y=100)
        self._up_bill_button = Button(self.correct_frame, text="SUBMIT", font=("Arial", 30), relief=RAISED,
                                       command=self.save_bill,
                                       overrelief=SUNKEN, bg="#1fc585")
        self._up_bill_button.place(x=200, y=300)
        self.button_update_return_fromIn = Button(self.correct_frame, text="RETURN", relief=RAISED,
                                                  overrelief=SUNKEN,
                                                  command=self.return_from_updateIn,
                                                  bg="#1fc585", font=("Arial", 30))
        self.button_update_return_fromIn.place(x=430, y=300)

    def save_bill(self):
        cur.execute(
            f"update patient set bill= {self._up_bill_entry.get()} where id = {self.id_entery_update.get()} ")
        con.commit()
        self.return_from_updateIn()

    def delete(self):
        super().delete()

    def msg(self):
        cur.execute(f"select id from patient where id = {self.id_delete_update.get()} ")
        result = cur.fetchone()
        if result:
            cur.execute(f"delete from patient where Id={self.id_delete_update.get()}")
            con.commit()
            #person.msg()
            messagebox.showinfo('hospital'.upper(), 'deleted')
            super().ret_del()

        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            super().ret_del()


class staff(doctor):
    def __init__(self):
       # person.__init__(self)
        super().__init__()

    def add(self):
        person.add(self)
        self.add_salary=Label(self.add_person,text='Salary',font=('times',20))
        self.add_salary.place(x=20,y=250)
        self.add_entery_s=Entry(self.add_person,font=('times',20),borderwidth=2)
        self.add_entery_s.place(x=20,y=300)
        self.add_major=Label(self.add_person,text='Department',font=('times',20))
        self.add_major.place(x=20,y=350)
        self.add_entery_m=Entry(self.add_person,font=('times',20),borderwidth=2)
        self.add_entery_m.place(x=20,y=400)
        self.v = StringVar(self.add_person, "1")
        self.gender_l=Label(self.add_person,text="Gender",font=('times',20)).place(x=20,y=450)
        self.male=Radiobutton(self.add_person,text='male',font=('times',20),variable=self.v,value='male')
        self.male.place(x=20,y=500)
        self.female=Radiobutton(self.add_person,text='female',font=('times',20),variable=self.v,value='female')
        self.female.place(x=150,y=500)
        
        self.add_button=Button(self.add_person,text='Add',font=('times',20),command=self.submit)
        self.add_button.place(x=20,y=590)
        self.addRet_button = Button(self.add_person, text='Return', font=('times', 20), command=self.return_from_Add)
        self.addRet_button.place(x=200, y=590)

    def submit(self):
        if(self.add_entery_n.get() and self.add_entery_a.get() and self.add_entery_s.get() and self.add_entery_m.get() and self.v.get()):
            messagebox.showinfo('hospital'.upper(),'employee added successfully')
            name=self.add_entery_n.get()
            age=self.add_entery_a.get()
            salary=self.add_entery_s.get()
            department=self.add_entery_m.get()
            gender=self.v.get()
            cur.execute(f"INSERT INTO staff (name,age,salary,department,gender) VALUES ('{name}',{age},{salary}, '{department}','{gender}')")
            con.commit()
            self.return_from_Add()

        else:
            messagebox.showerror('hospital'.upper(),'please,fill all inputs')

    def return_from_Add(self):
        self.add_person.place_forget()
        self.new_fram.place_forget()
        self.doc_frame.place(x=500,y=90)
            



    def search(self):
        super().search()
        self.search_buttRet = Button(self.search_id, text='Return', font=('times', 15), borderwidth=2,
                                     command=self.return_doctor_fun)
        self.search_buttRet.place(x=550, y=65)

    def get_info(self):


        cur.execute(f"select id from staff where id = {self.id_entery.get()} ")
        result = cur.fetchone()
        if result:
            cur.execute(f"select * from staff where id = {self.id_entery.get()}")
            name, id, salary, department, age,gender = cur.fetchone()
            

            super(doctor, self).get_info()
            self.fetch_doctor_name = Label(self.fetch_frame, text=name, font=("times", 20),width=10,)
            self.fetch_doctor_name.place(x=220, y=80)
            self.fetch_doctor_age = Label(self.fetch_frame,text=age,font=("times",20),width=10).place(x=220,y=140)
            self.display_id =Label(self.fetch_frame,text="ID",font=("times",20),width=10).place(x=30,y=200)
            self.fetch_doctor_id = Label(self.fetch_frame,text=id,font=("times",20),width=10).place(x=220,y=200)
            self.fetch_doctor_salary = Label(self.fetch_frame,text=salary,font=("times",20),width=10).place(x=220,y=260)
            self.display_salary = Label(self.fetch_frame, text="SALARY", font=("times", 20),width=10).place(x=30, y=260)
            self.fetch_doctor_major = Label(self.fetch_frame,text=department,font=("times",20),width=10).place(x=220,y=320)
            self.display_major =Label(self.fetch_frame,text="Depart.".upper(),font=("times",20),width=10).place(x=30,y=320)
            self.fetch_doctor_gender = Label(self.fetch_frame,text=gender,font=("times",20),width=10).place(x=220,y=380)
            self.display_gender =Label(self.fetch_frame,text="Gender.".upper(),font=("times",20),width=10).place(x=30,y=380)



        else:

            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self.search_id.place_forget()
            self.search_frame.place_forget()

            self.doc_frame.place(x=500, y=90)
    def delete(self):
        super().delete()

    def msg(self):
        cur.execute(f"select id from staff where id = {self.id_delete_update.get()} ")
        result = cur.fetchone()
        
        if result:
            cur.execute(f"delete from staff where Id={self.id_delete_update.get()}")
            con.commit()
            person.msg(self)
            person().ret_del()

        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            person().ret_del()


    def update_info(self):
        super().update_info()
        self.update_butt = Button(self.update_frame, text='Search', font=('times', 15), borderwidth=2, command=self.update_with_data_staff)
        self.update_butt.place(x=350, y=140)
    def update_with_data_staff(self):
        cur.execute(f"select id from staff where id = {self.id_entery_update.get()} ")
        result = cur.fetchone()
        if result:
            person.update_with_data(self)
            
            self.button_update_salary = Button(self.correct_id_frame, text="SALARY", relief=RAISED, overrelief=SUNKEN,
                                           command=self.update_salary,
                                           bg="#1fc585", font=("Arial", 30))
            self.button_update_salary.place(x=120, y=300)

            self.button_update_major = Button(self.correct_id_frame, text="depart.".upper(), relief=RAISED, overrelief=SUNKEN,
                                          command=self.update_depart,
                                          bg="#1fc585", font=("Arial", 30))
            self.button_update_major.place(x=400, y=300)

        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self.update_frame.place_forget()

            self.doc_frame.place(x=500, y=90)

    def update_name(self):
        super().update_name()



    def save_name(self):
        cur.execute(
            f"update staff set name= '{self._up_name_entry.get()}'where id = {self.id_entery_update.get()} ")
        con.commit()
        super().return_from_updateIn()
    def update_gender(self):
        super().update_gender()
    def save_gender(self):
        cur.execute(  f"update staff set gender= '{self.var.get()}'where id = {self.id_entery_update.get()} ")
        con.commit()
        super().return_from_updateIn()
        
    def update_age(self):
        super().update_age()
    def save_age(self):
        cur.execute(
            f"update staff set age= {self._up_age_entry.get()} where id = {self.id_entery_update.get()} ")
        con.commit()
        super().return_from_updateIn()



    def update_depart(self):
        self.correct_id_frame.place_forget()
        self.labeltit.place_forget()
        self.correct_frame = Frame(self.update_frame, width=1000, height=800)
        self.correct_frame.place(x=20, y=200)
        self._up_depart_label = Label(self.correct_frame, text="ENTER NEW department", font=("Arial", 20)).place(x=20, y=100)
        self._up_depart_entry = Entry(self.correct_frame, font=("Arial", 20))
        self._up_depart_entry.place(x=420, y=100)
        self._up_depart_button = Button(self.correct_frame, text="SUBMIT", font=("Arial", 30), relief=RAISED,
                                       command=self.save_depart,
                                       overrelief=SUNKEN, bg="#1fc585")
        self._up_depart_button.place(x=200, y=300)
        self.button_update_return_fromIn = Button(self.correct_frame, text="RETURN", relief=RAISED,
                                                  overrelief=SUNKEN,
                                                  command=self.return_from_updateIn,
                                                  bg="#1fc585", font=("Arial", 30))
        self.button_update_return_fromIn.place(x=430, y=300)

    def save_depart(self):
        cur.execute(
            f"update staff set department= '{self._up_depart_entry.get()}' where id = {self.id_entery_update.get()} ")
        con.commit()
        super().return_from_updateIn()

    def update_salary(self):
        super().update_salary()
    def save_salary(self):
        cur.execute(
            f"update staff set salary= {self._up_salary_entry.get()} where id = {self.id_entery_update.get()} ")
        con.commit()
        super().return_from_updateIn()
    def out_of_edit(self):
        super().out_of_edit()


class nurse(doctor):
    def __init__(self):
       # person.__init__(self)
        super().__init__()

    def add(self):
        person.add(self)
        self.add_salary=Label(self.add_person,text='Salary',font=('times',20))
        self.add_salary.place(x=20,y=250)
        self.add_entery_s=Entry(self.add_person,font=('times',20),borderwidth=2)
        self.add_entery_s.place(x=20,y=300)
        self.add_major=Label(self.add_person,text='Major',font=('times',20))
        self.add_major.place(x=20,y=350)
        self.add_entery_m=Entry(self.add_person,font=('times',20),borderwidth=2)
        self.add_entery_m.place(x=20,y=400)
        self.v = StringVar(self.add_person, "1")
        self.gender_l=Label(self.add_person,text="Gender",font=('times',20)).place(x=20,y=450)
        self.male=Radiobutton(self.add_person,text='male',font=('times',20),variable=self.v,value='male')
        self.male.place(x=20,y=500)
        self.female=Radiobutton(self.add_person,text='female',font=('times',20),variable=self.v,value='female')
        self.female.place(x=150,y=500)
        
        self.add_button=Button(self.add_person,text='Add',font=('times',20),command=self.submit)
        self.add_button.place(x=20,y=590)
        self.addRet_button = Button(self.add_person, text='Return', font=('times', 20), command=self.return_from_Add)
        self.addRet_button.place(x=200, y=590)
    def submit(self):
        if(self.add_entery_n.get() and self.add_entery_a.get() and self.add_entery_s.get() and self.add_entery_m.get(),self.v.get()):
            messagebox.showinfo('hospital'.upper(),'nurse added successfully')
            name=self.add_entery_n.get()
            age=self.add_entery_a.get()
            salary=self.add_entery_s.get()
            major=self.add_entery_m.get()
            gender=self.v.get()
            cur.execute(f"INSERT INTO nurses (name,age,salary,major,gender) VALUES ('{name}',{age},{salary}, '{major}','{gender}')")
            con.commit()
            self.return_from_updateIn()
            
        else:
            messagebox.showerror('hospital'.upper(),'please,fill all inputs')
    def search(self):
        super().search()
    def get_info(self):


        cur.execute(f"select id from nurses where id = {self.id_entery.get()} ")
        result = cur.fetchone()
        if result:
            cur.execute(f"select * from nurses where id = {self.id_entery.get()}")
            name, age,id, salary, major,gender = cur.fetchone()
            

            super(doctor, self).get_info()
            self.fetch_doctor_name = Label(self.fetch_frame, text=name, font=("times", 20),width=10,)
            self.fetch_doctor_name.place(x=220, y=80)
            self.fetch_doctor_age = Label(self.fetch_frame,text=age,font=("times",20),width=10).place(x=220,y=140)
            self.display_id =Label(self.fetch_frame,text="ID",font=("times",20),width=10).place(x=30,y=200)
            self.fetch_doctor_id = Label(self.fetch_frame,text=id,font=("times",20),width=10).place(x=220,y=200)
            self.fetch_doctor_salary = Label(self.fetch_frame,text=salary,font=("times",20),width=10).place(x=220,y=260)
            self.display_salary = Label(self.fetch_frame, text="SALARY", font=("times", 20),width=10).place(x=30, y=260)
            self.fetch_doctor_major = Label(self.fetch_frame,text=major,font=("times",20),width=10).place(x=220,y=320)
            self.display_major =Label(self.fetch_frame,text="Major".upper(),font=("times",20),width=10).place(x=30,y=320)
            self.fetch_doctor_gender = Label(self.fetch_frame,text=gender,font=("times",20),width=10).place(x=220,y=370)
            self.display_gender =Label(self.fetch_frame,text="Gender".upper(),font=("times",20),width=10).place(x=30,y=370)

            self.return_doctor = Button(self.fetch_frame,text="RETURN",font=("Algerian",20),command=self.return_doctor_fun)
            self.return_doctor.place(x=600,y=100)
            self.search_doctor = Button(self.fetch_frame, text="SEARCH AGAIN", font=("Algerian", 20),
                                        command=self.search_again)
            self.search_doctor.place(x=600, y=200)

        else:

            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self.search_id.place_forget()
            self.search_frame.place_forget()

            self.doc_frame.place(x=500, y=90)
    def delete(self):
        super().delete()
    def return_from_Add(self):
        self.add_person.place_forget()
        self.new_fram.place_forget()
        self.doc_frame.place(x=500,y=90)
            

    def msg(self):
        cur.execute(f"select id from nurses where id = {self.id_delete_update.get()} ")
        result = cur.fetchone()
        
        if result:
            cur.execute(f"delete from nurses where Id={self.id_delete_update.get()}")
            con.commit()
            person.msg(self)
            person().ret_del()


        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            person().ret_del()


    def update_info(self):
        super().update_info()
        self.update_butt = Button(self.update_frame, text='Search', font=('times', 15), borderwidth=2, command=self.update_with_data_staff)
        self.update_butt.place(x=350, y=140)


    def update_with_data_staff(self):
        cur.execute(f"select id from nurses where id = {self.id_entery_update.get()} ")
        result = cur.fetchone()
        if result:
            person.update_with_data(self)
            
            self.button_update_salary = Button(self.correct_id_frame, text="SALARY", relief=RAISED, overrelief=SUNKEN,
                                           command=self.update_salary,
                                           bg="#1fc585", font=("Arial", 30))
            self.button_update_salary.place(x=120, y=300)

            self.button_update_major = Button(self.correct_id_frame, text="MAJOR.".upper(), relief=RAISED, overrelief=SUNKEN,
                                          command=self.update_depart,
                                          bg="#1fc585", font=("Arial", 30))
            self.button_update_major.place(x=400, y=300)

        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self.update_frame.place_forget()

            self.doc_frame.place(x=500, y=90)

    def update_name(self):
        super().update_name()

    def save_name(self):
        cur.execute(
            f"update nurses set name= '{self._up_name_entry.get()}'where id = {self.id_entery_update.get()} ")
        con.commit()
        super().return_from_updateIn()

    def update_age(self):
        super().update_age()
    def save_age(self):
        cur.execute(
            f"update nurses set age= {self._up_age_entry.get()} where id = {self.id_entery_update.get()} ")
        con.commit()
        super().return_from_updateIn()

    def update_gender(self):
        super().update_gender()
    def save_gender(self):
        cur.execute(
            f"update nurses set gender= '{self.var.get()}' where id = {self.id_entery_update.get()} ")
        con.commit()
        super().return_from_updateIn()
        

    def update_depart(self):
        self.correct_id_frame.place_forget()
        self.labeltit.place_forget()
        self.correct_frame = Frame(self.update_frame, width=1000, height=800)
        self.correct_frame.place(x=20, y=200)
        self._up_depart_label = Label(self.correct_frame, text="ENTER NEW Major", font=("Arial", 20)).place(x=20, y=100)
        self._up_depart_entry = Entry(self.correct_frame, font=("Arial", 20))
        self._up_depart_entry.place(x=420, y=100)
        self._up_depart_button = Button(self.correct_frame, text="SUBMIT", font=("Arial", 30), relief=RAISED,
                                       command=self.save_depart,
                                       overrelief=SUNKEN, bg="#1fc585")
        self._up_depart_button.place(x=200, y=300)
        self.button_update_return_fromIn = Button(self.correct_frame, text="RETURN", relief=RAISED,
                                                  overrelief=SUNKEN,
                                                  command=self.return_from_updateIn,
                                                  bg="#1fc585", font=("Arial", 30))
        self.button_update_return_fromIn.place(x=430, y=300)
    def save_depart(self):
        cur.execute(
            f"update nurses set department= '{self._up_depart_entry.get()}' where id = {self.id_entery_update.get()} ")
        con.commit()
        super().return_from_updateIn()

    def update_salary(self):
        super().update_salary()
    def save_salary(self):
        cur.execute(
            f"update nurses set salary= {self._up_salary_entry.get()} where id = {self.id_entery_update.get()} ")
        con.commit()
        super().return_from_updateIn()
    def out_of_edit(self):
        super().out_of_edit()

class medical_store:
    def __init__(self):
        person().middle.place_forget()
        self.medical_frame = Frame(root, width=1000, height=700)
        self.medical_frame.place(x=330, y=120)
        """self.medical_frame_p = PhotoImage(file="med_doc.png")
        self.medical_frame_ph=self.medical_frame_p.subsample(1,1)
        self.medical_frame_p_label =Label(self.medical_frame,image=self.medical_frame_ph)
        self.medical_frame_p_label.place(x=700,y=20)"""
        self.bg=PhotoImage(file='pharma.png')
        self.bg_i=self.bg.subsample(1,1)
        self.back=Label(self.medical_frame,image=self.bg_i).place(x=0,y=0)
        self.say_welcom=Label(self.medical_frame,bg="white",text='welcome to pharmacy'.capitalize(),font=('forte',30))
        self.say_welcom.place(x=290,y=10)
        #self.add_ph=PhotoImage(file="add_med.png")
       # self.add_med=self.add_ph.subsample(5,5)
        self.add=PhotoImage(file='add_med.png')
        self.add_med=self.add.subsample(3,3)
        self.add_but_med=Button(self.medical_frame,image=self.add_med,width=300,text='ADD',bg='white', relief = RAISED, overrelief = SUNKEN,compound=TOP,fg='black',borderwidth=3,font=('arial',20),command=self.add_med_fun)
        self.add_but_med.place(x=120,y=90)

        self.search=PhotoImage(file='search_med.png')
        self.search_med=self.search.subsample(3,3)
        self.search_but_med = Button(self.medical_frame,image=self.search_med, text='SEARCH', bg='white', relief=RAISED, overrelief=SUNKEN,
                                compound=TOP, fg='black',width=300, borderwidth=3, font=('arial', 20), command=self.search_med_fun)
        self.search_but_med.place(x=590, y=90)

        self.delete=PhotoImage(file='delete_med.png')
        self.delete_med=self.delete.subsample(3,3)
        self.delete_but_med = Button(self.medical_frame,image=self.delete_med,text="DELETE",bg='white', relief=RAISED, overrelief=SUNKEN,
                                compound=TOP,width=300, fg='black', borderwidth=3, font=('arial', 20), command=self.delete_med_fun)
        self.delete_but_med.place(x=120, y=400)

        self.update=PhotoImage(file='update.png')
        self.update_med=self.update.subsample(3,3)
        self.delete_but_med = Button(self.medical_frame,image=self.update_med, text="UPDATE", bg='white', relief=RAISED, overrelief=SUNKEN,
                                     compound=TOP, fg='black', borderwidth=3,width=300, font=('arial', 20),
                                     command=self.update_med_fun)
        self.delete_but_med.place(x=590, y=400)


    def add_med_fun(self):
        self.medical_frame.place_forget()
        self.add_med_frame=Frame(root,width=1000,height=700)
        self.add_med_frame.place(x=340,y=120)
        self.Label_frame=LabelFrame(self.add_med_frame,width=1000,height=700,bg="#ffe6e6",text="ADD MEDICINE",font=("Algerian",25))
        self.Label_frame.pack(fill="both", expand="yes")
        self.Label_frame.place(x=40,y=20)
        self.Label_add_medName =Label(self.Label_frame,text="NAME",font=("Arial",20))
        self.Label_add_medName.place(x=80,y=50)
        self.Entry_add_medName = Entry(self.Label_frame, font=("Arial", 20))
        self.Entry_add_medName.place(x=230, y=50)
        self.Label_add_medPrice = Label(self.Label_frame, text="PRICE", font=("Arial", 20))
        self.Label_add_medPrice.place(x=80, y=150)
        self.Entry_add_medPrice = Entry(self.Label_frame, font=("Arial", 20))
        self.Entry_add_medPrice.place(x=230, y=150)
        self.Label_add_medAmount = Label(self.Label_frame, text="AMOUNT", font=("Arial", 20))
        self.Label_add_medAmount.place(x=80, y=250)
        self.Entry_add_medAmount = Entry(self.Label_frame, font=("Arial", 20))
        self.Entry_add_medAmount.place(x=230, y=250)

        self.Button_add_medReturn = Button(self.Label_frame, text="RETURN", font=("Algerian", 20), relief = RAISED, overrelief = SUNKEN,bg="#ff8080",command=self._return_from_add)
        self.Button_add_medReturn.place(x=250, y=350)

        self.Button_add_medSubmit = Button(self.Label_frame, text="SUBMIT",font=("Algerian", 20), relief = RAISED, overrelief = SUNKEN,bg="#ff8080",command=self._submit)
        self.Button_add_medSubmit.place(x=500, y=350)


    def _return_from_add(self):
        self.add_med_frame.place_forget()
        self.medical_frame.place(x=330, y=120)

    def _submit(self):
        if (self.Entry_add_medName.get() and self.Entry_add_medPrice.get() and self.Entry_add_medAmount.get()):
            name = self.Entry_add_medName.get()
            price = self.Entry_add_medPrice.get()
            amount = self.Entry_add_medAmount.get()
            cur.execute(f"INSERT INTO medical_store (name,price,amount) VALUES ('{name}',{price},{amount})")
            con.commit()
            messagebox.showinfo('hospital'.upper(), 'Added successfully')
            self._return_from_add()
        else:
            messagebox.showerror('hospital'.upper(), 'please,fill all inputs')

    def search_med_fun(self):
        self.medical_frame.place_forget()
        self.search_med_frame = Frame(root, width=1000, height=700)
        self.search_med_frame.place(x=340, y=120)
        self.Label_frame_se = LabelFrame(self.search_med_frame, width=1000, height=700, bg="#ffe6e6", text="SEARCH",
                                      font=("Algerian", 25))
        self.Label_frame_se.pack(fill="both", expand="yes")
        self.Label_frame_se.place(x=40, y=20)
        self.Label_search_medid = Label(self.Label_frame_se, text="ENTER ID", font=("Arial", 20))
        self.Label_search_medid.place(x=80, y=70)
        self.Entry_search_medid = Entry(self.Label_frame_se, font=("Arial", 20))
        self.Entry_search_medid.place(x=230, y=70)
        self.Button_search_med = Button(self.Label_frame_se, text="SEARCH", font=("Algerian", 15), relief=RAISED,
                                           overrelief=SUNKEN, bg="#ff8080", command=self.check)
        self.Button_search_med.place(x=550, y=70)

        self.but_returnFromSearch_med = Button(self.Label_frame_se, text="RETURN", font=("Algerian", 15),
                                           relief=RAISED,
                                           overrelief=SUNKEN, bg="#ff8080",
                                           command=self._return_from_returnSearch_medFun)
        self.but_returnFromSearch_med.place(x=700, y=70)
    def check(self):
        cur.execute(f"select id from medical_store where id = {self.Entry_search_medid.get()} ")
        result = cur.fetchone()
        if result:

            cur.execute(f"select * from medical_store where id = {self.Entry_search_medid.get()}")
            name, id,price, amount = cur.fetchone()
            self.Label_search_medname0 = Label(self.Label_frame_se, text="NAME", font=("Arial", 20),width=10)
            self.Label_search_medname0.place(x=80, y=180)
            self.Label_search_medname1 = Label(self.Label_frame_se, text=name, font=("Arial", 20),width=10)
            self.Label_search_medname1.place(x=280, y=180)
            self.Label_search_medid0 = Label(self.Label_frame_se, text="ID", font=("Arial", 20),width=10)
            self.Label_search_medid0.place(x=80, y=280)
            self.Label_search_medid1 = Label(self.Label_frame_se, text=id, font=("Arial", 20),width=10)
            self.Label_search_medid1.place(x=280, y=280)
            self.Label_search_medprice0 = Label(self.Label_frame_se, text="PRICE", font=("Arial", 20),width=10)
            self.Label_search_medprice0.place(x=80, y=380)
            self.Label_search_medprice1 = Label(self.Label_frame_se, text=price, font=("Arial", 20),width=10)
            self.Label_search_medprice1.place(x=280, y=380)
            self.Label_search_medamount0 = Label(self.Label_frame_se, text="AMOUNT", font=("Arial", 20),width=10)
            self.Label_search_medamount0.place(x=80, y=480)
            self.Label_search_medamount1 = Label(self.Label_frame_se, text=amount, font=("Arial", 20),width=10)
            self.Label_search_medamount1.place(x=280, y=480)

            """ self.but_searchagain_med =Button(self.Label_frame_se,text="SEARCH AGAIN",font=("Algerian", 20), relief=RAISED,
                                           overrelief=SUNKEN, bg="#ff8080",command=self._search_again)
            self.but_searchagain_med.place(x=600,y=300)
    
            def _search_again(self):
                self.search_med_fun()
            """
        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self._return_from_returnSearch_medFun()

    def _return_from_returnSearch_medFun(self):
        self.search_med_frame.place_forget()

        self.medical_frame.place(x=330, y=120)

    def delete_med_fun(self):
        self.medical_frame.place_forget()
        self.delete_med_frame = Frame(root, width=1000, height=700)
        self.delete_med_frame.place(x=340, y=120)
        self.delete_frame_se = LabelFrame(self.delete_med_frame, width=1000, height=700, bg="#ffe6e6", text="DELETE",
                                         font=("Algerian", 25))
        self.delete_frame_se.pack(fill="both", expand="yes")
        self.delete_frame_se.place(x=40, y=20)
        self.Label_delete_medid = Label(self.delete_frame_se, text="ENTER ID", font=("Arial", 20))
        self.Label_delete_medid.place(x=80, y=70)
        self.Entry_delete_medid = Entry(self.delete_frame_se, font=("Arial", 20))
        self.Entry_delete_medid.place(x=230, y=70)
        self.Button_delete_med = Button(self.delete_frame_se, text="DELETE", font=("Algerian", 15), relief=RAISED,
                                        overrelief=SUNKEN, bg="#ff8080", command=self.check_del_med)
        self.Button_delete_med.place(x=550, y=70)

        self.but_returnFromDelete_med = Button(self.delete_frame_se, text="RETURN", font=("Algerian", 15),
                                               relief=RAISED,
                                               overrelief=SUNKEN, bg="#ff8080",
                                               command=self._return_from_returnDelete_medFun)
        self.but_returnFromDelete_med.place(x=700, y=70)

    def check_del_med(self):
        cur.execute(f"select id from medical_store where id = {self.Entry_delete_medid.get()} ")
        result = cur.fetchone()
        if result:
            cur.execute(f"delete from medical_store where Id={self.Entry_delete_medid.get()}")
            con.commit()
            messagebox.showinfo('hospital'.upper(), 'DELETED SUCCESSFULLY')
            self._return_from_returnDelete_medFun()


        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self._return_from_returnDelete_medFun()

    def _return_from_returnDelete_medFun(self):
        self.delete_med_frame.place_forget()
        self.medical_frame.place(x=330, y=120)


    def update_med_fun(self):
        self.medical_frame.place_forget()
        self.update_med_frame = Frame(root, width=1000, height=700)
        self.update_med_frame.place(x=340, y=120)
        self.Label_frame_up = LabelFrame(self.update_med_frame, width=1000, height=700, bg="#ffe6e6", text="UPDATE",
                                         font=("Algerian", 25))
        self.Label_frame_up.pack(fill="both", expand="yes")
        self.Label_frame_up.place(x=40, y=20)
        self.Label_update_medid = Label(self.Label_frame_up, text="ENTER ID", font=("Arial", 20))
        self.Label_update_medid.place(x=80, y=70)
        self.Entry_update_medid = Entry(self.Label_frame_up, font=("Arial", 20))
        self.Entry_update_medid.place(x=230, y=70)
        self.Button_update_med = Button(self.Label_frame_up, text="SEARCH", font=("Algerian", 15), relief=RAISED,
                                        overrelief=SUNKEN, bg="#ff8080", command=self.check_up_med)
        self.Button_update_med.place(x=550, y=70)

        self.but_returnFromUpdate_med = Button(self.Label_frame_up, text="RETURN", font=("Algerian", 15),
                                               relief=RAISED,command=self._but_returnFromUpdate_medFun,
                                               overrelief=SUNKEN, bg="#ff8080")

        self.but_returnFromUpdate_med.place(x=700, y=70)

    def _but_returnFromUpdate_medFun(self):
        self.update_med_frame.place_forget()
        self.medical_frame.place(x=330, y=120)


    def check_up_med(self):
        cur.execute(f"select id from medical_store where id = {self.Entry_update_medid.get()} ")
        result = cur.fetchone()
        if result:
            self.up_butNameMed = Button(self.Label_frame_up,text="NAME", font=("Algerian", 25),
                                               relief=RAISED,command=self.updateNameMed,
                                               overrelief=SUNKEN, bg="#ff8080")
            self.up_butNameMed.place(x=100,y=230)
            self.up_butPriceMed = Button(self.Label_frame_up, text="PRICE", font=("Algerian", 25),
                                        relief=RAISED,command=self.updatePriceMed,
                                        overrelief=SUNKEN, bg="#ff8080")
            self.up_butPriceMed.place(x=100, y=330)
            self.up_butAmountMed = Button(self.Label_frame_up, text="AMOUNT", font=("Algerian", 25),
                                        relief=RAISED,command=self.updateAmountMed,
                                        overrelief=SUNKEN, bg="#ff8080")
            self.up_butAmountMed.place(x=100, y=430)
        else:
            messagebox.showerror('hospital'.upper(), 'ERROR INPUT')
            self._but_returnFromUpdate_medFun()

    def updateNameMed(self):
        self.up_butNameMed.place_forget()
        self.up_labelNameMed = Label(self.Label_frame_up, text="ENTER NEW NAME", font=("Arial", 20))
        self.up_labelNameMed.place(x=100, y=230)
        self.up_entryNameMed = Entry(self.Label_frame_up, font=("Arial", 20))
        self.up_entryNameMed.place(x=400, y=230)
        self.up_butNameMed0 = Button(self.Label_frame_up, text="UPDATE", font=("Algerian", 15),
                                    relief=RAISED,
                                    overrelief=SUNKEN, bg="#ff8080",command=self.update_name_med)
        self.up_butNameMed0.place(x=800, y=230)
    def update_name_med(self):
        cur.execute(
            f"update medical_store set name= '{self.up_entryNameMed.get()}' where id = {self.Entry_update_medid.get()} ")
        con.commit()
        messagebox.showinfo('hospital'.upper(), 'UPDATED SUCCESSFULLY')
        self.up_entryNameMed.place_forget()
        self.up_labelNameMed.place_forget()
        self.up_butNameMed0.place_forget()
        self.up_butNameMed.place(x=100, y=230)

    def updatePriceMed(self):
        self.up_butPriceMed.place_forget()
        self.up_labelPriceMed = Label(self.Label_frame_up, text="ENTER NEW PRICE", font=("Arial", 20))
        self.up_labelPriceMed.place(x=100, y=330)
        self.up_entryPriceMed = Entry(self.Label_frame_up, font=("Arial", 20))
        self.up_entryPriceMed.place(x=400, y=330)
        self.up_butPriceMed0 = Button(self.Label_frame_up, text="UPDATE", font=("Algerian", 15),
                                    relief=RAISED,
                                    overrelief=SUNKEN, bg="#ff8080",command=self.update_price_med)
        self.up_butPriceMed0.place(x=800, y=330)
    def update_price_med(self):
        cur.execute(
            f"update medical_store set price= {self.up_entryPriceMed.get()} where id = {self.Entry_update_medid.get()} ")
        con.commit()
        messagebox.showinfo('hospital'.upper(), 'UPDATED SUCCESSFULLY')
        self.up_entryPriceMed.place_forget()
        self.up_labelPriceMed.place_forget()
        self.up_butPriceMed0.place_forget()
        self.up_butPriceMed.place(x=100, y=330)

    def updateAmountMed(self):
        self.up_butAmountMed.place_forget()
        self.up_labelAmountMed = Label(self.Label_frame_up, text="ENTER NEW AMOUNT", font=("Arial", 20))
        self.up_labelAmountMed.place(x=100, y=430)
        self.up_entryAmountMed = Entry(self.Label_frame_up, font=("Arial", 20))
        self.up_entryAmountMed.place(x=400, y=430)
        self.up_butAmountMed0 = Button(self.Label_frame_up, text="UPDATE", font=("Algerian", 15),
                                    relief=RAISED,
                                    overrelief=SUNKEN, bg="#ff8080",command=self.update_amount_med)
        self.up_butAmountMed0.place(x=800, y=430)
    def update_amount_med(self):
        cur.execute(
            f"update medical_store set amount= {self.up_entryAmountMed.get()} where id = {self.Entry_update_medid.get()} ")
        con.commit()
        messagebox.showinfo('hospital'.upper(), 'UPDATED SUCCESSFULLY')
        self.up_entryAmountMed.place_forget()
        self.up_labelAmountMed.place_forget()
        self.up_butAmountMed0.place_forget()
        self.up_butAmountMed.place(x=100, y=430)





ob = Start(root)
root.mainloop()


con.close()