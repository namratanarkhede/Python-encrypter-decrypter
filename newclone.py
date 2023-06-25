#from logging import root
from encodings import utf_8
from logging import root
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
from turtle import screensize
from PIL import Image,ImageTk
import base64
import os

global screen,code

def _show_value(v, *pargs):
    print(*pargs)
    print(v.get())

'''def Decryption():
    print("dEncrypting...........")'''


'''def Encryption():
    print("Encrypting...........")
    password="123"
    if password=="123":
        screen1=Toplevel()
        screen1.geometry("400x200")
        screen1.title("encryption")
        screen1.configure(bg="#ed3833")

        message=entextentryvalue.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(base64.encode_message)
        encypt=base64_bytes.decode("ascii")
        Label(screen1,text="Encrypt",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encypt)'''
        








mainrooot=Tk()
mainrooot.title('EnCrYpToR & DeCrYPtOr')
icon_photo=PhotoImage(file="icon.png")
mainrooot.iconphoto(FALSE,icon_photo)
mainrooot.geometry('500x500')
mainrooot.minsize(700,500)
mainrooot.maxsize(700,500)
#settingimageonbg
mainimg=PhotoImage(file="mainwinowbg.png")
mainlabel=Label(mainrooot,image=mainimg,borderwidth=10,bg="#14231c")
mainlabel.place(x=0,y=0)
mainlabel2=Label(mainrooot,image=mainimg,borderwidth=10,bg="#14231c")
mainlabel2.place(x=0,y=250)

#creatingkeybutton
mainkeyimage=Image.open("mainwinowbgkey.jpg")
img_resizekey=mainkeyimage.resize((150,150))
click_btnkey=ImageTk.PhotoImage(img_resizekey)

#Let us create a label for button event
img_labelkey= Label(image=click_btnkey)
def openenc():
    
    
    encryptionwindow()
    
    

def opendec():
    decryptionwindow()
    

#Let us create a dummy button and pass the image
buttonkey= Button(mainrooot, image=click_btnkey,command= opendec,borderwidth=5,bg="#14231c")
buttonkey.place(x=300,y=52,height=150,width=150)




#creatingkeybutton
mainlockimage=Image.open("mainwinowbglock.jpg")
img_resizelock=mainlockimage.resize((150,150))
click_btnlock=ImageTk.PhotoImage(img_resizelock)

#Let us create a label for button event
img_labellock= Label(image=click_btnlock)


#Let us create a dummy button and pass the image
buttonlock= Button(mainrooot, image=click_btnlock,command= openenc,borderwidth=5,bg="#14231c")
buttonlock.place(x=300,y=300,height=150,width=150)





def encryptionwindow():

 root = Toplevel()
 root.grab_set()
 root.title('EnCrYpToR')
 
 root.geometry('500x500')
 root.minsize(700,500)
 root.maxsize(700,500)
 root.config(bg='#015063')

#seting image in bg
 img = PhotoImage(file="encryptorbackground.png")

 label = Label( root, image=img,borderwidth=10,bg='#015063')
 
 label.place(x=0, y=0)
 

#setting icon in title bar
 img_icon=PhotoImage(file="icon.png")
 root.iconphoto(False,img_icon)

 enText=Label(root,text="Enter Text for Encryption",bg="#015063",fg="black",font="calbri 13 bold",border=10,relief=SUNKEN)
 enText.place(x=30,y=20)

#create variable for entry in string
 
 entextentryvalue=StringVar()
 entextentryvalue.trace('w', lambda *pargs: _show_value(entextentryvalue, *pargs))

 entextentry=Entry(root,textvariable=entextentryvalue,font="Robote 13",borderwidth=10,relief=GROOVE,bg="black",fg="white")
 entextentry.place(x=300,y=20,width=360,height=100)



 '''enkeyText=Label(root,text="KEY FOR DECRYPTION",bg="#015063",fg="black",font="calbri 13 bold",border=10,relief=SUNKEN)
 enkeyText.place(x=30,y=200)

#create variable for key
 enkeytextentryvalue=StringVar()
 enkeytextentryvalue.trace('w', lambda *pargs: _show_value(entextentryvalue, *pargs))
 enkeytextentry=Entry(root,textvariable=enkeytextentryvalue,show="*",font="Robote 13",borderwidth=10,relief=GROOVE,bg="black",fg="white")
 enkeytextentry.place(x=300,y=200,width=360,height=90)'''


#using lock image as button to decrypt
#defining funtion of the button

 def Encryption():
    print("Encrypting...........")
    key=Fernet.generate_key()
    #print(key)
    message=entextentryvalue.get().encode()
    f_obj=Fernet(key)
    encryptedmsg=f_obj.encrypt(message)
    screen1=Toplevel()
    root.grab_release()
    screen1.geometry("400x200")
    screen1.title("encryption")
    screen1.configure(bg="#F0FFFF")
    Label(screen1,text="dECRPYT",font="arial",fg="white",bg="#000000").place(x=10,y=0)
    text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=150)
    encrypt1=encryptedmsg
    Label(screen1,text="dECRPYT",font="arial",fg="white",bg="#000000").place(x=10,y=0)
    text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=150)
    backkslash="\n"

    text2.insert(END,encrypt1)
    text2.insert(END,backkslash)
    text2.insert(END,key)


    

 '''def Encryption():
    print("Encrypting...........")
    print(entextentryvalue.get())
    password="123"
    if enkeytextentryvalue.get()=="":
        messagebox.showerror("Please Enter Password !!")
    else:
        screen1=Toplevel()
        root.grab_release()
        screen1.geometry("400x200")
        screen1.title("encryption")
        screen1.configure(bg="#ed3833")

        message=entextentryvalue.get()
        encodemode=message.encode("ascii")
        base64_bytes=base64.b64encode(encodemode)
        encrypt=base64_bytes.decode("ascii")
        encrypt1=encrypt
        Label(screen1,text="encrypt1",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt1)'''




#Import the image using PhotoImage function
 image=Image.open("locktobeused.png")
 img_resize=image.resize((150,150))
 click_btn=ImageTk.PhotoImage(img_resize)

#Let us create a label for button event
 img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
 button= Button(root, image=click_btn,command= Encryption,borderwidth=5,bg="#015063")
 button.place(x=300,y=303,height=150,width=150)









 
 root.mainloop()




def decryptionwindow():
 
 deroot = Toplevel()
 deroot.grab_set()
 deroot.title('DeCrYpToR')
 
 deroot.geometry('500x500')
 deroot.minsize(700,500)
 deroot.maxsize(700,500)
 deroot.config(bg='#015063')

#seting image in bg
 img = PhotoImage(file="encryptorbackground.png")

 label = Label( deroot, image=img,borderwidth=10,bg='#015063')
 
 label.place(x=0, y=0)
 

#setting icon in title bar
 img_icon=PhotoImage(file="icon.png")
 deroot.iconphoto(False,img_icon)

 enText=Label(deroot,text="Enter Encrypted Text",bg="#015063",fg="black",font="calbri 13 bold",border=10,relief=SUNKEN)
 enText.place(x=30,y=20)

#create variable for entry in string
 entextentryvalue=StringVar()
 entextentryvalue.trace('w', lambda *pargs: _show_value(entextentryvalue, *pargs))
 entextentry=Entry(deroot,textvariable=entextentryvalue,font="Robote 13",borderwidth=10,relief=GROOVE,bg="black",fg="white")
 entextentry.place(x=300,y=20,width=360,height=100)



 enkeyText=Label(deroot,text="KEY FOR DECRYPTION",bg="#015063",fg="black",font="calbri 13 bold",border=10,relief=SUNKEN)
 enkeyText.place(x=30,y=200)

#create variable for key
 enkeytextentryvalue=StringVar()
 enkeytextentryvalue.trace('w', lambda *pargs: _show_value(enkeytextentryvalue, *pargs))
 enkeytextentry=Entry(deroot,textvariable=enkeytextentryvalue,show="*",font="Robote 13",borderwidth=10,relief=GROOVE,bg="black",fg="white")
 enkeytextentry.place(x=300,y=200,width=360,height=90)


#using lock image as button to decrypt
#defining funtion of the button
 def Decryption():
    print("dEcrypting...........")
    key=enkeytextentryvalue.get()
    msg=entextentryvalue.get()

    f_obj=Fernet(
        key.encode("utf-8")
    )
    decryptedmsg=f_obj.decrypt(msg.encode("utf-8"))
   # print(decryptedmsg)
    screen1=Toplevel()
    
    screen1.geometry("400x200")
    screen1.title("encryption")
    screen1.configure(bg="#F0FFFF")
    Label(screen1,text="dEcrypt",font="arial",fg="white",bg="#000000").place(x=10,y=0)
    text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=150)
    encrypt1=decryptedmsg
    Label(screen1,text="dEcrypt",font="arial",fg="white",bg="#000000").place(x=10,y=0)
    text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=150)
    text2.insert(END,encrypt1)





#Import the image using PhotoImage function
 image=Image.open("keytobeused.png")
 img_resize=image.resize((150,150))
 click_btn=ImageTk.PhotoImage(img_resize)

#Let us create a label for button event
 img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
 button= Button(deroot, image=click_btn,command= Decryption,borderwidth=5,bg="#015063")
 button.place(x=300,y=303,height=150,width=150)










 deroot.mainloop()


mainrooot.mainloop()
