from tkinter import *
from tkinter import messagebox
import random
import json

WHITE = "#FFFFFF"
PASSWORD_FILE = 'passwords.json'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    passwordList = password_letters+password_symbols+password_numbers

    random.shuffle(passwordList)
    password = "".join(passwordList)
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    password_entry.clipboard_clear()
    password_entry.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    log = {
        website: {
            "username": username,
            "password": password,
        },
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Do not leave the boxes empty!")
    else:
        # messagebox.askokcancel(
        #     title=website,
        #     message=f"These are the details entered: \nUsername: {username}\n"
        #             f"Password: {password}\nIs it okay to save?"
        # )

        try:
            with open(PASSWORD_FILE, 'r') as f:
                data = json.load(f)

        except FileNotFoundError:
            with open(PASSWORD_FILE, 'w') as f:
                json.dump(log, f, indent=4)
        
        else:
            data.update(log)
            with open(PASSWORD_FILE, 'w') as f:
                json.dump(data, f, indent=4)
        
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def search():
    website = website_entry.get()

    try:
        with open(PASSWORD_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="First time user? \nno saved passwords here")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No saved password for {website}\n Add a password first")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(height=200, width=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Labels
website = Label(text="Website:", bg=WHITE)
website.grid(row=1, column=0)

username = Label(text="Email/Username:", bg=WHITE)
username.grid(row=2, column=0)

password = Label(text="Password:", bg=WHITE)
password.grid(row=3, column=0)


# Entries
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1, padx=(23,0))
website_entry.focus()

username_entry = Entry(width=42)
username_entry.insert(0, "kunalG")
username_entry.grid(row=2, column=1, columnspan=2, padx=(40,0))

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, padx=(30, 0))


# Buttons
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2, padx=(50, 0))

search_btn = Button(text="Search", width=15, command=search)
search_btn.grid(row=1,column=2)

window.mainloop()
