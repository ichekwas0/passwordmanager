from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    random.shuffle(password_list)
    final_password = "".join(password_list)
    password_entry.insert(0, final_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave any fields empty")

    else:
        try:
            with open("data.json", mode='r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            new_search = json.load(data_file)
            website = website_entry.get()
            display = new_search[website]
            messagebox.showinfo(title=website, message=f"Email: {display['email']}\nPassword:{display['password']}")
    except FileNotFoundError:
        messagebox.showwarning(title='Error', message="File not found")
    except KeyError:
        messagebox.showwarning(title='Error', message='The key does not exist')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
canvas_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ifeanyichekwas.ic@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', command=find_password, width=15)
search_button.grid(column=3, row=1, columnspan=2)


window.mainloop()
