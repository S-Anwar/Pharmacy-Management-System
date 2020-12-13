from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

db=sqlite3.connect("pharmacy.db")
cur=db.cursor()
cur.execute('create table if not exists stock(name varchar(30) unique, price varchar(10), quantity int, category varchar(30), discount varchar(5))')
root = Tk()
root.title("Simple Pharmacy Managment System")
root.iconbitmap('1.ico')
root.resizable(False, False)
root.geometry('1000x400')

img=Image.open('pi.jpg')
pi=ImageTk.PhotoImage(img)
canvas=Canvas(root)
canvas.pack(fill='both', expand='yes')
canvas.create_image(0, 0, anchor='nw', image=pi)

var=-1

def additem():
    e1= entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    row=(e1,e2,e3,e4,e5)
    cur.execute('insert into stock values(?,?,?,?,?)', row)
    db.commit()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


def deleteitem():
    cur.execute("select * from stock")
    res=cur.fetchall()
    e1 = str(entry1.get())
    k=True
    for row in res:
        if e1 in row:
            temp="delete from stock where name='{}'".format(e1)
            cur.execute(temp)
            db.commit()
            k=False
    if k:
        messagebox.showinfo("Item not found", "No such element in record")
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

def firstitem():
    global var
    var=0
    cur.execute("select * from stock")
    res = cur.fetchall()
    if len(res) == 0:
        messagebox.showerror("Empty", "No record found")
    else:
        k=res[0]
        v=list(k)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry1.insert(0,str(v[0]))
        entry2.insert(0,str(v[1]))
        entry3.insert(0,str(v[2]))
        entry4.insert(0,str(v[3]))
        entry5.insert(0,str(v[4]))

def nextitem():
    global var
    var = var + 1
    cur.execute("select * from stock")
    res = cur.fetchall()

    if var == len(res) or len(res) == 0:
        var = 0
        messagebox.showinfo("EOF", "No more records to show")
    else:
        k = res[var]
        v = list(k)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))

def previousitem():
    global var
    var=var-1
    cur.execute("select * from stock")
    res = cur.fetchall()
    if var == -1 or len(res) == 0:
        var = 0
        messagebox.showinfo("EOF", "No more records to show")
    else:
        k = res[var]
        v = list(k)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)

        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))


def lastitem():
    global var
    var = 0
    cur.execute("select * from stock")
    res = cur.fetchall()
    if len(res) == 0:
        messagebox.showerror("Empty", "No record found")
    else:
        k = res[-1]
        v = list(k)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)

        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))



def updateitem():

    e1 = str(entry1.get())
    e2 = str(entry2.get())
    e3 = str(entry3.get())
    e4 = str(entry4.get())
    e5 = str(entry5.get())
    temp="update stock set name='{}', price='{}', quantity='{}', category='{}', discount='{}' where name='{}'".format(e1,e2,e3,e4,e5,e1)
    cur.execute(temp)
    db.commit()

def searchitem():
    i=-1
    e1 = str(entry1.get())
    global var
    k=True
    cur.execute("select * from stock")
    res = cur.fetchall()
    if len(res) == 0:
        messagebox.showerror("Empty", "No record found")
    else:
        for row in res:
            i=i+1
            if row[0]==e1:
                var=i
                k=False
                v=list(row)
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                entry5.delete(0, END)
                entry1.insert(0, str(v[0]))
                entry2.insert(0, str(v[1]))
                entry3.insert(0, str(v[2]))
                entry4.insert(0, str(v[3]))
                entry5.insert(0, str(v[4]))
        if k:
            messagebox.showerror("Error", "Record does not exists")

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

label0= Label(canvas,text="PHARMACY MANAGEMENT SYSTEM ",bg="misty rose",fg="ivory4",font=("Times", 30))
label1=Label(canvas,text="ENTER ITEM NAME",bg="slate blue",relief="ridge",fg="white",font=("Times", 12),width=25)
entry1=Entry(canvas , font=("Times", 12))
label2=Label(canvas, text="ENTER ITEM PRICE",bd="2",relief="ridge",height="1",bg="slate blue",fg="white", font=("Times", 12),width=25)
entry2= Entry(canvas, font=("Times", 12))
label3=Label(canvas, text="ENTER ITEM QUANTITY",bd="2",relief="ridge",bg="slate blue",fg="white", font=("Times", 12),width=25)
entry3= Entry(canvas, font=("Times", 12))
label4=Label(canvas, text="ENTER ITEM CATEGORY",bd="2",relief="ridge",bg="slate blue",fg="white", font=("Times", 12),width=25)
entry4= Entry(canvas, font=("Times", 12))
label5=Label(canvas, text="ENTER ITEM DISCOUNT",bg="slate blue",relief="ridge",fg="white", font=("Times", 12),width=25)
entry5= Entry(canvas, font=("Times", 12))
button1= Button(canvas, text="ADD ITEM", bg="white", fg="black", width=20, font=("Times", 12),command=additem)
button2= Button(canvas, text="DELETE ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=deleteitem)
button3= Button(canvas, text="VIEW FIRST ITEM" , bg="white", fg="black", width =20, font=("Times", 12),command=firstitem)
button4= Button(canvas, text="VIEW NEXT ITEM" , bg="white", fg="black", width =20, font=("Times", 12), command=nextitem)
button5= Button(canvas, text="VIEW PREVIOUS ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=previousitem)
button6= Button(canvas, text="VIEW LAST ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=lastitem)
button7= Button(canvas, text="UPDATE ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=updateitem)
button8= Button(canvas, text="SEARCH ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=searchitem)
button9= Button(canvas, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12),command=clearitem)
label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
label4.grid(row=4,column=0, sticky=W, padx=10, pady=10)
label5.grid(row=5,column=0, sticky=W, padx=10, pady=10)
entry1.grid(row=1,column=1, padx=40, pady=10)
entry2.grid(row=2,column=1, padx=10, pady=10)
entry3.grid(row=3,column=1, padx=10, pady=10)
entry4.grid(row=4,column=1, padx=10, pady=10)
entry5.grid(row=5,column=1, padx=10, pady=10)
button1.grid(row=1,column=4, padx=40, pady=10)
button2.grid(row=1,column=5, padx=40, pady=10)
button3.grid(row=2,column=4, padx=40, pady=10)
button4.grid(row=2,column=5, padx=40, pady=10)
button5.grid(row=3,column=4, padx=40, pady=10)
button6.grid(row=3,column=5, padx=40, pady=10)
button7.grid(row=4,column=4, padx=40, pady=10)
button8.grid(row=4,column=5, padx=40, pady=10)
button9.grid(row=5,column=5, padx=40, pady=10)
root.mainloop()
