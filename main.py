
from tkinter import *
from tkinter import messagebox
FONT = ("Arial", 8, "")
window = Tk()
window.title("Password manager")
window.config( padx = 20, pady = 20)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from  PG import Password_generator

password = Password_generator()
def generate():
    password.create_password()
    entry_password.delete(0, END)
    entry_password.insert(0, string=f"{password.user_password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0:
        messagebox.showinfo(title="Warning!",  message = "You forgot to write website!")
    elif  len(password) == 0:
        messagebox.showinfo(title="Warning!",message="You forgot to write password!")
    else:
        agree = messagebox.askokcancel(title= f"For website: {website}!", message = f"Email: {email},\nPassword: {password}.\nSaved it?")
        if agree:
            file = open("my_password.txt", "a")
            file.write(f"{website} | {email} | {password}\n")
            file.close()
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_email.delete(0, END)
            entry_email.insert(END, string="mgshmatok@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #



canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
logo_pass = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_pass)
canvas.grid(row =0, column = 1)

label_website = Label(text = "Website:", font = FONT)
label_website.grid(row = 1, column = 0)

label_email = Label(text = "Email/Username:", font = FONT)
label_email.grid(row = 2, column = 0)

label_password = Label(text = "Password:", font = FONT)
label_password.grid(row = 3, column = 0)

entry_website = Entry(width = 35)
entry_website.grid (row =1, column = 1, columnspan = 2)
entry_website.focus()
entry_email = Entry(width = 35)
entry_email.insert(END, string="miha@gmail.com")
entry_email.grid (row =2, column = 1, columnspan = 2)

entry_password = Entry(width = 17)
entry_password.grid (row =3, column = 1)

button_GP = Button(text = "Generate Password",width = 16, font = FONT, command = generate)
button_GP.grid(row = 3, column = 2)

button_add = Button(text = "ADD", width = 34, font = FONT, command = save)
button_add.grid(row = 4, column = 1, columnspan = 2)


window.mainloop()