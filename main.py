from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letter_list + symbols_list + numbers_list
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email_username}"
                                               f"\n"f"Password: {password}\nIs it ok to save?")
        if is_ok:
            file = open("data.txt", "a")
            file.write(f"{website} | {email_username} | {password}\n")
            file.close()

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Email/Username
email_username_entry = Entry()
email_username_entry.insert(0, "test@email.com")
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

# Password
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

# Add button
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
