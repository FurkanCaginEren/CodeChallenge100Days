from tkinter import Canvas, Tk, PhotoImage, Label, Entry, Button, W, E, END
import os
from tkinter import messagebox
import random
import sys
import pandas
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SEARCH WEBSITE ------------------------------- #


def search():
    website_text = entry_website.get().title()
    try:
        with open("password-manage/password_data.json", "r") as data_file:
            # Reading Data for email
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website_text in data:
            email = data[website_text]['email']
            password =data[website_text]['password']
            messagebox.showinfo(
                title="Website Information", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message="No Website Found")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website_text = entry_website.get().title()
    email_text = entry_email.get()
    password_text = entry_password.get()
    new_data = {
        website_text: {
            "email": email_text,
            "password": password_text,
        }
    }

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(
            title="OOPS", message="Please don't leave any fields empty")
    else:
        try:
            with open("password-manage/password_data.json", "r") as data_file:

                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("password-manage/password_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:

            # Update data
            data.update(new_data)
            with open("password-manage/password_data.json", "w") as data_file:

                # Saving Updated data
                json.dump(data, data_file, indent=4)
        finally:

            entry_password.delete(0, END)
            entry_website.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=40, pady=40)


canvas = Canvas(width=200, height=200)
logo = os.path.abspath("password-manage/logo.png")
background_logo = PhotoImage(file=logo)
canvas.create_image(100, 100, image=background_logo)
canvas.grid(row=0, column=1, pady=2)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0, sticky=E, pady=2, padx=2)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0, sticky=E, pady=2, padx=2)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0, sticky=E, pady=2, padx=2)


entry_website = Entry(width=25)
entry_website.grid(row=1, column=1, sticky=W, pady=2)
entry_website.focus()


entry_email = Entry(width=44)
entry_email.insert(0, "fcagineren@gmail.com")
entry_email.grid(row=2, column=1,  sticky=W, pady=2)

entry_password = Entry(width=25)
entry_password.grid(row=3, column=1, sticky=W, pady=2)

button_password = Button(text="Generate Password", command=generate_password)
button_password.grid(row=3, column=1, columnspan=2, sticky=E, pady=2)

button_add = Button(text="Add", width=37, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)

button_search = Button(text="Search", width=14, command=search)
button_search.grid(row=1, column=1, columnspan=2, sticky=E, pady=2)


screen.mainloop()
