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
from tkinter import simpledialog
import numpy as np
import fnmatch
import sqlcredentials


class Studentgui:
    def __init__(self,root2):
        self.root2 = root2
        self.root2.geometry("1366x696+0+0")
        self.root2.title("Face recognisation system")
        self.root2.wm_iconbitmap("face.ico")
        
        
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
        
        lbl_1 = Label(self.root2,image=self.photoimg_1)
        lbl_1.place(x=0 , y=0 , width=350 , height =120)
        
        
        img_2 = Image.open(r"images/title2.jpeg")
        img_2=img_2.resize((200,120),Image.Resampling.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)
        
        lbl_2 = Label(self.root2,image=self.photoimg_2)
        lbl_2.place(x=350 , y=0 , width=200 , height =120)
        
        
        img_3 = Image.open(r"images/title3.jpeg")
        img_3=img_3.resize((200,120),Image.Resampling.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)
        
        lbl_3 = Label(self.root2,image=self.photoimg_3)
        lbl_3.place(x=550 , y=0 , width=200 , height =120)


        img_4 = Image.open(r"images/title 4.jpeg")
        img_4=img_4.resize((300,120),Image.Resampling.LANCZOS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)
        
        lbl_4 = Label(self.root2,image=self.photoimg_4)
        lbl_4.place(x=750 , y=0 , width=300 , height =120)

        img_5 = Image.open(r"images/title.jpeg")
        img_5=img_5.resize((316,120),Image.Resampling.LANCZOS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)
        
        lbl_5 = Label(self.root2,image=self.photoimg_5)
        lbl_5.place(x=1050 , y=0 , width=316 , height =120)
        
        img_6 = Image.open(r"images/title5.jpeg")
        img_6=img_6.resize((370,120),Image.Resampling.LANCZOS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)
        
        lbl_6 = Label(self.root2,image=self.photoimg_6)
        lbl_6.place(x=1550 , y=0 , width=370 , height =120)
        
        img_bg = Image.open(r"images/bg.jpeg")
        img_bg=img_bg.resize((1366,666),Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        
        lbl_bg = Label(self.root2,image=self.photoimg_bg)
        lbl_bg.place(x=0 , y=120 , width=1366 , height =696)
        
        lbl_title = Label(lbl_bg,text="STUDENT MANAGEMENT",font = ("Roboto Mono",27,"bold"),bg = "black", fg="#16f50f")
        lbl_title.place(x=0,y=0,width=1366,height=35)
        
        
        def time():
            string= strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
            
        lbl = Label(lbl_title,font = ("Roboto Mono",15,"bold"),bg = "black", fg="#16f50f")
        lbl.place(x=0,y=0,width=120,height=35)
        time()



        main_frame = Frame(lbl_bg,bd=3,bg= "white")
        main_frame.place(x=5,y=40,width = 1346, height=530)
        
        left_frame = LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font = ("Roboto Mono",20,"bold"),bg="white")
        left_frame.place(x=10,y=10,width=730,height=500)
        
        img_left = Image.open(r"images/student2.jpeg")
        img_left=img_left.resize((710,100),Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        lbl_left = Label(left_frame,image=self.photoimg_left)
        lbl_left.place(x=5 , y=0 , width=710 , height =100)
        
        detail_frame = Frame(left_frame,bd=2,bg="white")
        detail_frame.place(x=5,y=105,width = 710,height = 300)
        
        name_label = Label(detail_frame,text="NAME: ",font = ("Roboto Mono",11,"bold"),bg="white")
        name_label.grid(row=0,column=0,sticky=W,pady=10,padx=5)
        name_entry = ttk.Entry(detail_frame,font = ("Roboto Mono",11,"bold"),textvariable=self.var_name)
        name_entry.grid(row=0,column=1,sticky=W,pady=10,padx=5)
        
        class_label = Label(detail_frame,text="CLASS: ",font = ("Roboto Mono",11,"bold"),bg="white")
        class_label.grid(row=2,column=2,sticky=W,pady=10,padx=5)
        class_combo = ttk.Combobox(detail_frame,font = ("Roboto Mono",11,"bold"),width=19,state="readonly",textvariable=self.var_class)
        class_combo["values"]=("Select Class:","1","2","3","4","5","6","7","8","9","10","11-Non-Medical","11-Medical","11-Commerce-Without-Maths","11-Commerce-With-Maths","11-Humanities-Without-Maths","11-Humanities-With-Maths","12-Non-Medical","12-Medical","12-Commerce-Without-Maths","12-Commerce-With-Maths","12-Humanities-Without-Maths","12-Humanities-With-Maths")
        class_combo.current(0)
        class_combo.grid(row=2,column=3,stick=W,pady=10,padx=5)
        
        section_label = Label(detail_frame,text="SECTION: ",font = ("Roboto Mono",11,"bold"),bg="white")
        section_label.grid(row=2,column=0,sticky=W,pady=10,padx=5)
        section_combo = ttk.Combobox(detail_frame,font = ("Roboto Mono",11,"bold"),width=19,state="readonly",textvariable=self.var_sec)
        section_combo["values"]=("Select Section:","A","B","C","D","E","F")
        section_combo.current(0)
        section_combo.grid(row=2,column=1,stick=W,pady=10,padx=5)
        
        admno_label = Label(detail_frame,text="Admission Number: ",font = ("Roboto Mono",11,"bold"),bg="white")
        admno_label.grid(row=0,column=2,sticky=W,pady=10,padx=5)
        admno_entry = ttk.Entry(detail_frame,font = ("Roboto Mono",11,"bold"),textvariable=self.var_admno)
        admno_entry.grid(row=0,column=3,sticky=W,pady=10,padx=5)
        
        security_label = Label(detail_frame,text="Security Question: ",font = ("Roboto Mono",11,"bold"),bg="white")
        security_label.grid(row=3,column=0,sticky=W,pady=10,padx=5)
        security_combo = ttk.Combobox(detail_frame,font = ("Roboto Mono",11,"bold"),state="readonly",textvariable=self.var_securityQ)
        security_combo["values"]=("Select:","Birth Date(DD/MM/YYYY)","Your phone no.")
        security_combo.current(0)
        security_combo.grid(row=3,column=1,sticky=W,pady=10,padx=5)
        
        answer_label = Label(detail_frame,text="Security Answer: ",font = ("Roboto Mono",11,"bold"),bg="white")
        answer_label.grid(row=3,column=2,sticky=W,pady=10,padx=5)
        answer_entry = ttk.Entry(detail_frame,font = ("Roboto Mono",11,"bold"),textvariable=self.var_securityA)
        answer_entry.grid(row=3,column=3,sticky=W,pady=10,padx=5)
        
        passw_label = Label(detail_frame,text="Password: ",font = ("Roboto Mono",11,"bold"),bg="white")
        passw_label.grid(row=4,column=0,sticky=W,pady=10,padx=5)
        passw_entry = ttk.Entry(detail_frame,font = ("Roboto Mono",11,"bold"),textvariable=self.var_password)
        passw_entry.grid(row=4,column=1,sticky=W,pady=10,padx=5)
        
        phno_label = Label(detail_frame,text="Phone No.: ",font = ("Roboto Mono",11,"bold"),bg="white")
        phno_label.grid(row=4,column=2,sticky=W,pady=10,padx=5)
        phno_entry = ttk.Entry(detail_frame,font = ("Roboto Mono",11,"bold"),textvariable=self.var_phoneno)
        phno_entry.grid(row=4,column=3,sticky=W,pady=10,padx=5)
        
        self.var_radiobtn = StringVar()
        radiobtn1 = ttk.Radiobutton(detail_frame,text="Take Photo Sample",value="Y",variable=self.var_radiobtn)
        radiobtn1.grid(row=5,column=0,stick=W,pady=10,padx=5)

        radiobtn2 = ttk.Radiobutton(detail_frame,text="No Photo Sample",value="N",variable=self.var_radiobtn)
        radiobtn2.grid(row=5,column=1,stick=W,pady=17,padx=10)
        
        button_frame = Frame(left_frame,bd=2,bg="white")
        button_frame.place(x=5,y=320,width = 710,height = 130)
        
        button_row1 = Frame(button_frame,bd=2)
        button_row1.place(x=0,y=0,width=710,height=60)
        
        Submit_button = Button(button_row1,text="Submit",width=9,font = ("Roboto Mono",19,"bold"),bg="blue",fg="white",command=self.add_data)
        Submit_button.grid(row=0,column=0,stick=W,padx=5)
        
        Update_button = Button(button_row1,text="Update",width=10,font = ("Roboto Mono",20,"bold"),bg="blue",fg="white",command=self.update_data)
        Update_button.grid(row=0,column=1,stick=W,padx=5)
        
        Delete_button = Button(button_row1,text="Delete",width=9,font = ("Roboto Mono",20,"bold"),bg="blue",fg="white",command=self.delete_data)
        Delete_button.grid(row=0,column=2,stick=W,padx=5)
        
        Reset_button = Button(button_row1,text="Reset",width=9,font = ("Roboto Mono",19,"bold"),bg="blue",fg="white",command=self.reset_data)
        Reset_button.grid(row=0,column=3,stick=W,padx=5)
        
        button_row2 = Frame(button_frame,bd=2)
        button_row2.place(x=0,y=60,width=710,height=60)
        
        Takephotosample_button = Button(button_row2,text="Take Photo Sample",width=19,font = ("Roboto Mono",20,"bold"),bg="blue",fg="white",command=self.generate_dataset)
        Takephotosample_button.grid(row=0,column=0,stick=W,padx=5)
        
        UpdatePhotoSample_button = Button(button_row2,text="Update Photo Sample",width=20,font = ("Roboto Mono",20,"bold"),bg="blue",fg="white",command=self.generate_dataset)
        UpdatePhotoSample_button.grid(row=0,column=1,stick=W)
        
        
        
        right_frame = LabelFrame(main_frame,bd=5,relief=RIDGE,text="Class Student Details",font = ("Roboto Mono",20,"bold"),bg="white")
        right_frame.place(x=760,y=10,width=570,height=500)
        
        search_frame = LabelFrame()
        
        # img_right = Image.open(r"images/student3.jpeg")
        # img_right=img_right.resize((550,100),Image.Resampling.LANCZOS)
        # self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        # lbl_right = Label(right_frame,image=self.photoimg_right)
        # lbl_right.place(x=5 , y=0 , width=550 , height =100)
        
        search_frame = LabelFrame(right_frame,bd=5,relief=RIDGE,text="Search System",font = ("Roboto Mono",10,"bold"),bg="white")
        search_frame.place(x=10,y=0,width=550,height=100)
        
        Search_label = Label(search_frame,text="Search By: ",font = ("Roboto Mono",10,"bold"),bg="white")
        Search_label.grid(row=0,column=0,sticky=W,padx=10)
        
        self.var_search=StringVar()
        Search_combo = ttk.Combobox(search_frame,font = ("Roboto Mono",10,"bold"),width=20,state="readonly",textvariable=self.var_search)
        Search_combo["values"]=("Select By:","admno","name","class","phno")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,stick=W,padx=10)
        
        self.var_searchtext=StringVar()
        search_entry = ttk.Entry(search_frame,font = ("Roboto Mono",15,"bold"),textvariable=self.var_searchtext)
        search_entry.grid(row=0,column=2,sticky=W,padx=10)
        
        Search_button = Button(search_frame,text="Search",width=7,font = ("Roboto Mono",15,"bold"),bg="blue",fg="white",command=self.search)
        Search_button.grid(row=1,column=0,stick=W,padx=1,pady=5)
        
        Showall_button = Button(search_frame,text="Show All",width=7,font = ("Roboto Mono",15,"bold"),bg="blue",fg="white",command = self.fetch_data)
        Showall_button.grid(row=1,column=1,stick=W,padx=1,pady=5)

        Reset_button = Button(search_frame,text="Reset",width=7,font = ("Roboto Mono",15,"bold"),bg="blue",fg="white",command=self.reset_search)
        Reset_button.grid(row=1,column=2,stick=W,padx=1,pady=5)
        
        table_frame = Frame(right_frame,bd=5,bg="white")
        table_frame.place(x=10,y=110,width=550,height=350)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column=("name","class","sec","admno","photosample","securityQ","securityA","password","phno"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("name",text="Name")
        self.student_table.heading("class",text="Class")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("admno",text="Admission Number")
        self.student_table.heading("photosample",text="Photo Sample")
        self.student_table.heading("securityQ",text="Securty Q")
        self.student_table.heading("securityA",text="Securty A")
        self.student_table.heading("password",text="Password")
        self.student_table.heading("phno",text="Phone No.")
        
        self.student_table["show"]="headings"
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def showall(self):
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        
        
    
    def add_data(self):
        if self.var_name.get() == "" or self.var_class.get() == "Select Class:" or self.var_class.get() == "Select Section:" or self.var_admno.get() == "" or self.var_securityQ.get()=="Select:" or self.var_securityA.get()=="" or self.var_password.get()=="" or self.var_phoneno.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host=sqlcredentials.sqlhost,username=sqlcredentials.sqluser,password=sqlcredentials.sqlpassword,database=sqlcredentials.sqldatabse)
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_name.get(),
                                                                                self.var_class.get(),
                                                                                self.var_sec.get(),
                                                                                self.var_admno.get(),
                                                                                self.var_radiobtn.get(),
                                                                                self.var_securityQ.get(),
                                                                                self.var_securityA.get(),
                                                                                self.var_password.get(),
                                                                                self.var_phoneno.get()
                                                                                
                                                                            ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root2)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root2)
                
                
    def fetch_data(self):
        conn=mysql.connector.connect(host=sqlcredentials.sqlhost,username=sqlcredentials.sqluser,password=sqlcredentials.sqlpassword,database=sqlcredentials.sqldatabse)
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_name.set(data[0])
        self.var_class.set(data[1])
        self.var_sec.set(data[2])
        self.var_admno.set(data[3])
        self.var_radiobtn.set(data[4])
        self.var_securityQ.set(data[5])
        self.var_securityA.set(data[6])
        self.var_password.set(data[7])
        self.var_phoneno.set(data[8])
        
    def update_data(self):
        if self.var_name.get() == "" or self.var_class.get() == "Select Class:" or self.var_class.get() == "Select Section:" or self.var_admno.get() == ""or self.var_securityQ.get()=="Select:" or self.var_securityA.get()=="" or self.var_password.get()=="" or self.var_phoneno.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
            
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this data",parent = self.root2)
                if Update > 0:
                    conn=mysql.connector.connect(host=sqlcredentials.sqlhost,username=sqlcredentials.sqluser,password=sqlcredentials.sqlpassword,database=sqlcredentials.sqldatabse)
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set name=%s,class=%s,sec=%s,photosample=%s,securityQ=%s,securityA=%s,password=%s,phno=%s where admno=%s",(
                                                                                                                            self.var_name.get(),
                                                                                                                            self.var_class.get(),
                                                                                                                            self.var_sec.get(),
                                                                                                                            self.var_radiobtn.get(),
                                                                                                                            self.var_securityQ.get(),
                                                                                                                            self.var_securityA.get(),
                                                                                                                            self.var_password.get(),
                                                                                                                            self.var_phoneno.get(),
                                                                                                                            self.var_admno.get()      
                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student detail successfully updated",parent=self.root2)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root2)
                
    def delete_data(self):
        if self.var_admno.get()=="":
            messagebox.showerror("Error","Student admission number must be required",parent=self.root2)
        
        else:
            try:
                delete = messagebox.askyesno("Student delete page","Do you want to delete this student data",parent=self.root2)
                if delete>0:
                    conn=mysql.connector.connect(host=sqlcredentials.sqlhost,username=sqlcredentials.sqluser,password=sqlcredentials.sqlpassword,database=sqlcredentials.sqldatabse)
                    my_cursor = conn.cursor()
                    sql = "delete from student where admno=%s"
                    val = (self.var_admno.get(),)
                    my_cursor.execute(sql,val)
                    
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                directory = r'data'
                id = self.var_admno.get()

                if id:
                    # File extension or wildcard pattern
                    file_pattern = f'user.{id}.*.jpeg'


                    image_files = []


                    for file in os.listdir(directory):
                        if fnmatch.fnmatch(file, file_pattern):
                            image_files.append(file)
                    
                    if len(image_files)==0:
                        messagebox.showerror("NOt FOUND","Images not found plase check the ref no and images folder")


                    else:
                        for file in image_files:
                            file_path = os.path.join(directory, file)
                            os.remove(file_path)   
                messagebox.showinfo("Success","Student detail successfully deleted",parent=self.root2)
                self.train_classifier()
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root2)
                
    def train_classifier(self):
        file_pattern = f'classifier.xml'
        directory=r'./'
        image_files=[]
        for file in os.listdir(directory):
                        if fnmatch.fnmatch(file, file_pattern):
                            image_files.append(file)
                    
        if len(image_files)==0:
                a=1
        else:
            file_path = os.path.join(directory,file_pattern)
            os.remove(file_path)
        
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!",parent = self.root2)
    
    def reset_data(self):
        self.var_name.set("")
        self.var_class.set("Select Class:")
        self.var_sec.set("Select Section:")
        self.var_admno.set("")
        self.var_radiobtn.set("")
        self.var_securityQ.set("Select:") 
        self.var_securityA.set("") 
        self.var_password.set("")
        self.var_phoneno.set("")
        


    def generate_dataset(self):
        id = simpledialog.askstring("Enter Admission Number", "Please enter the admission number again:")
        if self.var_name.get() == "" or self.var_class.get() == "Select Class:" or self.var_class.get() == "Select Section:" or self.var_admno.get() == "" or self.var_phoneno.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host=sqlcredentials.sqlhost,username=sqlcredentials.sqluser,password=sqlcredentials.sqlpassword,database=sqlcredentials.sqldatabse)
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()

                my_cursor.execute("update student set name=%s,class=%s,sec=%s,photosample=%s,securityQ=%s,securityA=%s,password=%s,phno=%s where admno=%s",(
                                                                                                            self.var_name.get(),
                                                                                                            self.var_class.get(),
                                                                                                            self.var_sec.get(),
                                                                                                            self.var_radiobtn.get(),
                                                                                                            self.var_securityQ.get(),
                                                                                                            self.var_securityA.get(),
                                                                                                            self.var_password.get(),
                                                                                                            self.var_phoneno.get(),
                                                                                                            self.var_admno.get()     
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                angle = 0  

                while True:
                    ret, my_frame = cap.read()

            
                    rows, cols, _ = my_frame.shape
                    rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
                    rotated_frame = cv2.warpAffine(my_frame, rotation_matrix, (cols, rows))

                    if face_cropped(rotated_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(rotated_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpeg"
                        cv2.imwrite(file_name_path, face)
                        # cv2.putText(face, str(img_id), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 200:
                        break

                    angle += 10 

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generation data set completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root2)
    
    def reset_search(self):
        self.var_search.set("")
        self.var_searchtext.set("")

    def search(self):
        conn=mysql.connector.connect(host=sqlcredentials.sqlhost,username=sqlcredentials.sqluser,password=sqlcredentials.sqlpassword,database=sqlcredentials.sqldatabse)
        my_cursor = conn.cursor()

        my_cursor.execute("select * from student where "+str(self.var_search.get())+" like '%"+str(self.var_searchtext.get())+"%'")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root2=Tk()
    obj = Studentgui(root2)
    root2.mainloop()
        