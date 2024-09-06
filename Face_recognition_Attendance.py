from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import cv2
import mysql.connector
from time import strftime
from datetime import datetime
import os
import csv
from tkinter import filedialog
import numpy as np
from main_admin import face_recognsation_system
# from main_student import student_portal
from face_recognisation import Face_recognisation
import sqlcredentials

def main():
    win=Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,main_root):
        self.main_root = main_root
        self.main_root.resizable(width=1,height=1)
        self.main_root.title("Face recognisation system")
        self.main_root.wm_iconbitmap("face.ico")
        
        self.bg = ImageTk.PhotoImage(file=r"images/bg.jpeg")        
        lbl_bg = Label(self.main_root,image=self.bg)
        lbl_bg.place(x=0 , y=0 , width=440 , height = 550)
        
        
        frame = Frame(self.main_root,bg="black",width = 440,height=550)
        frame.grid(row=0,column=0,sticky=E+W+N+S)
        
    
        
        
        img_1 = Image.open(r"images/usernameicon.png")
        img_1=img_1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)
        
        lbl_bg = Label(image=self.photoimg_1,bg="black",borderwidth=0)
        lbl_bg.place(x=170 , y=0 , width=100 , height =100)
        
        get_str = Label(frame,text="GET STARTED",font = ("Roboto Mono",25,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=110)
        
        username_lbl= Label(frame,text="Admission Number",font = ("Roboto Mono",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=80,y=180)
        
        self.txtuser = Entry(frame,font = ("Roboto Mono",15,"bold"))
        self.txtuser.place(x=60,y=210,width = 320,height=30)
        
        password_lbl= Label(frame,text="Password",font = ("Roboto Mono",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=80,y=280)
        
        self.txtpass = Entry(frame,font = ("Roboto Mono",15,"bold"),show="*")
        self.txtpass.place(x=60,y=310,width = 320,height=30)
        
        img_icon1 = Image.open(r"images/username.jpeg")
        img_icon1=img_icon1.resize((20,20),Image.Resampling.LANCZOS)
        self.photoimg_icon1 = ImageTk.PhotoImage(img_icon1)
        
        lbl_bg = Label(frame,image=self.photoimg_icon1,bg="black",borderwidth=0)
        lbl_bg.place(x=57 , y=187 , width=20 , height =20)
        
        img_icon2 = Image.open(r"images/lock.png")
        img_icon2=img_icon2.resize((20,20),Image.Resampling.LANCZOS)
        self.photoimg_icon2 = ImageTk.PhotoImage(img_icon2)
        
        lbl_bg = Label(frame,image=self.photoimg_icon2,bg="black",borderwidth=0)
        lbl_bg.place(x=57 , y=287 , width=20 , height =20)
        
        
        loginbtn = Button(frame,text="Login",font = ("Roboto Mono",25,"bold"),fg="white",bg="red",borderwidth=0,command=self.login)
        loginbtn.place(x=140,y=360,width=150)
        
        
        registerbtn = Button(frame,text="Register new user",command=self.register_window,font = ("Roboto Mono",10,"bold"),fg="white",bg="black",borderwidth=0,activeforeground="white",activebackground="black")
        registerbtn.place(x=40,y=450)
        
        frgtbtn = Button(frame,text="Forget Password",font = ("Roboto Mono",10,"bold"),fg="white",bg="black",borderwidth=0,activeforeground="white",activebackground="black",command=self.forgot_password_window)
        frgtbtn.place(x=40,y=480)
        
        
    
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required",parent=self.main_root)
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
            open_main=messagebox.askyesno("YesNo","Access only admin",parent=self.main_root)
            if open_main>0:
                self.new_window=Toplevel(self.main_root)
                self.app = face_recognsation_system(self.new_window)
                # self.main_root.destroy()
            else:
                if not open_main:
                    return
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student where admno=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()             
                                                                                    ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Admission Number or Password",parent=self.main_root)
            else:
                global id 
                id = self.txtuser.get()
                open_main=messagebox.askyesno("YesNo","Access as Student",parent=self.main_root)
                if open_main>0:
                    self.new_window=Toplevel(self.main_root)
                    self.app = student_portal(self.new_window)
                    # self.main_root.destroy()
                else:
                    if not open_main:
                        return
            
            conn.commit()
            conn.close()



            
    
    
            
            
    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter admission no. to reset password",parent=self.main_root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from student where admno=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please enter the valid admission no.",parent=self.main_root)
            else:
                conn.close()
                self.forgotroot = Toplevel()
                self.forgotroot.geometry("540x650+610+170")
                self.forgotroot.title("Forget Password")
                self.forgotroot.wm_iconbitmap("face.ico")
                
                l = Label(self.forgotroot,text="Forget Passsword",font = ("Roboto Mono",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                securityQ_label = Label(self.forgotroot,text="Security Question: ",font = ("Roboto Mono",17,"bold"),bg="white")
                securityQ_label.place(x=50,y=120)
                self.securityQ_combo = ttk.Combobox(self.forgotroot,font = ("Roboto Mono",17,"bold"),state="readonly",)
                self.securityQ_combo["values"]=("Select:","Birth Date(DD/MM/YYYY)","Your phone no.")
                self.securityQ_combo.current(0)
                self.securityQ_combo.place(x=50,y=160)
                
                answerA_label = Label(self.forgotroot,text="Security Answer: ",font = ("Roboto Mono",17,"bold"),bg="white")
                answerA_label.place(x=50,y=220)
                self.answerA_entry = ttk.Entry(self.forgotroot,font = ("Roboto Mono",17,"bold"),)
                self.answerA_entry.place(x=50,y=260)
                
                newpass_label = Label(self.forgotroot,text="New Password: ",font = ("Roboto Mono",17,"bold"),bg="white")
                newpass_label.place(x=50,y=320)
                self.newpass_entry = ttk.Entry(self.forgotroot,font = ("Roboto Mono",17,"bold"),)
                self.newpass_entry.place(x=50,y=360)
                
                btn = Button(self.forgotroot,text="Reset",font = ("Roboto Mono",30,"bold"),bg="green",fg="white",command=self.reset_pass)
                btn.place(x=180,y=440)
        
    def register_window(self):
        self.new_window = Toplevel(self.main_root)
        self.app = Register(self.new_window)
    def reset_pass(self):
        if self.securityQ_combo.get()=="Select:":
            messagebox.showerror("Error","Select the security question",parent=self.forgotroot)
            
        elif self.answerA_entry.get()=="":
            messagebox.showerror("Error","Enter the security answer",parent=self.forgotroot)
            
        elif self.newpass_entry.get()=="":
            messagebox.showerror("Error","Enter the new password",parent=self.forgotroot)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from student where admno=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.securityQ_combo.get(),self.answerA_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Invalid Answer",parent=self.forgotroot)
            else:
                query=("update student set password=%s where admno=%s")
                value = (self.newpass_entry.get(),self.txtuser.get(),)
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset , please login with new password",parent=self.forgotroot)
                self.forgotroot.destroy()



class Register:
    def __init__(self,register_root):
        self.register_root = register_root
        
        self.register_root.title("Face recognisation system")
        self.register_root.wm_iconbitmap("face.ico")
        
        
        self.var_name = StringVar()
        self.var_class = StringVar()
        self.var_sec = StringVar()
        self.var_admno = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()


        
        
        self.bg = ImageTk.PhotoImage(file=r"images/bg.jpeg")        
        lbl_bg = Label(self.register_root,image=self.bg)
        lbl_bg.place(x=0 , y=0 , width=1920 , height = 995)
        
        
        frame = Frame(self.register_root,bg="white",width = 1000,height=750)
        frame.grid(row=0,column=0)
        
        mainlbl = LabelFrame(frame,text="Register Here",borderwidth=0,font = ("Roboto Mono",30,"bold"),bg="white",fg="green")
        mainlbl.place(x=20,y=20,width=960,height=540)
        
        firstname_label = Label(mainlbl,text="First Name: ",font = ("Roboto Mono",17,"bold"),bg="white")
        firstname_label.place(x=50,y=20)
        firstname_entry = ttk.Entry(mainlbl,font = ("Roboto Mono",17,"bold"),textvariable=self.var_name)
        firstname_entry.place(x=50,y=60)
        
        adm_label = Label(mainlbl,text="Admission No. : ",font = ("Roboto Mono",17,"bold"),bg="white")
        adm_label.place(x=450,y=20)
        adm_entry = ttk.Entry(mainlbl,font = ("Roboto Mono",17,"bold"),textvariable=self.var_admno)
        adm_entry.place(x=450,y=60)
        
        class_label = Label(mainlbl,text="CLASS: ",font = ("Roboto Mono",14,"bold"),bg="white")
        class_label.place(x=50,y=120)
        class_combo = ttk.Combobox(mainlbl,font = ("Roboto Mono",14,"bold"),width=19,state="readonly",textvariable=self.var_class)
        class_combo["values"]=("Select Class:","1","2","3","4","5","6","7","8","9","10","11-Non-Medical","11-Medical","11-Commerce-Without-Maths","11-Commerce-With-Maths","11-Humanities-Without-Maths","11-Humanities-With-Maths","12-Non-Medical","12-Medical","12-Commerce-Without-Maths","12-Commerce-With-Maths","12-Humanities-Without-Maths","12-Humanities-With-Maths")
        class_combo.current(0)
        class_combo.place(x=50,y=160)
        
        section_label = Label(mainlbl,text="SECTION: ",font = ("Roboto Mono",14,"bold"),bg="white")
        section_label.place(x=450,y=120)
        section_combo = ttk.Combobox(mainlbl,font = ("Roboto Mono",14,"bold"),width=19,state="readonly",textvariable=self.var_sec)
        section_combo["values"]=("Select Section:","A","B","C","D","E","F")
        section_combo.current(0)
        section_combo.place(x=450,y=160)
        
        security_label = Label(mainlbl,text="Security Question: ",font = ("Roboto Mono",17,"bold"),bg="white")
        security_label.place(x=50,y=220)
        security_combo = ttk.Combobox(mainlbl,font = ("Roboto Mono",17,"bold"),state="readonly",textvariable=self.var_securityQ)
        security_combo["values"]=("Select:","Birth Date(DD/MM/YYYY)","Your phone no.")
        security_combo.current(0)
        security_combo.place(x=50,y=260)
        
        answer_label = Label(mainlbl,text="Security Answer: ",font = ("Roboto Mono",17,"bold"),bg="white")
        answer_label.place(x=450,y=220)
        answer_entry = ttk.Entry(mainlbl,font = ("Roboto Mono",17,"bold"),textvariable=self.var_securityA)
        answer_entry.place(x=450,y=260)
        
        passw_label = Label(mainlbl,text="Password: ",font = ("Roboto Mono",17,"bold"),bg="white")
        passw_label.place(x=50,y=320)
        passw_entry = ttk.Entry(mainlbl,font = ("Roboto Mono",17,"bold"),textvariable=self.var_password)
        passw_entry.place(x=50,y=360)
        
        confpassw_label = Label(mainlbl,text="Confirm Password: ",font = ("Roboto Mono",17,"bold"),bg="white")
        confpassw_label.place(x=450,y=320)
        confpassw_entry = ttk.Entry(mainlbl,font = ("Roboto Mono",17,"bold"),textvariable=self.var_confpass)
        confpassw_entry.place(x=450,y=360)
        
        termscond = Checkbutton(mainlbl,text="Agree to the terms and condition",font = ("Roboto Mono",17,"bold"),bg="white",onvalue=1,offvalue=0,variable=self.var_check)
        termscond.place(x=50,y=420)
        
        
        btnframe = Frame(frame,borderwidth=0,bg="white")
        btnframe.place(x=20,y=545,width=960,height=150)
        registerbtn = Button(btnframe,text="Resgister Now",font = ("Roboto Mono",30,"bold"),bg="red",fg="white",command=self.register_data)
        registerbtn.place(x=100,y=30)
        
        loginbtn = Button(btnframe,text="Login Now",font = ("Roboto Mono",30,"bold"),bg="dark blue",fg="white",command=self.login_now)
        loginbtn.place(x=600,y=30)
        
        
        
    def register_data(self):
        if self.var_name.get()=="" or self.var_class.get()=="" or self.var_admno.get()=="" or self.var_securityQ.get()=="Select:" or self.var_securityA.get()=="" or self.var_password.get()=="" or self.var_confpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.register_root)
            
        elif self.var_password.get() !=  self.var_confpass.get(): 
            messagebox.showerror("Error","Password and confirm password must be same",parent=self.register_root)
            
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to the terms and conditions",parent=self.register_root)
        else:
            conn=mysql.connector.connect(host=sqlcredentials.sqlhost,username=sqlcredentials.sqluser,password=sqlcredentials.sqlpassword,database=sqlcredentials.sqldatabse)
            my_cursor = conn.cursor()
            query = ("select * from student where admno=%s")
            value=(self.var_admno.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist , please try another admno",parent=self.register_root)
            else:
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_name.get(),
                                                                                        self.var_class.get(),
                                                                                        self.var_sec.get(),
                                                                                        self.var_admno.get(),
                                                                                        self.var_check.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_password.get(),
                                                                                        
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Successfully Registered",parent=self.register_root)
            
    def login_now(self):
        open_main=messagebox.askyesno("YesNo","Do you want to proceed to login page",parent=self.register_root)
        if open_main>0:
            self.register_root.destroy()

        else:
            if not open_main:
                return
    
    
def variables():
    conn=mysql.connector.connect(host=sqlcredentials.sqlhost,username=sqlcredentials.sqluser,password=sqlcredentials.sqlpassword,database=sqlcredentials.sqldatabse)
    my_cursor = conn.cursor()
                
                
    my_cursor.execute("select name from student where admno="+str(id))
    n = my_cursor.fetchone()
    n="".join((n))

    my_cursor.execute("select class from student where admno="+str(id))
    c = my_cursor.fetchone()
    c="".join((c))  

    my_cursor.execute("select sec from student where admno="+str(id))
    s = my_cursor.fetchone()
    s="".join((s))

    my_cursor.execute("select admno from student where admno="+str(id))
    adm = my_cursor.fetchone()
    adm="".join((adm))    

    my_cursor.execute("select securityQ from student where admno="+str(id))
    sq = my_cursor.fetchone()
    sq="".join((sq))  

    my_cursor.execute("select securityA from student where admno="+str(id))
    sa = my_cursor.fetchone()
    sa="".join((sa))

    my_cursor.execute("select password from student where admno="+str(id))
    p = my_cursor.fetchone()
    p="".join((p))
    
    my_cursor.execute("select phno from student where admno="+str(id))
    phn = my_cursor.fetchone()
    phn="".join((phn))    

    return n,c,s,adm,sq,sa,p,phn 
    

class student_portal:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x696+0+0")
        self.root.title("Face recognisation system")
        self.root.wm_iconbitmap("face.ico")

        self.var_name = StringVar()
        self.var_class = StringVar()
        self.var_sec = StringVar()
        self.var_admno = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_phoneno = StringVar()
        
        img_1 = Image.open(r"images/maintitle.png")
        img_1=img_1.resize((350,120),Image.Resampling.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)
        
        lbl_1 = Label(self.root,image=self.photoimg_1)
        lbl_1.place(x=0 , y=0 , width=350 , height =120)
        
        
        img_2 = Image.open(r"images/title2.jpeg")
        img_2=img_2.resize((200,120),Image.Resampling.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)
        
        lbl_2 = Label(self.root,image=self.photoimg_2)
        lbl_2.place(x=350 , y=0 , width=200 , height =120)
        
        
        img_3 = Image.open(r"images/title3.jpeg")
        img_3=img_3.resize((200,120),Image.Resampling.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)
        
        lbl_3 = Label(self.root,image=self.photoimg_3)
        lbl_3.place(x=550 , y=0 , width=200 , height =120)


        img_4 = Image.open(r"images/title 4.jpeg")
        img_4=img_4.resize((300,120),Image.Resampling.LANCZOS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)
        
        lbl_4 = Label(self.root,image=self.photoimg_4)
        lbl_4.place(x=750 , y=0 , width=300 , height =120)

        img_5 = Image.open(r"images/title.jpeg")
        img_5=img_5.resize((316,120),Image.Resampling.LANCZOS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)
        
        lbl_5 = Label(self.root,image=self.photoimg_5)
        lbl_5.place(x=1050 , y=0 , width=316 , height =120)
        
        img_6 = Image.open(r"images/title5.jpeg")
        img_6=img_6.resize((370,120),Image.Resampling.LANCZOS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)
        
        lbl_6 = Label(self.root,image=self.photoimg_6)
        lbl_6.place(x=1550 , y=0 , width=370 , height =120)
        
        img_bg = Image.open(r"images/bg.jpeg")
        img_bg=img_bg.resize((1366,666),Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        
        lbl_bg = Label(self.root,image=self.photoimg_bg)
        lbl_bg.place(x=0 , y=120 , width=1366 , height =696)
        
        lbl_title = Label(lbl_bg,text="FACE RECOGNISATION ATTENDANCE SYSTEM SOFTWARE",font = ("Roboto Mono",27,"bold"),bg = "black", fg="#16f50f")
        lbl_title.place(x=0,y=0,width=1366,height=35)
        
        
        def time():
            string= strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
            
        lbl = Label(lbl_title,font = ("Roboto Mono",15,"bold"),bg = "black", fg="#16f50f")
        lbl.place(x=0,y=0,width=120,height=35)
        time()

        img_df = Image.open(r"images/stface.jpeg")
        img_df=img_df.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_df = ImageTk.PhotoImage(img_df)
        
        b21 = Button(lbl_bg,image=self.photoimg_df,cursor="hand2",command=self.face_recognisation)
        b21.place(x=200,y=150,width = 200, height=200)
        
        b22 = Button(lbl_bg,text="Detect Face",cursor="hand2",font = ("Roboto Mono",20,"bold"),bg = "black", fg="#16f50f",command=self.face_recognisation)
        b22.place(x=200,y=350,width = 200, height=40)
        
        # img_ex = Image.open(r"images/exit.jpeg")
        # img_ex=img_ex.resize((400,400),Image.Resampling.LANCZOS)
        # self.photoimg_ex = ImageTk.PhotoImage(img_ex)
        
        # b61 = Button(lbl_bg,image=self.photoimg_ex,cursor="hand2",command=self.iexit)
        # b61.place(x=800,y=50,width = 400, height=400)
        
        # b62 = Button(lbl_bg,text="Exit",cursor="hand2",font = ("Roboto Mono",40,"bold"),bg = "white", fg="#16f50f",command=self.iexit)
        # b62.place(x=800,y=450,width = 400, height=90)
        # 

        detailbox = LabelFrame(lbl_bg,text="Student details",font = ("Roboto Mono",20,"bold"),bg = "white", fg="#16f50f")
        detailbox.place(x=800,y=50,width = 400, height=500)

        name_label = Label(detailbox,text="NAME: ",font = ("Roboto Mono",11,"bold"),bg="white")
        name_label.grid(row=0,column=0,sticky=W,pady=10,padx=5)
        name_entry = ttk.Entry(detailbox,font = ("Roboto Mono",11,"bold"),textvariable=self.var_name,state="readonly")
        name_entry.grid(row=0,column=1,sticky=W,pady=10,padx=5)
        
        class_label = Label(detailbox,text="CLASS: ",font = ("Roboto Mono",11,"bold"),bg="white")
        class_label.grid(row=1,column=0,sticky=W,pady=10,padx=5)
        class_combo = ttk.Entry(detailbox,font = ("Roboto Mono",11,"bold"),width=19,state="readonly",textvariable=self.var_class)
        class_combo.grid(row=1,column=1,stick=W,pady=10,padx=5)
        
        section_label = Label(detailbox,text="SECTION: ",font = ("Roboto Mono",11,"bold"),bg="white")
        section_label.grid(row=2,column=0,sticky=W,pady=10,padx=5)
        section_combo = ttk.Entry(detailbox,font = ("Roboto Mono",11,"bold"),width=19,state="readonly",textvariable=self.var_sec)
        section_combo.grid(row=2,column=1,stick=W,pady=10,padx=5)
        
        admno_label = Label(detailbox,text="Admission Number: ",font = ("Roboto Mono",11,"bold"),bg="white")
        admno_label.grid(row=3,column=0,sticky=W,pady=10,padx=5)
        admno_entry = ttk.Entry(detailbox,font = ("Roboto Mono",11,"bold"),textvariable=self.var_admno,state="readonly")
        admno_entry.grid(row=3,column=1,sticky=W,pady=10,padx=5)
        
        security_label = Label(detailbox,text="Security Question: ",font = ("Roboto Mono",11,"bold"),bg="white")
        security_label.grid(row=4,column=0,sticky=W,pady=10,padx=5)
        security_combo = ttk.Entry(detailbox,font = ("Roboto Mono",11,"bold"),state="readonly",textvariable=self.var_securityQ)
        security_combo.grid(row=4,column=1,sticky=W,pady=10,padx=5)
        
        answer_label = Label(detailbox,text="Security Answer: ",font = ("Roboto Mono",11,"bold"),bg="white")
        answer_label.grid(row=5,column=0,sticky=W,pady=10,padx=5)
        answer_entry = ttk.Entry(detailbox,font = ("Roboto Mono",11,"bold"),textvariable=self.var_securityA,state="readonly")
        answer_entry.grid(row=5,column=1,sticky=W,pady=10,padx=5)
        
        passw_label = Label(detailbox,text="Password: ",font = ("Roboto Mono",11,"bold"),bg="white")
        passw_label.grid(row=6,column=0,sticky=W,pady=10,padx=5)
        passw_entry = ttk.Entry(detailbox,font = ("Roboto Mono",11,"bold"),textvariable=self.var_password,state="readonly")
        passw_entry.grid(row=6,column=1,sticky=W,pady=10,padx=5)
        
        phno_label = Label(detailbox,text="Phone no.: ",font = ("Roboto Mono",11,"bold"),bg="white")
        phno_label.grid(row=7,column=0,sticky=W,pady=10,padx=5)
        phno_entry = ttk.Entry(detailbox,font = ("Roboto Mono",11,"bold"),textvariable=self.var_phoneno,state="readonly")
        phno_entry.grid(row=7,column=1,sticky=W,pady=10,padx=5)

        btnfetch = Button(detailbox,text="FETCH",font=("Roboto Mono",20,"bold"),bg="Black",fg="Gold",width=7,command=self.fetch_data)
        btnfetch.grid(row=8,column=1,sticky=W,pady=10,padx=5)

    def fetch_data(self):
        
        name,clas,sec,admno,secq,seca,password,phone = variables()

        self.var_admno.set(admno)
        self.var_name.set(name)
        self.var_class.set(clas)
        self.var_sec.set(sec)
        self.var_securityQ.set(secq)
        self.var_securityA.set(seca)
        self.var_password.set(password)
        self.var_phoneno.set(phone)

        messagebox.showinfo("Success","Succesfully details fetched",parent = self.root)



    def face_recognisation(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognisation(self.new_window)
        
    
        
    def iexit(self):
        self.iexit=messagebox.askyesno("Face Recognisation","Are you sure you want to exit",parent=self.root)
        if self.iexit >0:
            self.root.destroy()
        else:
            return


                        
        



class Forgotpass:
    def __init__(self,forget_root):
        self.forget_root = forget_root
        self.forget_root.geometry("1920x995+0+0")
        self.forget_root.title("Face recognisation system")       
        
        
        
if __name__ == "__main__":
    main()