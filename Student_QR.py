from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Code Generator |Devolped by Sukalyan")
        self.root.resizable(False,False)
        self.root.config(background="")
        self.root.config(background="white")

        heading=Label(self.root,text="QR CODE GENERATOR",font=(" Courier",35),bg="#7e3878",fg="White",anchor="w").place(x=0,y=0,relwidth=1)

        #******Student details window******
        # variable
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_depart = StringVar()
        self.var_college = StringVar()
        self.var_year = StringVar()

        student_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        student_Frame.place(x=50,y=100,height=350,width=450)
        student_tittle=Label(student_Frame,text="Student Details",font=("times new roman",20),bg="#9f00a7",fg="white").place(x=0,y=0,relwidth=1)


        student_id=Label(student_Frame,text="Student ID ",font=("times new roman",15),bg="white")
        student_id.place(x=20,y=60)
        student_name = Label(student_Frame, text="Name ", font=("times new roman", 15), bg="white").place(x=20, y=100)
        student_Depart = Label(student_Frame, text="Department ", font=("times new roman", 15), bg="white").place(x=20, y=140)
        student_college = Label(student_Frame, text="College ", font=("times new roman", 15), bg="white").place(x=20, y=180)
        student_year = Label(student_Frame, text="Year ", font=("times new roman", 15), bg="white").place(x=20, y=220)

        student_id = Entry(student_Frame, text="Student ID ",textvariable=self.var_id, font=("times new roman", 15), bg="#dcdde1").place(x=150,y=60)
        student_name = Entry(student_Frame, text="Name ",textvariable=self.var_name, font=("times new roman", 15), bg="#dcdde1").place(x=150, y=100)
        student_Depart = Entry(student_Frame, text="Department ", textvariable=self.var_depart,font=("times new roman", 15), bg="#dcdde1").place(x=150,y=140)
        student_college = Entry(student_Frame, text="College ",textvariable=self.var_college, font=("times new roman", 15), bg="#dcdde1").place(x=150,y=180)
        student_year = Entry(student_Frame, text="Year ",textvariable=self.var_year, font=("times new roman", 15), bg="#dcdde1").place(x=150, y=220)


        #******QR code window*******
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        qr_Frame.place(x=550, y=100, height=350, width=300)

        qr_tittle = Label(qr_Frame, text="QR Code", font=("times new roman", 20), bg="#9f00a7",fg="white").place(x=0, y=0, relwidth=1)

        self.qr_code=Label(qr_Frame,text="QR \n Unavailable !!!",font=("times new roman",15),bg="green",fg="black")
        self.qr_code.place(x=45,y=90,height=200,width=200)
        btn_generate=Button(student_Frame,text="Generate",font=("times new roman",14,'bold'),bg="green",fg="white",command=self.Generate).place(x=150,y=260,height=35,width=80)
        btn_clear = Button(student_Frame, text="clear", font=("times new roman", 14, 'bold'), bg="red", fg="white",command=self.clear).place(x=274, y=260, height=35, width=80)

        self.msg=''
        self.lable_msg=Label(student_Frame,text=self.msg,font=("times new roman",15,'bold'),bg="white",fg="green")
        self.lable_msg.place(x=128,y=305)

    def clear(self):
        self.var_id.set('')
        self.var_name.set('')
        self.var_depart.set('')
        self.var_college.set('')
        self.var_year.set('')

        self.msg = ''
        self.lable_msg.config(text=self.msg)



    def Generate(self):

        if self.var_id.get()=='' or self.var_name.get()=='' or self.var_depart.get()=='' or self.var_college.get()=='' or   self.var_year.get()=='':
         self.msg='All Fields are Required !!!'
         self.lable_msg.config(text=self.msg,fg='red')

        else:
            qr_data=(f"Student ID :{self.var_id.get()}\nName :{self.var_name.get()}\nDepartment :{self.var_depart.get()}\nCollege :{self.var_college.get()}\nYear :{self.var_year.get()}")
            qr=qrcode.make(qr_data)
            #For resize the image
            qr_code=resizeimage.resize_cover(qr,[180,180])
            #For saving the qr code picture in folder
            qr_code.save(("E:\ML\QR-Generator-Project\QR"+str(self.var_name.get()))+'.png')

            #To show the qr image using pillow module
            self.im=ImageTk.PhotoImage(file=("E:\ML\QR-Generator-Project\QR"+str(self.var_name.get()))+'.png')
            self.qr_code.config(image=self.im)



            #Notification update
            self.msg = 'QR Generated Successfully !!!'
            self.lable_msg.config(text=self.msg, fg='green')

root=Tk()
obj=Generator(root)
root.mainloop()