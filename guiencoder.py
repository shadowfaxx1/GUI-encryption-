from tkinter import *
import base64

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')
def Exit():
    root.destroy()
    
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

def test():
    root = Tk()
    root.geometry('500x300')
    root.resizable(0,0)
    root.title("kaif Message Encode and Decode")
    Label(root, text ='TEXT CRYPTIC', font = 'Helvetica 20 bold italic',bg='pink',fg='black').pack(side=TOP)
    Label(root, text ='used for safe message transfer', font = 'Helvetica 9  italic' ).pack(side=BOTTOM)
    Text = StringVar()
    private_key = StringVar()
    mode = StringVar()
    Result = StringVar()
    Label(root, font= 'Consolas 13 bold', text='MESSAGE').place(x= 60,y=60)
    Entry(root, font = 'Consolas 10', textvariable = Text, bg = 'ghost white',fg='red').place(x=290, y = 60)
    Label(root, font = 'Consolas 13 bold', text ='KEY').place(x=60, y = 90)
    Entry(root, font = 'Consolas 10', textvariable = private_key , bg ='ghost white',fg='pink').place(x=290, y = 90)
    Label(root, font = 'Consolas 13 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
    Entry(root, font = 'Consolas 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
    Entry(root, font = 'Consolas 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)
    Button(root, font = 'Consolas 10 bold', text = 'RESULT'  ,padx =6,bg ='orange' ,command = Mode).place(x=60, y = 150)
    Button(root, font = 'Times 10 italic' ,text ='RESET' ,width =6, command = Reset,bg = 'pink', padx=2).place(x=150, y = 220)
    Button(root, font = 'Times 10 italic ',text= 'EXIT' , width = 6, command = Exit,bg = 'cyan',fg='black', padx=2, pady=2).place(x=240, y = 220)
    root.mainloop()

if __name__ =="__main__":
    test()
    
    
    