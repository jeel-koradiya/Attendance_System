from tkinter import *
import sqlite3 as db
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import datetime
from tkinter import ttk

main = Tk()
main.geometry("400x400")
main.title("GVM ATTENDANCE")
main.wm_iconbitmap("1.ico")
c_width="400"
c_height="400"
c_widget = Canvas(main, width=c_width, height=c_height)
c_widget.pack()
c_widget.create_rectangle(0, 0, 800, 100, fill="#A71B05", outline="#A71B05")
c_widget.create_rectangle(0, 100, 800, 80, fill="#DF1E0E", outline="#DF1E0E")

use = Label(main, text="Username:",width=20,font=("bold", 10))
use.place(x=20,y=130)

e1 = Entry(main)
e1.place(x=180,y=130)

pas = Label(main, text="Password:",width=20,font=("bold", 10))
pas.place(x=20,y=180)

e2 = Entry(main)
e2.place(x=180,y=180)




def reg():
    main.destroy()
    root123 = Tk()
    root123.title("Registration")
    root123.wm_iconbitmap("1.ico")
    c_width="500"
    c_height="700"
    c_widget = Canvas(root123, width=c_width, height=c_height)
    c_widget.pack()
    c_widget.create_rectangle(0, 0, 800, 100, fill="#A71B05", outline="#A71B05")
    c_widget.create_rectangle(0, 100, 800, 80, fill="#DF1E0E", outline="#DF1E0E")
   
    conn = db.connect('sample.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS login
        (
            name TEXT,
            email TEXT,
            gender TEXT,
            birth TEXT,
            phone TEXT,
            address TEXT,
            user TEXT,
            passwd TEXT
            )''')
    cur.close()
    conn.commit()
    conn.close()

    def put():
        if len(name.get()) == 0:
            messagebox.showwarning("warning","Please Enter Name.")
        
        elif (name.get().isdigit()):
            messagebox.showwarning("warning","Please Enter Proper Name.")
        elif len(email.get()) == 0:
            messagebox.showwarning("warning","Please Enter Email.")
        elif (email.get().isdigit()):
            messagebox.showwarning("warning","Please Enter Proper Email Address.")
        elif len(var.get()) == 0:
            messagebox.showwarning("warning","Please Select Radio Button.")    
        elif len(birth.get()) == 0:
            messagebox.showwarning("warning","Please Enter BirthDate.")
        elif (birth.get().isidentifier()):
            messagebox.showwarning("warning","Please Enter Proper Birthdate")
        elif len(phone.get()) == 0:
            messagebox.showwarning("warning","Please Enter PhoneNo.")
        elif (phone.get().isidentifier()):
            messagebox.showwarning("warning","Please Enter Proper PhoneNo")
        elif len(address.get()) == 0:
            messagebox.showwarning("warning","Please Enter Address.")
        elif len(user.get()) == 0:
            messagebox.showwarning("warning","Please Enter UserName.")
        elif len(passwd.get()) == 0:
            messagebox.showwarning("warning","Please Enter Password.")
        else:
            conn = db.connect('sample.db')
            cur = conn.cursor()
            cur.execute("insert into login values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(name.get(), email.get(), var.get(), birth.get(), phone.get(), address.get(), user.get(), passwd.get()))
            messagebox.showinfo("Information","Submit Data...")
            cur.close()
            conn.commit()
            conn.close()
            clear()


    name = StringVar()
    email = StringVar()
    var = StringVar()
    var.set("Male")
    birth = StringVar()
    phone = StringVar()
    address = StringVar()
    user = StringVar()
    passwd = StringVar()

    label_1 = Label(root123, text="Name", width=20, font=("bold", 10))
    label_1.place(x=70, y=200)
    name_entry = Entry(root123, textvar=name)
    name_entry.place(x=240, y=200)

    label_2 = Label(root123, text="Email", width=20, font=("bold", 10))
    label_2.place(x=70, y=250)
    email_entry = Entry(root123, textvar=email)
    email_entry.place(x=240, y=250)

    label_3 = Label(root123, text="Gender", width=20, font=("bold", 10))
    label_3.place(x=70, y=300)
    radio1=Radiobutton(root123, text="Male", padx=5, variable=var, value=1)
    radio1.place(x=235, y=300)
    radio2=Radiobutton(root123, text="Female", padx=20, variable=var, value=0)
    radio2.place(x=290, y=300)

    label_4 = Label(root123, text="BirthDate", width=20, font=("bold", 10))
    label_4.place(x=70, y=350)
    label_44 = Label(root123, text="dd-mm-yyyy", width=20, font=("bold", 10))
    label_44.place(x=325, y=350)
    birth_entry = Entry(root123, textvar=birth)
    birth_entry.place(x=240, y=350)

    label_5 = Label(root123, text="PhoneNumber", width=20, font=("bold", 10))
    label_5.place(x=70, y=400)
    phone_entry = Entry(root123, textvar=phone)
    phone_entry.place(x=240, y=400)

    label_6 = Label(root123, text="Address", width=20, font=("bold", 10))
    label_6.place(x=70, y=450)
    address_entry = Entry(root123, textvar=address)
    address_entry.place(x=240, y=450)

    label_7 = Label(root123, text="UserName", width=20, font=("bold", 10))
    label_7.place(x=70, y=500)
    user_entry = Entry(root123, textvar=user)
    user_entry.place(x=240, y=500)

    label_8 = Label(root123, text="Password", width=20, font=("bold", 10))
    label_8.place(x=70, y=550)
    password_entry = Entry(root123, textvar=passwd)
    password_entry.place(x=240, y=550)

    Button(root123, text='Submit', width=20, bg='brown',height=2,fg='white',command=put).place(x=180, y=650)
  


    
    def clear():
            name_entry.delete(0, END)
            email_entry.delete(0, END)
            birth_entry.delete(0, END)
            phone_entry.delete(0, END)
            address_entry.delete(0, END)
            user_entry.delete(0, END)
            password_entry.delete(0, END)
            
    root123.mainloop()

def login():
    if len(e1.get()) == 0:
                messagebox.showwarning("warning","Please Enter Proper UserName.")
    elif len(e2.get()) == 0:
                messagebox.showwarning("warning","Please Enter Proper Password.")
    else:
        user=e1.get()
        passwd=e2.get()
    
        con=db.connect('sample.db')
        cor=con.cursor()

        cor.execute('SELECT * FROM login WHERE user="%s" AND passwd="%s"'%(user,passwd))
        if cor.fetchone() is not None:
            main.destroy()
            root = Tk()
            root.geometry("400x400")
            root.title("GVM ATTENDANCE")
            root.wm_iconbitmap("1.ico")


        #check by name first window

            def click1():
                Button(root, text='Check By Name', width=20, bg='brown',height=2,fg='white',command=new).place(x=30, y=320)
                Button(root, text='Check By Date', width=20, bg='brown',height=2,fg='white',command=new1).place(x=180, y=320)
  

        #new window khulse


        def new():
            root.destroy()
            root1 = Tk()
            root1.geometry("630x700")
            root1.title("Check Attendance")
            root1.wm_iconbitmap("1.ico")
            
            c_width="630"
            c_height="800"
            c_widget = Canvas(root1, width=c_width, height=c_height)
            c_widget.pack()
            c_widget.create_rectangle(0, 0, 800, 100, fill="#A71B05", outline="#A71B05")
            c_widget.create_rectangle(0, 100, 800, 80, fill="#DF1E0E", outline="#DF1E0E")
            
            dell = StringVar()
            label_1 = Label(root1, text="Name", width=20, font=("bold", 10))
            label_1.place(x=0, y=130)
            e1 = Entry(root1, textvar=dell)
            e1.place(x=120, y=130)
                      
            def ch_at():
                if len(dell.get()) == 0:
                    messagebox.showwarning("warning","Please Enter Name.")
                elif (dell.get().isdigit()):  
                    messagebox.showwarning("warning","Please Enter Proper Name.")
                else:
                    #tex.delete("1.0",END)
                    name=e1.get()
                    li=[]
                    conn = db.connect('sample.db')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM DATA WHERE name='%s'"%(name))

                    tv = ttk.Treeview(root1, columns=(1,2,3),show="headings", height="22")
                    tv.place(x=5,y=200)
                    tv.heading(1, text="Name")
                    tv.heading(2, text="Date")
                    tv.heading(3, text="Attendance")

                    tvScrollbar=ttk.Scrollbar(root1,orient="vertical",command=tv.yview)
                    tv.config(yscroll=tvScrollbar.set)
                    tvScrollbar.place(x=610,y=200,height=470)
  
                    #scrollbar.config(command=tv.yview)
            
                    for i in cur:
                        tv.insert('', 'end', values=i)
                        #li.append("\n")
                        #li.append(i)

                    #tex.insert(END,li) 
                    conn.commit()
                    cur.close()
                    conn.close()
                
                
                
            Button(root1, text='check', width=20, bg='brown',fg='white',command=ch_at).place(x=250, y=130)


        def new1():
            root.destroy()
            root1 = Tk()
            root1.geometry("630x700")
            root1.title("Check Attendance")
            root1.wm_iconbitmap("1.ico")

            c_width="630"
            c_height="800"
            c_widget = Canvas(root1, width=c_width, height=c_height)
            c_widget.pack()
            c_widget.create_rectangle(0, 0, 800, 100, fill="#A71B05", outline="#A71B05")
            c_widget.create_rectangle(0, 100, 800, 80, fill="#DF1E0E", outline="#DF1E0E")
            
            dell = StringVar()
            label_1 = Label(root1, text="Date", width=20, font=("bold", 10))
            label_1.place(x=0, y=130)
            label_3 = Label(root1, text="dd-mm-yyyy", width=20, font=("bold", 10))
            label_3.place(x=205, y=130)
            e1= Entry(root1, textvar=dell)
            e1.place(x=120, y=130)


            #tex = Text(root1)
            #tex.grid(row=2, columnspan=3)
            def ch_at():
                if len(dell.get()) == 0: 
                   messagebox.showwarning("warning","Please Enter Date.")
                elif (dell.get().isidentifier()):  
                    messagebox.showwarning("warning","Please Enter Proper Date")
                else:
                    #tex.delete("1.0",END)
                    date=e1.get()
                    li=[]
                    conn = db.connect('sample.db')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM DATA WHERE date='%s'"%(date))

                    tv = ttk.Treeview(root1, columns=(1,2,3),show="headings", height="22")
                    tv.place(x=5,y=200)
                    tv.heading(1, text="Name")
                    tv.heading(2, text="Date")
                    tv.heading(3, text="Attendance")

                    tvScrollbar=ttk.Scrollbar(root1,orient="vertical",command=tv.yview,)
                    tv.config(yscroll=tvScrollbar.set)
                    tvScrollbar.place(x=610,y=200,height=470)

                    tvScrollbar.config(command=tv.yview)            
                    for i in cur:
                        tv.insert('', 'end', values=i)
                        #li.append(i)
                        #li.append("\n")

                    
                    #tex.insert(END,li)
                    conn.commit()
                    cur.close()
                    conn.close()
                
            Button(root1, text='check', width=20, bg='brown',fg='white',command=ch_at).place(x=350, y=130)

            
            
            


                
            
        #submit data connection    

        conn = db.connect('sample.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS DATA
            (
              name TEXT,
              date TEXT,
              var TEXT
            )''')
        cur.close()
        conn.commit()
        conn.close()

        # submit button

        def put():
            if len(name.get()) == 0:
                messagebox.showwarning("warning","Please Enter Name.")
            elif (name.get().isdigit()):
                messagebox.showwarning("warning","Please Enter Proper Name.")
            elif len(date.get()) == 0:
                messagebox.showwarning("warning","Please Enter Date.")
            elif (date.get().isidentifier()):
                messagebox.showwarning("warning","Please Enter Proper Date")
            elif len(var.get()) == 0:
                messagebox.showwarning("warning","Please Select Radio Button.")
            else:   
                conn = db.connect('sample.db')
                cur = conn.cursor()
                cur.execute("insert into DATA values('%s', '%s', '%s')"%(name.get(), date.get(), var.get()))
                cur.close()
                conn.commit()
                conn.close()
                clear()
                messagebox.showinfo("Information","Submit Data...")
            

        name = StringVar()
        date = StringVar()
        now = datetime.datetime.now()
        date.set(now.strftime("%d-%m-%Y"))

        var = StringVar()
        var.set("Present")




        #label of the name, date, radiobutton
        c_width="500"
        c_height="800"
        c_widget = Canvas(root, width=c_width, height=c_height)
        c_widget.pack()
        c_widget.create_rectangle(0, 0, 800, 100, fill="#A71B05", outline="#A71B05")
        c_widget.create_rectangle(0, 100, 800, 80, fill="#DF1E0E", outline="#DF1E0E")

        label_1 = Label(root, text="Name", width=20, font=("bold", 10))
        label_1.place(x=0, y=130)
        name_entry = Entry(root, textvar=name)
        name_entry.place(x=120, y=130)

        label_2 = Label(root, text="Date", width=20, font=("bold", 10))
        label_2.place(x=0, y=170)
        label_3 = Label(root, text="dd-mm-yyyy", width=20, font=("bold", 10))
        label_3.place(x=200, y=170)
        email_entry = Entry(root, textvar=date)
        email_entry.place(x=120, y=170)

        label_3 = Label(root, text="Attendence", width=20, font=("bold", 10))
        label_3.place(x=0, y=200)
        radio1=Radiobutton(root, text="Absent", padx=5, variable=var, value="Absent")
        radio1.place(x=120, y=200)
        radio2=Radiobutton(root, text="Present", padx=20, variable=var, value="Present")
        radio2.place(x=190, y=200)

        Button(root, text='Submit', width=20, bg='brown',height=2,fg='white',command=put).place(x=30, y=250)
        Button(root, text='Check attendence', width=20, bg='brown',height=2,fg='white',command=click1).place(x=180, y=250)
  

        def clear():
            name_entry.delete(0, END)
            
            
        root.mainloop()

bt=Button(main, text='Login',width=20,height=2,bg='brown',fg='white', command=login).place(x=120,y=230)
bt1=Button(main, text='Registration',width=20,height=2,bg='red',fg='white', command=reg).place(x=120,y=280)
main.mainloop()


