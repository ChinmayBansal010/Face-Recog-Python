from tkinter import*
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

mydata=[]

class Student_Attendance:
    def __init__(self,root5):
        self.root5 = root5
        self.root5.geometry("1366x696+0+0")
        self.root5.title("Face recognisation system")
        self.root5.wm_iconbitmap("face.ico")
        
        self.var_admno2 = StringVar()
        self.var_name2 = StringVar()
        self.var_class2 = StringVar()
        self.var_sec2 = StringVar()
        self.var_time2 = StringVar()
        self.var_date2 = StringVar()
        self.var_status2 = StringVar()
        self.var_period2 = StringVar()
        
        
        
        img_left = Image.open(r"images/student2.jpeg")
        img_left=img_left.resize((683,130),Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        lbl_left = Label(self.root5,image=self.photoimg_left)
        lbl_left.place(x=0 , y=0 , width=683 , height =130)
        
        img_right = Image.open(r"images/student3.jpeg")
        img_right=img_right.resize((683,130),Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        lbl_right = Label(self.root5,image=self.photoimg_right)
        lbl_right.place(x=683 , y=0 , width=683 , height =130)
        
        
        img_bg = Image.open(r"images/bg.jpeg")
        img_bg=img_bg.resize((1366,596),Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        
        lbl_bg = Label(self.root5,image=self.photoimg_bg)
        lbl_bg.place(x=0 , y=130 , width=1366 , height =596)
        
        lbl_title = Label(lbl_bg,text="ATTENDANCE MANAGEMENT",font = ("Roboto Mono",30,"bold"),bg = "black", fg="#16f50f")
        lbl_title.place(x=0,y=0,width=1366,height=40)


        main_frame = Frame(lbl_bg,bd=3,bg= "white")
        main_frame.place(x=5,y=40,width = 1346, height=520)
        
        left_frame = LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Attendance Details",font = ("Roboto Mono",20,"bold"),bg="white")
        left_frame.place(x=10,y=0,width=650,height=500)
        
        img_left2 = Image.open(r"images/atn1.jpeg")
        img_left2=img_left2.resize((635,100),Image.Resampling.LANCZOS)
        self.photoimg_left2 = ImageTk.PhotoImage(img_left2)
        
        lbl_left2 = Label(left_frame,image=self.photoimg_left2)
        lbl_left2.place(x=5 , y=0 , width=635 , height =100)
        
        detail_frame = Frame(left_frame,bd=2,bg="white")
        detail_frame.place(x=5,y=120,width = 630,height = 300)
        
        adm_label = Label(detail_frame,text="Admission No: ",font = ("Roboto Mono",12,"bold"),bg="white")
        adm_label.grid(row=0,column=0,sticky=W,pady=12)
        adm_entry = ttk.Entry(detail_frame,font = ("Roboto Mono",12,"bold"),textvariable=self.var_admno2)
        adm_entry.grid(row=0,column=1,sticky=W,pady=12)
        
        name_label = Label(detail_frame,text="Name: ",font = ("Roboto Mono",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,sticky=W,pady=12)
        name_entry = ttk.Entry(detail_frame,font = ("Roboto Mono",12,"bold"),textvariable=self.var_name2)
        name_entry.grid(row=0,column=3,sticky=W,pady=12)
        
        class_label = Label(detail_frame,text="CLASS: ",font = ("Roboto Mono",12,"bold"),bg="white")
        class_label.grid(row=1,column=0,sticky=W,pady=12)
        class_combo = ttk.Combobox(detail_frame,font = ("Roboto Mono",8,"bold"),state="readonly",textvariable=self.var_class2)
        class_combo["values"]=("Select Class:","1","2","3","4","5","6","7","8","9","12","11-Non-Medical","11-Medical","11-Commerce-Without-Maths","11-Commerce-With-Maths","11-Humanities-Without-Maths","11-Humanities-With-Maths","12-Non-Medical","12-Medical","12-Commerce-Without-Maths","12-Commerce-With-Maths","12-Humanities-Without-Maths","12-Humanities-With-Maths")
        class_combo.current(0)
        class_combo.grid(row=1,column=1,stick=W)
        
        section_label = Label(detail_frame,text="SECTION: ",font = ("Roboto Mono",12,"bold"),bg="white")
        section_label.grid(row=1,column=2,sticky=W,pady=12)
        section_combo = ttk.Combobox(detail_frame,font = ("Roboto Mono",8,"bold"),state="readonly",textvariable=self.var_sec2)
        section_combo["values"]=("Select Section:","A","B","C","D","E","F")
        section_combo.current(0)
        section_combo.grid(row=1,column=3,stick=W)
        
        
        Time_label = Label(detail_frame,text="Time: ",font = ("Roboto Mono",12,"bold"),bg="white")
        Time_label.grid(row=2,column=0,sticky=W,pady=12)
        Time_entry = ttk.Entry(detail_frame,font = ("Roboto Mono",12,"bold"),textvariable=self.var_time2)
        Time_entry.grid(row=2,column=1,sticky=W,pady=12)
        
        Date_label = Label(detail_frame,text="Date: ",font = ("Roboto Mono",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2,sticky=W,pady=12)
        Date_entry = ttk.Entry(detail_frame,font = ("Roboto Mono",12,"bold"),textvariable=self.var_date2)
        Date_entry.grid(row=2,column=3,sticky=W,pady=12)

        period2_label = Label(detail_frame,text="period2: ",font = ("Roboto Mono",12,"bold"),bg="white")
        period2_label.grid(row=3,column=0,sticky=W,pady=12)
        period2_entry = ttk.Entry(detail_frame,font = ("Roboto Mono",12,"bold"),textvariable=self.var_period2,state="readonly")
        period2_entry.grid(row=3,column=1,sticky=W,pady=12)
        
        atn_label = Label(detail_frame,text="Attendance Status:",font = ("Roboto Mono",12,"bold"),bg="white")
        atn_label.grid(row=3,column=2,sticky=W,pady=12)
        atn_combo = ttk.Combobox(detail_frame,font = ("Roboto Mono",8,"bold"),state="readonly",textvariable=self.var_status2)
        atn_combo["values"]=("Select Status:","Absent","Present")
        atn_combo.current(0)
        atn_combo.grid(row=3,column=3,stick=W)
        
        
        
        
        button_frame = Frame(left_frame,bd=2,bg="white")
        button_frame.place(x=10,y=350,width = 630,height = 100)
        
        button_row1 = Frame(button_frame,bd=2)
        button_row1.place(x=0,y=0,width=630,height=80)
        
        import_button = Button(button_row1,text="Import CSV",width=9,font = ("Roboto Mono",25,"bold"),bg="blue",fg="white",command=self.importCSV)
        import_button.grid(row=0,column=0,stick=W,padx=5)
        
        export_button = Button(button_row1,text="Export CSV",width=9,font = ("Roboto Mono",25,"bold"),bg="blue",fg="white",command=self.exportCSV)
        export_button.grid(row=0,column=1,stick=W,padx=5)
        
        # Update_button = Button(button_row1,text="Update",width=9,font = ("Roboto Mono",19,"bold"),bg="blue",fg="white")
        # Update_button.grid(row=0,column=2,stick=W,padx=5)
        
        Reset_button = Button(button_row1,text="Reset",width=9,font = ("Roboto Mono",25,"bold"),bg="blue",fg="white",command=self.reset_data)
        Reset_button.grid(row=0,column=3,stick=W,padx=5)
        
        
        
        
        
        
        right_frame = LabelFrame(main_frame,bd=5,relief=RIDGE,text="Attendance Details",font = ("Roboto Mono",20,"bold"),bg="white")
        right_frame.place(x=680,y=0,width=650,height=500)
        
        img_right2 = Image.open(r"images/atn2.jpeg")
        img_right2=img_right2.resize((630,100),Image.Resampling.LANCZOS)
        self.photoimg_right2 = ImageTk.PhotoImage(img_right2)
        
        lbl_right2 = Label(right_frame,image=self.photoimg_right2)
        lbl_right2.place(x=5 , y=0 , width=630 , height =100)
        
        table_frame = Frame(right_frame,bd=5,bg="white")
        table_frame.place(x=10,y=100,width=630,height=350)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column=("admno2","name2","class2","sec2","time2","date2","period2","status2"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("admno2",text="Admission Number")
        self.student_table.heading("name2",text="Name")
        self.student_table.heading("class2",text="Class")
        self.student_table.heading("sec2",text="Section")
        self.student_table.heading("time2",text="Time")
        self.student_table.heading("date2",text="Date")
        self.student_table.heading("period2",text="Period")
        self.student_table.heading("status2",text="Status")
        self.student_table["show"]="headings"
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
    
    def fetchData(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)
            
    
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent = self.root5)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root5)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent = self.root5)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
            
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root5)
                
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_admno2.set(data[0])
        self.var_name2.set(data[1])
        self.var_class2.set(data[2])
        self.var_sec2.set(data[3])
        self.var_time2.set(data[4])
        self.var_date2.set(data[5])
        self.var_period2.set(data[6])
        self.var_status2.set(data[7])
        
    def reset_data(self):
        self.var_admno2.set("")
        self.var_name2.set("")
        self.var_class2.set("Select Class:")
        self.var_sec2.set("Select Section:")
        self.var_time2.set("")
        self.var_date2.set("")
        self.var_period2.set("")
        self.var_status2.set("Attendance Status:")
            
        
        

if __name__ == "__main__":
    root5=Tk()
    obj = Student_Attendance(root5)
    root5.mainloop()