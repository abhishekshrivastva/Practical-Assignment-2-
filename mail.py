from tkinter import *
from tkinter import ttk

import smtplib
import webbrowser

def sendemail():
    try:
        
        sender = account.get()
        recepient = [receiver.get()]
        sub = subject.get()
        pswrd = password.get()
        msg = msgbody.get('1.0','end')
        msgtosend = """\
        From: %s
        To: %s
        subject: %s
        

        %s
        """ % (sender, recepient, sub, msg)
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.login(sender, pswrd)
        mail.sendmail(sender, recepient, msgtosend)
        mail.close()
        
        ttk.Label(mainframe, text="Email sent successfully").grid(column=4,row=9,sticky=W)

    except Exception as e:
        ttk.Label(mainframe, text=str(e)).grid(column=4,row=9,sticky=W)

def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")
   
def clear_search(event): 
    Cc.delete(0,END)
  

my_window = Tk()
my_window.title("Compose Email")
my_window.configure(background='gray')


mainframe = ttk.Frame(my_window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1,)
mainframe.rowconfigure(0, weight=1)
mainframe=my_window

account = StringVar()
password = StringVar()
receiver = StringVar()
Cc = StringVar()
Bcc = StringVar()
subject = StringVar()
msgbody = StringVar()

a = Label(mainframe, text="Click here to go to the settings to turn on the settings to use this app" , fg="Red", cursor="hand2", background='gray')
a.grid(columnspan=2,column=0, row=0, sticky=W)
a.bind("<Button-1>", setup)


ttk.Label(mainframe, text="Your Email Account:", background='gray' ).grid(column=0, row=1, sticky=W)
account_entry = ttk.Entry(mainframe, width=30, textvariable=account)
account_entry.grid(column=4, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Your Password: ", background='gray').grid(column=0, row=2, sticky=W)
password_entry = ttk.Entry(mainframe, show="*", width=30, textvariable=password)
password_entry.grid(column=4, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Reply to" , background='gray').grid(column=0, row=3, sticky=W)
receiver_entry = ttk.Entry(mainframe, width=30, textvariable=receiver)
receiver_entry.grid(column=4, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Cc", background='gray').grid(column=0, row=4, sticky=W)
Cc = ttk.Entry(mainframe, width=30, textvariable=Cc)
Cc.grid(column=4, row=4, sticky=(W, E))
Cc.insert(0, "Add Recipient") 
Cc.bind("<Button-1>", clear_search)

def clear_search(event): 
    Bcc.delete(0,END)
ttk.Label(mainframe, text="Bcc", background='gray').grid(column=0, row=5, sticky=W)
Bcc = ttk.Entry(mainframe, width=30, textvariable=Bcc)
Bcc.grid(column=4, row=5, sticky=(W, E))
Bcc.insert(0, "Add Recipient") 
Bcc.bind("<Button-1>", clear_search)


ttk.Label(mainframe, text="Compose Email", background='gray').grid(column=2, row=6, sticky=W)

ttk.Label(mainframe, text="Subject: ", background='gray').grid(column=0, row=7, sticky=W)
subject = ttk.Entry(mainframe, width=30, textvariable=subject)
subject.grid(column=4, row=7, sticky=(W, E))


ttk.Label(mainframe, text="Message Body: ", background='gray').grid(column=0, row=8, sticky=W)
msgbody = Text(mainframe, width=30, height=10)
msgbody.grid(column=4, row=8, sticky=(W, E))

ttk.Button(mainframe, text="Send", command=sendemail).grid(column=4,row=9,sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

account_entry.focus()

my_window.mainloop()
