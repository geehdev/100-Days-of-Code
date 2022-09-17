from tkinter import END, Canvas, Label, PhotoImage, Tk, ttk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list_letters = [choice(letters) for _ in range(randint(8, 10))]
    list_letters += [choice(symbols) for _ in range(randint(2, 4))]
    list_letters += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(list_letters)

    password = ' '.join(list_letters)

    entry_password.delete(0, END)

    entry_password.insert(0, password)
    pyperclip.copy(text=password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_all():
    my_website = website.get()
    my_email = email.get()
    my_password = entry_password.get()

    new_dict = {
        my_website: {
            'email': my_email,
            'password': my_password
        }
    }

    if bool(my_website) == False or bool(my_email) == False or bool(my_password) == False:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields em empty!")
    else:
        try:
            with open(file='password-manager\data.json', mode='r') as file:
                # Reading old data
                data = json.load(fp=file)

        except FileNotFoundError:
            with open(file='password-manager\data.json', mode='w') as new_file:
                json.dump(new_dict, new_file, indent=4)

        else:
            data.update(new_dict) # Updating old data with new data

            with open(file='password-manager\data.json', mode='w') as file: # Saving update data
                json.dump(data, file, indent=4)

        finally:
            website.delete(0, END)
            entry_password.delete(0, END)
            website.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_search():
    my_website = website.get()

    try:
        with open(file='password-manager\data.json', mode='r') as file:
            data = json.load(file)
            messagebox.showinfo(title=my_website, message=f"Email: {data[my_website]['email']} \nPassword: {data[my_website]['password']}")
    except FileNotFoundError:
            messagebox.showinfo(title=my_website, message="No Data File Found.")
    except KeyError:
            messagebox.showinfo(title=my_website, message=f"No details for {my_website} exists.")
    finally:
        website.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(background='white', padx=20, pady=20)

canvas = Canvas(width=200, height=200, background='white', highlightthickness=0)

path_logo = PhotoImage(file=r'password-manager\logo.png')

image = canvas.create_image(100, 100 , image=path_logo)
canvas.grid(column=1, row=0)

#labels
web_lb = Label(text='Website:', background='white')
web_lb.grid(row=1, column=0)

email_lb =Label(text='Email/Username:', background='white')
email_lb.grid(row=2, column=0)

password_lb = Label(text='Password:', background='white')
password_lb.grid(row=3, column=0)

#Entries
website = ttk.Entry(width=32)
website.grid(column=1, row=1)

email = ttk.Entry(width=50)
email.grid(column=1, row=2, columnspan=2)

entry_password = ttk.Entry(width=32)
entry_password.grid(column=1, row=3)

#Buttons
btn_search = ttk.Button(text='Search', width=17,command=find_search)
btn_search.grid(column=2, row=1)

generate = ttk.Button(text='Generate Password', command=generate_password)
generate.grid(column=2, row=3)

add = ttk.Button(text='Add', width=50, command=save_all)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()