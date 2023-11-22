from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json


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
    new_data = {
        entry_website: {
            "email": entry_email,
            "password": entry_password,
        }
    }

    if len(entry_website) == 0 or len(entry_password) == 0:
        messagebox.showwarning(title="Warning!!", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # create a new file
                json.dump(new_data, data_file, indent=4)

        else:
            # Update old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Write updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Find Password ------------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {email} \n"
                                                       f"password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"{website} is not found")


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
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
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

# search button
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

# generate_password button
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2)

# add button
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# --- MainLoop ----

window.mainloop()
