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
from student import Studentgui
from train import Train
from face_recognisation import Face_recognisation
from attendance import Student_Attendance
import shutil

def main():
    root=Tk()
    obj = face_recognsation_system(root)
    root.mainloop()

class face_recognsation_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x696+0+0")
        self.root.title("Face recognisation system")
        self.root.wm_iconbitmap("face.ico")
        
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
        
        
        img_st = Image.open(r"images/student.png")
        img_st=img_st.resize((250,200),Image.Resampling.LANCZOS)
        self.photoimg_st = ImageTk.PhotoImage(img_st)
        
        b11 = Button(lbl_bg,image=self.photoimg_st,cursor="hand2",command = self.sstudent_details)
        b11.place(x=150,y=50,width = 250, height=200)
        
        b12 = Button(lbl_bg,text="Student Details",cursor="hand2",font = ("Roboto Mono",20,"bold"),bg = "black", fg="#16f50f",command = self.sstudent_details)
        b12.place(x=150,y=250,width = 250, height=35)
        
        
        img_df = Image.open(r"images/stface.jpeg")
        img_df=img_df.resize((250,200),Image.Resampling.LANCZOS)
        self.photoimg_df = ImageTk.PhotoImage(img_df)
        
        b21 = Button(lbl_bg,image=self.photoimg_df,cursor="hand2",command=self.face_recognisation)
        b21.place(x=550,y=50,width = 250, height=200)
        
        b22 = Button(lbl_bg,text="Detect Face",cursor="hand2",font = ("Roboto Mono",20,"bold"),bg = "black", fg="#16f50f",command=self.face_recognisation)
        b22.place(x=550,y=250,width = 250, height=35)
        
        img_sa = Image.open(r"images/attendance.png")
        img_sa=img_sa.resize((250,200),Image.Resampling.LANCZOS)
        self.photoimg_sa = ImageTk.PhotoImage(img_sa)
        
        b31 = Button(lbl_bg,image=self.photoimg_sa,cursor="hand2",command=self.attendance)
        b31.place(x=950,y=50,width = 250, height=200)
        
        b32 = Button(lbl_bg,text="Attendance",cursor="hand2",font = ("Roboto Mono",20,"bold"),bg = "black", fg="#16f50f",command=self.attendance)
        b32.place(x=950,y=250,width = 250, height=35)
        
        
        img_tr = Image.open(r"images/train.jpeg")
        img_tr=img_tr.resize((250,200),Image.Resampling.LANCZOS)
        self.photoimg_tr = ImageTk.PhotoImage(img_tr)
        
        b41 = Button(lbl_bg,image=self.photoimg_tr,cursor="hand2",command=self.train)
        b41.place(x=150,y=300,width = 250, height=200)
        
        b42 = Button(lbl_bg,text="Train data",cursor="hand2",font = ("Roboto Mono",20,"bold"),bg = "black", fg="#16f50f",command=self.train)
        b42.place(x=150,y=500,width = 250, height=35)
        
        
        img_ph = Image.open(r"images/photo.jpeg")
        img_ph=img_ph.resize((250,200),Image.Resampling.LANCZOS)
        self.photoimg_ph = ImageTk.PhotoImage(img_ph)
        
        b51 = Button(lbl_bg,image=self.photoimg_ph,cursor="hand2",command = self.open_img)
        b51.place(x=550,y=300,width = 250, height=200)
        
        b52 = Button(lbl_bg,text="Photos",cursor="hand2",command = self.open_img,font = ("Roboto Mono",20,"bold"),bg = "black", fg="#16f50f")
        b52.place(x=550,y=500,width = 250, height=35)
        
        
        img_ex = Image.open(r"images/exit.jpeg")
        img_ex=img_ex.resize((250,200),Image.Resampling.LANCZOS)
        self.photoimg_ex = ImageTk.PhotoImage(img_ex)
        
        b61 = Button(lbl_bg,image=self.photoimg_ex,cursor="hand2",command=self.iexit)
        b61.place(x=950,y=300,width = 250, height=200)
        
        b62 = Button(lbl_bg,text="Exit",cursor="hand2",font = ("Roboto Mono",20,"bold"),bg = "black", fg="#16f50f",command=self.iexit)
        b62.place(x=950,y=500,width = 250, height=35)

        samplebtn = Button(lbl_bg,text = "Download Sample Img" ,width = 250,font=("Roboto Mono",14,"bold"),bg="black",fg="gold",relief=RIDGE,bd=0,cursor="hand2",command=self.downloadsampleimg )
        samplebtn.place(x=1130,y=540,width = 250,height = 30)

    def downloadsampleimg(self):
        current_directory = os.getcwd()

        # Specify the relative path to the image file
        file_path = os.path.join(current_directory, "database", "sampledata", "sampleimg.jpg")

            # Prompt the user to choose a destination folder
        root = Tk()
        root.withdraw()
        destination_folder = filedialog.askdirectory()
        root.destroy()

        if destination_folder:
            # Get the filename from the file path
            filename = os.path.basename(file_path)

            # Construct the new file path with the destination folder
            new_file_path = os.path.join(destination_folder, filename)

            try:
                # Copy the image file to the destination folder
                shutil.copy(file_path, new_file_path)
                messagebox.showinfo("Success","Image copied successfully.",parent = self.root)
            except OSError as e:
                messagebox.showerror("Error",f"Error copying image: {e}",parent = self.root)
        else:
            messagebox.showerror("Error","No destination folder selected.",parent = self.root)


        
    
    def open_img(self):
        os.startfile("data")
        
    def sstudent_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Studentgui(self.new_window)
        
    def train(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_recognisation(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognisation(self.new_window)
        
    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Student_Attendance(self.new_window)
        
    def iexit(self):
        self.iexit=messagebox.askyesno("face Recognisation","Are you sure you want to exit",parent=self.root)
        if self.iexit >0:
            self.root.destroy()
        else:
            return
        
    
        
    
        
        
        
        


if __name__ == "__main__":
    main()
     