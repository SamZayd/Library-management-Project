from tkinter import Tk,Label,Entry,Button,Checkbutton,Radiobutton,IntVar,Menu,DISABLED,NORMAL,END,ttk,Canvas,Scrollbar
import tkinter.messagebox
from PIL import Image,ImageTk
import mysql.connector    


def registerpage():
    def regtomain(): 
        print("Registration Cancelled")
        reg.destroy()
        mainpage()
    
    def phonecheck():
        pno = str(epn.get())
        if len(pno) == 10:
            return pno
        else:
            tkinter.messagebox.showerror(title="Error !!!",message="Phone no. requires 10 digit")
            print("Error in phone. no")
            
    def gmf():
        if var.get() == 1:
            return "Male"
        elif var.get() == 2:
            return "Female"
        else:
            print("Error in gender selection");
    
    def reginsert():
        def insertomain():
            reg.destroy()
            mainpage()
            
        mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="sam", database="proj")  
          
        mycursor = mydb.cursor()
        name=IntVar()
        name=en.get()
        
        gen=gmf()  
        
        phone=IntVar()
        phone=phonecheck()
        
        email=IntVar()
        email=ee.get()
        
        password=IntVar()
        password=ep.get()
        
        if len(name)==0 or len(phone)==0 or len(email)==0 or len(password)==0:
            tkinter.messagebox.showerror(title="Input error",message="All fields are required")
        else:    
            mycursor.execute("insert into user(Name,Gender,Email,Phone,Password) values (%s,%s,%s,%s,%s)",(name,gen,email,phone,password))
            mydb.commit()
        
            
            print("Data saved Successfully")
            print("Name : " +name)
            print("Gender : "+gen)
            print("Phone no : "+phone)
            print("Email Id : "+email)
            print("Password : "+password)
        
            insertomain() 
            
                    
        
    #registerpage
    reg = Tk()
    
    reg.geometry("1366x768")
    reg.resizable(0,0)
    reg.configure(bg="#636188")
    load=Image.open('img/11.png')
    render=ImageTk.PhotoImage(load)
    img=Label(image=render)
    img.image=render
    img.place(x=0,y=0,relwidth=1, relheight=1)
    
    var=IntVar()
    
    reg.title("Registration Page")
    Label(reg,text="=",bg="#636188",fg="white",font="Wingdings 30 bold ").grid(row=0,column=4)
    Label(reg,text="Register Here",bg="#636188",fg="white",font="Consolas 30 bold").grid(row=0,column=5)
    
    
    Label(reg,text="Create New\nAccount",bg="#636188",fg="white", width=8,bd=11,font="Georgia 18 bold underline").grid()
    
    
    Label(reg,text="\n",bg="#636188").grid(row=1,column=2)
    
    Label(reg, text="Name :",bg="#636188",fg="white", width=10,font="Impact 15").grid(row=2,column=1)
    
    en = Entry(reg,font="Times 15",bg="#636188",fg="white",relief="solid")
    en.grid(row=2,column=2)
    
    
    
    Label(reg,text="\n",bg="#636188").grid(row=3,column=2)
    
    Label(reg, text=" Gender : ",bg="#636188",fg="white", width=10,font="Impact 15").grid(row=4,column=1)
    rgm = Radiobutton(reg, text=" Male ", variable=var, value=1, width=10,bg="#636188",font="Times 15")
    rgm.grid(row=4,column=2)
    
    rgf = Radiobutton(reg, text=" Female ", variable=var, value=2, width=10,bg="#636188",font="Times 15")
    rgf.grid(row=5,column=2)
    
    Label(reg,text="\n",bg="#636188").grid(row=6,column=2)
    
    Label(reg, text="Email ID :",bg="#636188",fg="white", width=10,font="Impact 15").grid(row=7,column=1)
    ee = Entry(reg,font="Times 15",bg="#636188",fg="white",relief="solid")
    ee.grid(row=7,column=2)
    
    Label(reg,text="\n",bg="#636188").grid(row=8,column=2)
    
    Label(reg, text="Phone No. :",bg="#636188",fg="white", width=10,font="Impact 15").grid(row=9,column=1)
    epn = Entry(reg,font="Times 15",bg="#636188",fg="white",relief="solid")
    epn.grid(row=9,column=2)
    
    Label(reg,text="\n",bg="#636188").grid(row=10,column=2)
    
    Label(reg, text="Password :",bg="#636188",fg="white", width=10,font="Impact 15").grid(row=11,column=1)
    ep = Entry(reg, show="*",font="Times 15",bg="#636188",fg="white",relief="solid")
    ep.grid(row=11,column=2)
    
    Label(reg,text="\n\n",bg="#636188").grid(row=12,column=2)
    
    bs = Button(reg,text="Submit",width=17,font="Impact 15",command=reginsert,bg="#636188",fg="white",relief="ridge", borderwidth=1)
    bs.grid(row=13,column=1)
    
    bc = Button(reg,text="Cancel",width=17,font="Impact 15",command=regtomain,bg="#636188",fg="white",relief="ridge", borderwidth=1)
    bc.grid(row=13,column=2)
    
    reg.mainloop()
       
def page1():
        
    def page1tolog():
        ap.destroy()
        print("Logged Out")
        loginpage()
                
    #page1
    ap=Tk()        
    ap.configure(bg="#7E7C7D")
    ap.resizable(0,0)
    ap.geometry("1366x768")
    
    global vframe
        
    vframe=ttk.Frame(ap)    
    
    def search():
        checkFrameExistance()
            
        vframe=ttk.Frame(ap)
        Label(vframe,text="Search\n",bg="#7E7C7D",fg="#CCD1D1", width=10,font="Consolas 30 bold").grid(row=0,column=6)
        
        vframe.pack()
        vframe.destroy()
        print("vframe "+str(vframe.winfo_exists()))
        
        
    def showbooks():
    
        sb =Tk()
        sb.configure(bg="#7E7C7D")
        sb.geometry("1350x754")
        container = ttk.Frame(sb)
        canvas = Canvas(container)
        scrollbar = Scrollbar(container, command=canvas.yview)
        s_frame = ttk.Frame(canvas)
        
        s_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(bg="#7E7C7D", scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0,0), window=s_frame,anchor="n")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="sam", database="proj")  
        
        mycursor = mydb.cursor()
        mycursor.execute("select * from books")
        data=mycursor.fetchall()
        
        Label(s_frame,text="B_Id ",bg="#7E7C7D",fg="#CCD1D1", width=4,font="Impact 14").grid(row=2,column=1)
        Label(s_frame,text="Book Name ",bg="#7E7C7D",fg="#CCD1D1", width=50,font="Impact 14").grid(row=2,column=2)
        Label(s_frame,text="Genre ",bg="#7E7C7D",fg="#CCD1D1", width=25,font="Impact 14").grid(row=2,column=4)
        Label(s_frame,text="Price ",bg="#7E7C7D",fg="#CCD1D1", width=5,font="Impact 14").grid(row=2,column=5)
        Label(s_frame,text="DOR ",bg="#7E7C7D",fg="#CCD1D1", width=12,font="Impact 14").grid(row=2,column=6)
        Label(s_frame,text="Author ",bg="#7E7C7D",fg="#CCD1D1", width=30,font="Impact 14").grid(row=2,column=7)
        Label(s_frame,text="Quantity ",bg="#7E7C7D",fg="#CCD1D1", width=9,font="Impact 14").grid(row=2,column=8)
        Label(s_frame,text=" ").grid(row=3)
        
        i = 4
        for row in data:
            Label(s_frame,text=str(row[0]),bg="#7E7C7D",fg="Black", width=3,font="12").grid(row=i,column=1)
            Label(s_frame,text=str(row[1]),bg="#7E7C7D",fg="Black", width=50,font="12").grid(row=i,column=2)
            Label(s_frame,text=str(row[2]),bg="#7E7C7D",fg="Black", width=25,font="12").grid(row=i,column=4)    
            Label(s_frame,text=str(row[3]),bg="#7E7C7D",fg="Black", width=5,font="12").grid(row=i,column=5)
            Label(s_frame,text=str(row[4]),bg="#7E7C7D",fg="Black", width=12,font="12").grid(row=i,column=6)
            Label(s_frame,text=str(row[5]),bg="#7E7C7D",fg="Black", width=30,font="12").grid(row=i,column=7)
            Label(s_frame,text=str(row[6]),bg="#7E7C7D",fg="Black", width=9,font="12").grid(row=i,column=8)    
            i+=1
            
        container.pack(fill="both", expand="y")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        sb.mainloop()
    
    def updateuser():
    
        def update():
            
            def phonecheck():
                pno = str(ep.get())
                if len(pno) == 10:
                    return pno
                else:
                    tkinter.messagebox.showerror(title="Error !!!",message="Phone no. requires 10 digit")
                    print("Error in phone. no")
                        
                
            mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="sam", database="proj")  
              
            mycursor = mydb.cursor()
            name=IntVar()
            name=en.get()
            
            phone=IntVar()
            phone=phonecheck()            
            
            email=IntVar()
            email=ee.get()
            
            address=IntVar()
            address=ea.get()
            
            dob=IntVar()
            dob=ed.get()
            
            aadhar=IntVar()
            aadhar=eaa.get()
            
            print("regno =",r)
            
    
            if len(name)==0 or len(phone)==0 or len(email)==0 or len(address)==0 or len(dob)==0 or len(aadhar)==0:
                tkinter.messagebox.showerror(title="Input error",message="All fields are required")
            else:    
                mycursor.execute("update proj.user set Name = %s,Email = %s,Phone = %s,address = %s,dob = %s,aadhar = %s where regno = %s ",(name,email,phone,address,dob,aadhar,r))
                mydb.commit()    
           
            tkinter.messagebox.showinfo(title="Updated ",message="Data updated successfully !!!")
            up.destroy() 
    
    
        up = Tk()  
    
        print("update")
        up.configure(bg="#7E7C7D")
        up.resizable(0,0)
        up.geometry("1366x768")
        mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="sam", database="proj")  
    
        mycursor = mydb.cursor()
        
        mycursor = mydb.cursor()
        mycursor.execute("select * from user where Name=%s and Password=%s",val)
        data=mycursor.fetchall()
        Label(up,text=" \t",width=12,bg="#7E7C7D").grid(column=0)
        Label(up,text="Profile\n",bg="#7E7C7D",fg="#CCD1D1", width=10,font="Consolas 30 bold").grid(row=0,column=6)
        Label(up,text="\n",width=12,bg="#7E7C7D").grid(row=4,column=0)
        Button(up,text="Update",width=17,font="Impact 15",command=update,bg="#636188",fg="white",relief="ridge", borderwidth=1).grid(row=5,column=6)
        
        for row in data:
            
            Label(up,text="Name :",bg="#7E7C7D",fg="#CCD1D1", width=17,font="Impact 12").grid(row=2,column=2)
            Label(up,text="Email :",bg="#7E7C7D",fg="#CCD1D1", width=27,font="Impact 12").grid(row=2,column=4)
            Label(up,text="Phone no. :",bg="#7E7C7D",fg="#CCD1D1", width=12,font="Impact 12").grid(row=2,column=5)
            Label(up,text="Address :",bg="#7E7C7D",fg="#CCD1D1", width=30,font="Impact 12").grid(row=2,column=6)
            Label(up,text="Date Of Birth :",bg="#7E7C7D",fg="#CCD1D1", width=18,font="Impact 12").grid(row=2,column=7)
            Label(up,text="Aadhar no.:",bg="#7E7C7D",fg="#CCD1D1", width=17,font="Impact 12").grid(row=2,column=8)
            
            r=row[0]
            Label(up,text=row[1],bg="#7E7C7D",fg="Black", width=17,font="Impact 12").grid(row=3,column=2)
            Label(up,text=row[3],bg="#7E7C7D",fg="Black", width=27,font="Impact 12").grid(row=3,column=4)    
            Label(up,text=row[4],bg="#7E7C7D",fg="Black", width=12,font="Impact 12").grid(row=3,column=5)
            Label(up,text=row[6],bg="#7E7C7D",fg="Black", width=30,font="Impact 12").grid(row=3,column=6)
            Label(up,text=row[7],bg="#7E7C7D",fg="Black", width=18,font="Impact 12").grid(row=3,column=7)
            Label(up,text=row[8],bg="#7E7C7D",fg="Black", width=17,font="Impact 12").grid(row=3 ,column=8)
     
        mycursor.execute("select * from user where Name=%s and Password=%s",val)
        data=mycursor.fetchall()
           
        en = Entry(up,font="Impact 12", width=15,bg="#636188",fg="white",relief="solid")
        en.grid(row=4,column=2)
        ee = Entry(up,font="Impact 12", width=25,bg="#636188",fg="white",relief="solid")
        ee.grid(row=4,column=4)
        ep = Entry(up,font="Impact 12", width=10,bg="#636188",fg="white",relief="solid")
        ep.grid(row=4,column=5)
        ea = Entry(up,font="Impact 12", width=30,bg="#636188",fg="white",relief="solid")
        ea.grid(row=4,column=6)
        ed = Entry(up,font="Impact 12", width=16,bg="#636188",fg="white",relief="solid")
        ed.grid(row=4,column=7)
        eaa = Entry(up,font="Impact 12", width=15,bg="#636188",fg="white",relief="solid")
        eaa.grid(row=4,column=8)
    
        
    
        up.mainloop()
    
    def checkFrameExistance():
        print("vframe exists"+str(vframe.winfo_exists() ))
        if (vframe.winfo_exists() == 1):
            print("vframe destroyed")
            vframe.pack_forget()
            vframe.destroy()
            #return
            
        
        print("doneeee")
    def viewprof():
        checkFrameExistance()
        
        vframe=ttk.Frame(ap)
    
        vframe.pack()
    
        mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="sam", database="proj")  
    
        mycursor = mydb.cursor()
    
        mycursor = mydb.cursor()
        mycursor.execute("select * from user where Name=%s and Password=%s",val)
        data=mycursor.fetchall()
        
        Label(vframe,text="Profile\n",bg="#7E7C7D",fg="#CCD1D1", width=10,font="Consolas 30 bold").grid(row=0,column=6)
        
        
        for row in data:
            
            #print("Id =",row[0])
            Label(vframe,text="RegNo :",bg="#7E7C7D",fg="#CCD1D1", width=6,font="Impact 12").grid(row=2,column=1)
            Label(vframe,text="Name :",bg="#7E7C7D",fg="#CCD1D1", width=15,font="Impact 12").grid(row=2,column=2)
            Label(vframe,text="Gender :",bg="#7E7C7D",fg="#CCD1D1", width=6,font="Impact 12").grid(row=2,column=3)
            Label(vframe,text="Email :",bg="#7E7C7D",fg="#CCD1D1", width=25,font="Impact 12").grid(row=2,column=4)
            Label(vframe,text="Phone no. :",bg="#7E7C7D",fg="#CCD1D1", width=10,font="Impact 12").grid(row=2,column=5)
            Label(vframe,text="Address :",bg="#7E7C7D",fg="#CCD1D1", width=30,font="Impact 12").grid(row=2,column=6)
            Label(vframe,text="Date Of Birth :",bg="#7E7C7D",fg="#CCD1D1", width=16,font="Impact 12").grid(row=2,column=7)
            Label(vframe,text="Aadhar no.:",bg="#7E7C7D",fg="#CCD1D1", width=15,font="Impact 12").grid(row=2,column=8)
            
    
            Label(vframe,text=row[0],bg="#7E7C7D",fg="Black", width=6,font="Impact 12").grid(row=3,column=1)
            Label(vframe,text=row[1],bg="#7E7C7D",fg="Black", width=15,font="Impact 12").grid(row=3,column=2)
            Label(vframe,text=row[2],bg="#7E7C7D",fg="Black", width=6,font="Impact 12").grid(row=3,column=3)
            Label(vframe,text=row[3],bg="#7E7C7D",fg="Black", width=25,font="Impact 12").grid(row=3,column=4)    
            Label(vframe,text=row[4],bg="#7E7C7D",fg="Black", width=10,font="Impact 12").grid(row=3,column=5)
            Label(vframe,text=row[6],bg="#7E7C7D",fg="Black", width=30,font="Impact 12").grid(row=3,column=6)
            Label(vframe,text=row[7],bg="#7E7C7D",fg="Black", width=16,font="Impact 12").grid(row=3,column=7)
            Label(vframe,text=row[8],bg="#7E7C7D",fg="Black", width=15,font="Impact 12").grid(row=3 ,column=8)
        print("vframe exists "+str(vframe.winfo_exists() ))
        vframe.pack()
    
            
            
        
        
    load=Image.open('img/8.png')
    render=ImageTk.PhotoImage(load)
    img=Label(image=render)
    img.image=render
    img.place(x=0,y=0,relwidth=1, relheight=1)
    
        
    ap.title("Library Management")
    menu=Menu(ap)
    ap.config(menu=menu)
    
    searchmenu=Menu(menu)
    search1=Menu(menu)
    
    servicesmenu=Menu(menu)
    borrowing=Menu(menu)
    
    researchmenu=Menu(menu)
    reshelp=Menu(menu)
    faculty=Menu(menu)
    
    hoursmenu=Menu(menu)
    local=Menu(menu)        
    
    accountmenu=Menu(menu)
    helpmenu=Menu(menu)
    
    menu.add_cascade(label="Search and Find",menu=searchmenu)
    searchmenu.add_command(label="Search",command=search)
    searchmenu.add_cascade(label="Resources",menu=search1)
    search1.add_command(label="Books",command=showbooks)
    searchmenu.add_command(label="Collection")
    searchmenu.add_command(label="Courses Reserve")
    searchmenu.add_command(label="New Items")
    searchmenu.add_command(label="Library Help")
    
    
    menu.add_cascade(label="Services",menu=servicesmenu)
    servicesmenu.add_cascade(label="Borrowing",menu=borrowing)
    borrowing.add_command(label="Borrowing from Library")
    servicesmenu.add_command(label="Loan")
    servicesmenu.add_command(label="Fines")
    servicesmenu.add_command(label="Off campus access")
    
    
    menu.add_cascade(label="Research Support",menu=researchmenu)
    researchmenu.add_cascade(label="Research Help",menu=reshelp)
    reshelp.add_command(label="Subject Guides")
    reshelp.add_command(label="Subject Area Help")
    researchmenu.add_cascade(label="Faculty",menu=faculty)
    faculty.add_command(label="Faculties Details")
    researchmenu.add_command(label="Open Access")
    researchmenu.add_command(label="Research Data Management")
     
    
    menu.add_cascade(label="Hours and Locations",menu=hoursmenu)
    hoursmenu.add_command(label="Working Hours")
    hoursmenu.add_cascade(label="Localization",menu=local)
    local.add_command(label="Maps And Direction")
    
    
    menu.add_cascade(label="About and Help",menu=helpmenu)
    helpmenu.add_command(label="( i ) about the Author")
    helpmenu.add_command(label="( i ) about the Library")
    helpmenu.add_separator()
    helpmenu.add_command(label="Policies")
    helpmenu.add_command(label="Find Us")
    
    
    menu.add_cascade(label="Account",menu=accountmenu)
    accountmenu.add_command(label="View Profile",command=viewprof)
    accountmenu.add_command(label="Edit Profile", command=updateuser)
    accountmenu.add_command(label="Logout",command=page1tolog)
    
    
    ap.mainloop()

def loginpage():
    
    def logtoreg():
        log.destroy()
        registerpage()
        
    def logincheck():
       
        name=lem.get()
        passw=lep.get()  
        
        mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="sam", database="proj")  
    
        mycursor = mydb.cursor()
    
        global val
        val=(name,passw)
    
        mycursor.execute("select * from user where Name=%s and Password=%s",val)
        
        data=mycursor.fetchone()
        if (len(name) == 0 or len(passw) == 0):
            tkinter.messagebox.showerror(title="Input Error", message="Enter Name and Password")
            print("Empty")
            
        elif data is not None:
            
            print("Logged In as "+str(name))
            log.destroy()
            page1()
            
        else:
            print("Invalid Name or Password")
            tkinter.messagebox.showwarning(title="Invalid Name or Password", message="Account not Found \n Create New Account")
    
    #loginpage
        
    log = Tk()
    log.geometry("1366x768")
    log.resizable(0,0)    
    log.configure(bg="#98A48C")
    
    load=Image.open('img/picb.jpg')
    render=ImageTk.PhotoImage(load)
    img=Label(image=render)
    img.image=render
    img.place(x=0,y=0,relwidth=1, relheight=1)
    
    log.title("Login Page")

    Label(log,text="=",bg="#98A48C",fg="white",font="Wingdings 30 bold ").grid(row=0,column=4)
    Label(log,text="Library Management ",bg="#98A48C",fg="white",font="Consolas 30 bold").grid(row=0,column=5)
    
    Label(log,text="Login\n",bg="#98A48C",fg="white", width=8,bd=11,font="Georgia 20 bold underline").grid()
    
    Label(log,text=" Name :",bg="#98A48C",fg="white", width=10,font="Impact 15").grid(row=2,column=2)
        
    lem = Entry(log,font="Times 15")
    lem.grid(row=2,column=3)
    lem.insert(0, "Username")
    lem.configure(state=DISABLED) 
    
    def on_click1(event):    
        lem.configure(state=NORMAL)
        lem.delete(0, END)
        
        lem.unbind('<Button-1>', on_click_name)
        
    on_click_name = lem.bind('<Button-1>', on_click1)
    
    Label(log,text="\n",bg="#98A48C").grid()
    Label(log,text="Password :",bg="#98A48C",fg="white", width=10,font="Impact 15").grid(row=4,column=2)
    
    lep = Entry(log, show="*sad",font="Times 15")
    lep.grid(row=4,column=3)
    
    Label(log,text="\n",bg="#98A48C").grid()
    
    Checkbutton(log,text=" Remember me",bg="#98A48C",font="Times 15").grid(row=6,column=3)
    
    Label(log,text="\n\n",bg="#98A48C").grid()
    
    bl = Button(log,text="Login",width=12,bg="#98A48C",fg="black", command=logincheck,font=("Times 15 bold") ,relief="ridge", borderwidth=1)
    bl.grid(row=8,column=2)
    
    
    br = Button(log,text="Sign Up",width=12,bg="#98A48C",fg="black",command=logtoreg,font="Times 15 bold" ,relief="ridge",borderwidth=1)
    br.grid(row=8,column=3)
    
    log.mainloop()



def mainpage():
    def maintolog():
        main.destroy()
        loginpage()
        
    def maintoreg():
        main.destroy()
        registerpage() 
    
    #mainpage
  
    main=Tk()
    main.geometry("1366x768")
    main.resizable(0,0)
    main.configure(bg="#C5C8DB")
        
    load=Image.open('img/2.png')
    render=ImageTk.PhotoImage(load)
    img=Label(image=render)
    img.image=render
    img.place(x=0,y=0,relwidth=1, relheight=1)
        
    main.title("Library Management ")
        
    Label(main,text="\n\nLibrary Management",bg="#C5C8DB",fg="#FB1C21",font="Consolas 35 bold").grid(column=1)
    
    Label(main,text="\n\n\n\n",bg="#C5C8DB",fg="#FB1C21",font="Consolas 35 bold").grid()
        
    Label(main,text="A Library Management System is a software built to handle the primary housekeeping functions of a library.\n Libraries rely on library management systems to manage asset collections as well\n as relationships with their members. Library management systems help libraries keep track of the books\n and their checkouts, as well as members subscriptions and profiles.\n",bg="#C5C8DB",fg="#3A577B",font="Georgia 12 bold").grid(row=2,column=1)
    
    Label(main,text="A new user, then click ",bg="#C5C8DB",fg="#3F4565",font="Consolas 19 bold").grid(column=1)
    
    breg = Button(main,text="Sign Up",width=12,command=maintoreg,bg="#C5C8DB",fg="#462838",bd=0,font="Consolas 20 bold underline") 
    breg.grid(column=1)   
    
    Label(main,text="Already an user, then Click ",bg="#C5C8DB",fg="#3F4565",font="Consolas 19 bold").grid(column=1)
    
    blogin = Button(main,text="Sign In",width=12,command=maintolog,bg="#C5C8DB",fg="#462838",bd=0,font="Consolas 20 bold underline") 
    blogin.grid(column=1)   
    
    main.mainloop()


def onetomain():
    one.destroy()
    mainpage()
    
one = Tk()
onetomain()
one.mainloop()