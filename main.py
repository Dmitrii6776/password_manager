from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json


# ---------------------------- Search data ------------------------------- #
def search():
    website = website_text.get().capitalize()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\n'
                                                       f'Password: {password}')
    except Exception:
        messagebox.showinfo(title="Error", message="Does`not exist.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = random_letters + random_symbols + random_numbers

    shuffle(password_list)

    password = "".join(password_list)
    global password_text
    password_text.delete(0, END)
    password_text.insert(0, f'{password}')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title='Warning', message="Please don't leave any fields empty.")
    else:
        try:
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open('data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)
        except Exception:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, heigh=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:', font=("Courier", 10))
website_label.grid(row=1, column=0)
website_text = Entry(width=24)
website_text.grid(row=1, column=1)

search_button = Button(text='Search', font=("Courier", 9), command=search, width=14)
search_button.grid(row=1, column=2)

email_label = Label(text='Email/Username:', font=("Courier", 10))
email_label.grid(column=0, row=2)
email_text = Entry(width=40)
website_text.focus()
email_text.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:', font=("Courier", 10))
password_label.grid(row=3, column=0)
password_text = Entry(width=24)
password_text.grid(row=3, column=1)

generate_password_button = Button(text='Generate password', font=("Courier", 9), highlightthickness=0,
                                  command=password_generator, width=14)
generate_password_button.grid(row=3, column=2)

add_button = Button(text='Add', font=("Courier", 10), width=37, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
