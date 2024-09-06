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
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import ast
import threading


class Face_recognisation:
    def __init__(self,root4):
        self.root4 = root4
        self.root4.geometry("1366x696+0+0")
        self.root4.title("Face recognisation system")
        self.root4.wm_iconbitmap("face.ico")
        
        lbl_title = Label(self.root4,text="FACE RECOGNITION",font = ("Roboto Mono",60,"bold"),bg = "black", fg="#16f50f")
        lbl_title.place(x=0,y=0,width=1366,height=70)
        
        img_top1 = Image.open(r"images/face_rocog.jpeg") 
        img_top1=img_top1.resize((640,626),Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        
        lbl_top1 = Label(self.root4,image=self.photoimg_top1)
        lbl_top1.place(x=0 , y=70 , width=640 , height =626)
        
        img_top2 = Image.open(r"images/face_recog.jpeg")
        img_top2=img_top2.resize((726,626),Image.Resampling.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
        
        lbl_top2 = Label(self.root4,image=self.photoimg_top2)
        lbl_top2.place(x=640 , y=70 , width=726 , height =626)
        
        b11 = Button(lbl_top2,text="FACE RECOGNISATION",font = ("Roboto Mono",15,"bold"),bg = "green", fg="white",cursor="hand2",command=self.face_recog)
        b11.place(x=236,y=490,width = 241, height=40)
    
    def send_message(self):

        try:
            api_id = '25887055'
            api_hash = 'e9410813c15dfff7705ae5ad3b1ed783'
            token = '6516251507:AAFsvvh3e1ScH6eGPwOZtg8Xaygxoie27UE'
            now=datetime.now()
            d1=now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            message = f"your child {n} enterted/exited the school at {dtString} on the date {d1}"

            phone = '+91'+phn


            client = TelegramClient('session', api_id, api_hash)

            client.connect()

            # if not client.is_user_authorized():
            #     client.send_code_request(phone)
            #     client.sign_in(phone, input('Enter the code: '))

            command = client.get_entity(phone)
            command = str(command)
            ids = command.find("id=") + 3
            ide = command.find(",", ids)
            ahvs = command.find("access_hash=") + 12
            ahve = command.find(",", ahvs)

            id_value = command[ids:ide]
            ahv = command[ahvs:ahve]

            id = int(id_value)
            ahv = int(ahv)

            try:
                
                receiver = InputPeerUser(id, ahv)
                
                client.send_message(receiver, message, parse_mode='html')

            except Exception as e:
                messagebox.showerror("Error : ",f"{es}",parent=self.root4)
            client.disconnect()

            # bot_token = '6516251507:AAFsvvh3e1ScH6eGPwOZtg8Xaygxoie27UE'
            # # Initialize the bot
            # bot = telebot.TeleBot(bot_token)

            # # Define the user or chat you want to send the message to
            # user_or_chat_id = 6113212496  # Replace with the user or chat ID

            # # The message you want to send
            # message = "Your message goes here."

            # # Send the message using the bot
            # bot.send_message(user_or_chat_id, message)

            # # Run the bot
            # bot.polling()
        
        except Exception as es:
            messagebox.showerror("Error: ",f"{es}",parent=self.root4)

    
    def mark_attendance(self,r,n,c,s):
        with open("attendance_report/attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            # if((r not in name_list) and (n not in name_list) and (c not in name_list) and (s not in name_list)):
            now=datetime.now()
            d1=now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            pd=" "
            if "08:00:00"<dtString<"09:00:00":
                pd = "Period 1"
            elif "09:00:00"<dtString<"10:00:00":
                pd = "Period 2"
            elif "10:00:00"<dtString<"11:00:00":
                pd = "Period 3"
            elif "11:00:00"<dtString<"12:00:00":
                pd = "Period 4"
            elif "12:00:00"<dtString<"13:00:00":
                pd = "Period 5"
            elif "13:00:00"<dtString<"14:00:00":
                pd = "Period 6"
            if pd == " ":
                pd = "No period"
                f.writelines(f"\n{r},{n},{c},{s},{dtString},{d1},{pd},Present")
            else:
                f.writelines(f"\n{r},{n},{c},{s},{dtString},{d1},{pd},Present")  
            
        
    def face_recog(self):
        
        

        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
        
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            
            global phn,n
            
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
            coord = []
            
            
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                
                confidence = int((100*(1-predict/300)))
                print(confidence)
                
                
                    
                    
                if confidence>78:

                    my_cursor = conn.cursor()
                
                
                    my_cursor.execute("select admno from student where admno="+str(id))
                    r = my_cursor.fetchone()
                    r="+".join(r)
                    
                    my_cursor.execute("select name from student where admno="+str(id))
                    n = my_cursor.fetchone()
                    n="+".join(n)
                        
                    my_cursor.execute("select class from student where admno="+str(id))
                    c = my_cursor.fetchone()
                    c="+".join(c)
                        
                    my_cursor.execute("select sec from student where admno="+str(id))
                    s = my_cursor.fetchone()
                    s="+".join(s)
                    
                    my_cursor.execute("select phno from student where admno="+str(id))
                    phn = my_cursor.fetchone()
                    phn="+".join(phn)
                    


                    cv2.putText(img,f"Admission no:{r}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,355),3)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,355),3)
                    cv2.putText(img,f"Class:{c}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,355),3)
                    cv2.putText(img,f"Section:{s}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,355),3)
                    self.mark_attendance(r,n,c,s)
                    
                    thread1 = threading.Thread(target=self.send_message())
                    thread1.start()
                    
                    thread1.join()
                    
                    
                    messagebox.showinfo("Done",f"Face recognised for,{n}")
                        
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,355),3)
                    
                coord=[x,y,w,h]
                
                
                    
            return coord
            
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
            
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
            
        video_cap=cv2.VideoCapture(0)
            
        while True:
            ret,img=video_cap.read()
            img = cv2.convertScaleAbs(img, alpha=1.6, beta=20)
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognisation",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        


if __name__ == "__main__":
    root4=Tk()
    obj = Face_recognisation(root4)
    root4.mainloop()