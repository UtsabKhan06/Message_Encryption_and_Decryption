from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()
screen.geometry('500x500')
screen.title('Message Encryption')
screen.configure(background='wheat')
def encrypt():
    password=code.get()
    if password=='1234':
        screen1=Toplevel(screen)
        screen1.title('Encryption')
        screen1.geometry('400x300')

        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1,text='Your message has been encrypted',font='impack 16 bold',bg='green',fg='white',bd=4).place(x=4,y=10)
        text2 = Text(screen1,font="16",bd=4,wrap=WORD)
        text2.place(x=4,y=70,width=390,height=200)
        text2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror('Error','Please enter the key')
    elif(password!="1234"):
        messagebox.showerror('Error','Invalid Key')


def decrypt():
    password = code.get()
    if password == '1234':
        screen2 = Toplevel(screen)
        screen2.title('Decryption')
        screen2.geometry('400x300')

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2, text='Your message has been Decrypted', font='impack 16 bold', bg='green', fg='white',
              bd=4).place(x=4, y=10)
        text2 = Text(screen2, font="16", bd=4, wrap=WORD)
        text2.place(x=4, y=70, width=390, height=200)
        text2.insert(END, encrypt)

    elif (password == ""):
        messagebox.showerror('Error', 'Please enter the key')
    elif (password != "1234"):
        messagebox.showerror('Error', 'Invalid Key')



#label
Label(screen,text="Enter Message To Encrypt or Decrypt",font="Helvetica 16 bold",bg="cyan",bd=4).place(x=64,y=10)
#text
text1=Text(screen,font='12',bd=4)
text1.place(x=10,y=60,width=480,height=100)
#label
Label(screen,text='Enter Key',font='Helvetica 16 bold',bg='black',fg='white',bd=4).place(x=200,y=200)
#entry
code=StringVar()
Entry(textvariable=code,bd=4,font='10',show='*').place(x=138,y=240)
#button
Button(screen,text='Encrypt',bg='red',fg='white',font='Helvetica 14 bold',bd=4,command=encrypt).place(x=25,y=300,width=180)
Button(screen,text='Decrypt',bg='red',fg='white',font='Helvetica 14 bold',bd=4,command=decrypt).place(x=290,y=300,width=180)
Button(screen,text='Reset',bg='blue',fg='white',font='Helvetica 14 bold',bd=4).place(x=160,y=350,width=180)
mainloop()