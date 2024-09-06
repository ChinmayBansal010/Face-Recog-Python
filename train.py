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
import fnmatch


class Train:
    def __init__(self,root3):
        self.root3 = root3
        self.root3.geometry("1366x696+0+0")
        self.root3.title("Face recognisation system")
        self.root3.wm_iconbitmap("face.ico")
        
        
        lbl_title = Label(self.root3,text="TRAIN DATA SET",font = ("Roboto Mono",30,"bold"),bg = "black", fg="#16f50f")
        lbl_title.place(x=0,y=0,width=1366,height=60)
        
        img_top1 = Image.open(r"images/title.jpeg")
        img_top1=img_top1.resize((540,225),Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        
        lbl_top1 = Label(self.root3,image=self.photoimg_top1)
        lbl_top1.place(x=0 , y=60 , width=540 , height =225)
        
        img_top2 = Image.open(r"images/title2.jpeg")
        img_top2=img_top2.resize((440,225),Image.Resampling.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
        
        lbl_top2 = Label(self.root3,image=self.photoimg_top2)
        lbl_top2.place(x=540 , y=60 , width=440 , height =225)
        
        img_top3 = Image.open(r"images/title3.jpeg")
        img_top3=img_top3.resize((440,225),Image.Resampling.LANCZOS)
        self.photoimg_top3 = ImageTk.PhotoImage(img_top3)
        
        lbl_top3 = Label(self.root3,image=self.photoimg_top3)
        lbl_top3.place(x=940 , y=60 , width=440 , height =225)
        
        img_bg = Image.open(r"images/train.jpeg")
        img_bg=img_bg.resize((1366,510),Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        
        lbl_bg = Label(self.root3,image=self.photoimg_bg)
        lbl_bg.place(x=0 , y=355 , width=1366 , height =350)
        
        b11 = Button(self.root3,text="TRAIN DATA",font = ("Roboto Mono",50,"bold"),bg = "red", fg="white",cursor="hand2",command=self.train_classifier)
        b11.place(x=0,y=275,width = 1366, height=80)
        
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
        messagebox.showinfo("Result","Training datasets completed!!",parent = self.root3)






if __name__ == "__main__":
    root3=Tk()
    obj = Train(root3)
    root3.mainloop()