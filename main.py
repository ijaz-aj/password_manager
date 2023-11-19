from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number

    shuffle(password_list)

    password = "".join(password_list)
    # it will show password in the password_entry
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    entry_website = website_entry.get()
    entry_email = email_entry.get()
    entry_password = password_entry.get()

    if len(entry_website) == 0 or len(entry_password) == 0:
        messagebox.showwarning(title="Warning!!", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=entry_website,
                                       message=f"These are the details you entered \nEmail: {entry_email} "
                                               f"\npassword: {entry_password}\n Is it ok to save ?")

        if is_ok:
            with open('data.txt', "a") as file:
                file.write(f"{entry_website} || {entry_email} || {entry_password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ---- Canvas ----

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ----- Labels -----

# website Label
website_label = Label(text="Website:")
website_label.config(pady=5)
website_label.grid(row=1, column=0)

# email label
email_label = Label(text="Email/Username:")
email_label.config(pady=5)
email_label.grid(row=2, column=0)

# password label
password_label = Label(text="Password:")
password_label.config(pady=5)
password_label.grid(row=3, column=0)

# ---- Entries ----

# website entry
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
# focus is used to cursor will ready in the text box
website_entry.focus()

# email entry
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "yourmail@gmail.com")

# password entry
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# ---- Buttons -----

# generate_password button
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2)

# add button
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# --- MainLoop ----

window.mainloop()
