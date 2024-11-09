import tkinter as tk
from tkinter import messagebox
from tkinter import Message, Text
import cv2, os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from pymongo import MongoClient  # Import MongoDB client

# MongoDB connection
mongo_client = MongoClient("mongodb+srv://akshithshanagonda:MOMdad12@cluster0.tjewr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = mongo_client['attendance_db']  # Use your desired database name
attendance_collection = db['attendance_records']  # Use your desired collection name

recognizer = cv2.face.LBPHFaceRecognizer_create()
print("LBPHFaceRecognizer is available")

# Create a Tkinter window
window = tk.Tk()
window.title("PresencePro")
window.geometry('2688x1536')

# Create a custom style
style = ttk.Style()
style.configure("Curvy.TLabel", borderwidth=2, relief="groove")

# Adding Background Image
bg_image = Image.open("Girl.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Adding Images
def load_image(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# Load and place images
img_computer = load_image("Designer.png", 100, 100)
img_label = tk.Label(window, image=img_computer, bg="black")
img_label.place(x=1300, y=20)

img_computer2 = load_image("Student.png", 100, 100)
img_label2 = tk.Label(window, image=img_computer2, bg="#36454F", relief="sunken", borderwidth=10)
img_label2.place(x=50, y=25)

# Create the label with the custom style
message = tk.Label(
    window,
    text="PresencePro: Automated Attendance System",
    bg="#36454F",
    fg="#ffd700",
    width=50,
    height=2,
    font=("Comic Sans MS", 30, "bold"),
    relief="groove",
    borderwidth=10,
)

message.place(x=200, y=20)

# User input fields
lbl = tk.Label(window, text="Enter ID   :", width=20, height=1, fg="#ffd700", bg="#36454F", font=("Comic Sans MS", 15, " bold "), relief="groove", borderwidth=10)
lbl.place(x=400, y=200)

txt = tk.Entry(window, width=20, bg="#EEE8AA", fg="blue", font=("Comic Sans MS", 15, " bold "), relief="solid", borderwidth=5)
txt.place(x=700, y=205)

lbl2 = tk.Label(window, text="Enter Name :", width=20, fg="#ffd700", bg="#36454F", height=1, font=("Comic Sans MS", 15, " bold "), relief="groove", borderwidth=10)
lbl2.place(x=400, y=260)

txt2 = tk.Entry(window, width=20, bg="#EEE8AA", fg="blue", font=("Comic Sans MS", 15, " bold "), relief="solid", borderwidth=5)
txt2.place(x=700, y=265)

lbl5 = tk.Label(window, text="Enter Mail  :", width=20, fg="#ffd700", bg="#36454F", height=1, font=("Comic Sans MS", 15, " bold "), relief="groove", borderwidth=10)
lbl5.place(x=400, y=320)

txt3 = tk.Entry(window, width=20, bg="#EEE8AA", fg="blue", font=("Comic Sans MS", 15, " bold "), relief="solid", borderwidth=5)
txt3 .place(x=700, y=325)

# Function to insert attendance data into MongoDB
##   data_text = message2.cget("text")
    
    # Assume the text format is "Id: <ID> Name: <Name> Mail: <Mail>"
  #  try:
        # Split and parse the values from data_text
    #    data_parts = data_text.split()
    #    Id = data_parts[1]    # Assuming "Id:" is followed by ID
      #  name = data_parts[3]  # Assuming "Name:" is followed by Name
      #  mail = data_parts[5]  # Assuming "Mail:" is followed by Mail
        
        # Get current date and time
      #  date = datetime.datetime.now().strftime("%Y-%m-%d")
     #   time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Create the attendance record
       # attendance_data = {
       #     "Id": Id,
       #     "Name": name,
       #     "Mail": mail,
       #     "Date": date,
       #     "Time": time
       # }
        
        # Insert into MongoDB
       # attendance_collection.insert_one(attendance_data)
        
        # Update message box with success response
       # res = "Attendance recorded successfully!"
       # message.configure(text=res)
        
   # except IndexError:
        # Error handling in case the format is not as expected
       # message.configure(text="Error: Invalid format in message2")


# Function to insert attendance data into MongoDB
def insert_attendance():
    Id = txt.get()
    name = txt2.get()
    mail = txt3.get()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    attendance_data = {
        "Id": Id,
        "Name": name,
        "Mail": mail,
        "Date": date,
        "Time": time
    }

    attendance_collection.insert_one(attendance_data)

    res = "Attendance recorded successfully!"
    message.configure(text=res)
# Add a button to insert attendance data
insert_button = tk.Button(window, text="Insert Attendance", command=insert_attendance, fg="#000080", bg="#ffd700", width=20, height=3, activebackground="#ffd700", font=("Comic Sans MS", 15, " bold "), relief="groove", borderwidth=10)
insert_button.place(x=1200, y=650)


lbl3 = tk.Label(
    window,
    text="Notification:",
    width=20,
    fg="black",
    bg="#ffd700",
    height=2,
    font=("Comic Sans MS", 15, " bold "),relief="groove",
    borderwidth=10,
)
lbl3.place(x=400, y=400)

message = tk.Label(
    window,
    text="",
    bg="#36454F",
    fg="#ffd700",
    width=35,
    height=2,
    activebackground="black",
    font=("Comic Sans MS", 15, " bold "),relief="groove",
    borderwidth=10,
)
message.place(x=700, y=400)

lbl4 = tk.Label(
    window,
    text="Attendance:",
    width=20,
  fg="#000080",
    bg="#ffd700",
    height=2,
    font=("Comic Sans MS", 15, " bold "),relief="groove",
    borderwidth=10,
)
lbl4.place(x=400, y=670)

message2 = tk.Label(
    window,
    text="",
   fg="white",
   bg="#36454F",
   activeforeground="green",
   width=35,
  font=("Comic Sans MS", 15, " bold "),relief="groove",
  borderwidth=10,
)
message2.place(height=120, x=700, y=650)


def clear():
    txt.delete(0, "end")
    res = ""
    message.configure(text=res)


def clear2():
    txt2.delete(0, "end")
    res = ""
    message.configure(text=res)


def clear3():
    txt3.delete(0, "end")
    res = ""
    message.configure(text=res)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata

        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def TakeImages():
    Id = (txt.get())
    name = (txt2.get())
    mail = (txt3.get())
    if ((name.isalpha()) or (" " in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum += 1
                cv2.imwrite(
                    "TrainingImage/" + name + "." + Id + "." + str(sampleNum) + ".jpg",
                    gray[y : y + h, x : x + w],
                )
                cv2.imshow("frame", img)
            if cv2.waitKey(100) & 0xFF == ord("q"):
                break
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name, mail]
        with open("StudentDetails/StudentDetails.csv", "a+") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        message.configure(text=res)
    else:
        if is_number(Id):
            res = "Enter Alphabetical Name"
            message.configure(text=res)
        if name.isalpha():
            res = "Enter Numeric Id"
            message.configure(text=res)

def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel/Trainner.yml")
    res = "Image Trained"
    message.configure(text=res)


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert("L")
        imageNp = np.array(pilImage, "uint8")
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids
def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageLabel/Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails/StudentDetails.csv")
    print(df.columns)
    print(df)
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ["Id", "Name", "Date", "Time"]
    attendance = pd.DataFrame(columns=col_names)

    face_recognized = False  # Flag to check if a face is recognized

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])  # conf: confidence

            if conf < 50:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                face_recognized = True  # Set flag to true when a face is recognized
                break  # Exit the for loop if a face is recognized

            else:
                Id = ' '
                tt = str(Id)

            if conf > 75:
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown/Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])

            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)

        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)

        if face_recognized or (cv2.waitKey(1) == ord('q')):
            break  # Exit the while loop if a face is recognized or 'q' is pressed

    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
    Hour, Minute, Second = timeStamp.split(":")
    fileName = (
        "Attendance/Attendance_"
        + date
        + "_"
        + Hour
        + "-"
        + Minute
        + "-"
        + Second
        + ".csv"
    )
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    res = attendance
    message2.configure(text=res)


#5  6606  Akshith Shanagonda  akshithshanagonda@gmail.com         NaN    NaN

clearButton = tk.Button(
    window,
    text="Clear",
    command=clear,
    fg="#ffd700",
    bg="#36454F",
    width=20,
    height=1,
    activebackground="#ffd700",
    font=("Comic Sans MS", 10, " bold "),relief="raised",
    borderwidth=5,
)
clearButton.place(x=980, y=205)
clearButton2 = tk.Button(
    window,
    text="Clear",
    command=clear2,
    fg="#ffd700",
    bg="#36454F",
    width=20,
    height=1,
    activebackground="#ffd700",
    font=("Comic Sans MS", 10, " bold "),relief="raised",
    borderwidth=5,
)
clearButton2.place(x=980, y=265)
clearButton3 = tk.Button(
    window,
    text="Clear",
    command=clear3,
    fg="#ffd700",
    bg="#36454F",
    width=20,
    height=1,
    activebackground="#ffd700",
    font=("Comic Sans MS", 10, " bold "),relief="raised",
    borderwidth=5,
)
clearButton3.place(x=980, y=325)

takeImg = tk.Button(
    window,
    text="Scan Facial Features",
    command=TakeImages,
    fg="#000080",
    bg="#ffd700",
    width=20,
    height=3,
    activebackground="#ffd700",
    font=("Comic Sans MS", 15, " bold "),relief="groove",
    borderwidth=10,
)
takeImg.place(x=120, y=500)
trainImg = tk.Button(
    window,
    text="Train Images",
    command=TrainImages,
    fg="#000080",
    bg="#ffd700",
    width=20,
    height=3,
    activebackground="#ffd700",
    font=("Comic Sans MS", 15, " bold "),relief="groove",
    borderwidth=10,
)
trainImg.place(x=500, y=500)
trackImg = tk.Button(
    window,
    text="Take Attendance",
    command=TrackImages,
    fg="#000080",
    bg="#ffd700",
    width=20,
    height=3,
    activebackground="#ffd700",
    font=("Comic Sans MS", 15, " bold "),relief="groove",
    borderwidth=10,
)
trackImg.place(x=850, y=500)
quitWindow = tk.Button(
    window,
    text="Quit",
    command=window.quit,
    fg="#000080",
    bg="#ffd700",
    width=20,
    height=3,
    activebackground="#ffd700",
    font=("Comic Sans MS", 15, " bold "),relief="groove",
    borderwidth=10,
)
quitWindow.place(x=1200, y=500)



# Function to show attendance visualization
def show_attendance():
    # Load the CSV file into a DataFrame
    df = pd.read_csv(r'C:\Users\akshi\OneDrive\Desktop\(IOMP)\PresencePro\PresencePro\StudentDetails\StudentDetails.csv')  # Replace with your CSV file path

    # Ensure 'Date' column is in the correct datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')  # Specify the format as DD-MM-YYYY

    # Check for any parsing errors
    if df['Date'].isnull().any():
        print("Some dates could not be parsed. Please check the format:")
        print(df[df['Date'].isnull()])

    # Create a pivot table for attendance with names on the x-axis and dates on the y-axis
    attendance_data = df.pivot_table(index='Date', columns='Name', values='Id', aggfunc='count', fill_value=0)

    # Display the DataFrame for verification
    print("Attendance Data:")
    print(attendance_data)

    # Create a heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(attendance_data, cmap='YlGnBu', annot=True, fmt='d', cbar_kws={'label': 'Number of Days Present'})
    plt.title('Student Attendance Heatmap (Days Present)')
    plt.xlabel('Student Name')
    plt.ylabel('Date')
    plt.xticks(rotation=45)  # Rotate student name labels for better readability
    plt.tight_layout()  # Adjust layout to make room for the x-axis labels
    plt.show()


show_attendance_button = tk.Button(
    window,
    text="Show Attendance",
    command=show_attendance,
    fg="#000080",
    bg="#ffd700",
    width=20,
    height=3,
    activebackground="#ffd700",
    font=("Comic Sans MS", 15, " bold "),relief="groove",
    borderwidth=10,
)
show_attendance_button.place(x=120, y=650)


import tkinter as tk
from tkinter import messagebox
import os



def send_mail():
    MsgBox = tk.messagebox.askquestion(
        "Send Mail", "Do you want to send report via mail", icon="warning"
    )
    if MsgBox == "yes":
        tk.messagebox.showinfo("Send Mail", "Mail has been sent")
        os.system('"C:/Program Files/Python311/python.exe" automail1.py')
        res = "Email Sent Successfully!"
        message.configure(text=res)


# Add the Send Mail button
send_mail_button = tk.Button(
    window,
    text="Send Mail",
    command=send_mail,
    fg="#000080",
    bg="#ffd700",
    width=20,
    height=2,
    activebackground="#ffd700",
    font=("Comic Sans MS", 15, " bold "),relief="groove",
    borderwidth=10,
)
send_mail_button.place(x=1200, y=390)

window.mainloop()
