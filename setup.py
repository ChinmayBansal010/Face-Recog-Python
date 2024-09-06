import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:/Users/Chinmay Bansal/AppData/Local/Programs/Python/Python310/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = r"C:/Users/Chinmay Bansal/AppData/Local/Programs/Python/Python310/tcl/tk8.6"

executables = [cx_Freeze.Executable("Face_recognition_Attendance.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Attendance",
    options = {"build_exe": {"packages":["tkinter","os","cv2","mysql.connector","mysql","time","datetime","numpy","PIL","telethon"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll','images','data','database','attendance_report','haarcascade_frontalface_default.xml','readme.html']}},
    version = "1.1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Chinmay Bansal",
    executables = executables
    )
