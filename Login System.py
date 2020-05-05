
import tkinter as tk                                                                                                # importing tkinter module as 'tk'
import pickle                                                                                                       # importing pickle module for easy file operation
from tkinter import messagebox                                                                                      # importing messagebox module to display message boxes

# Defining main window of the program
root = tk.Tk()
root.title("Account log in System")                                                                                 # title of the main window
root.geometry("500x200")
#root.configure(bg = '#CAECCF')                                                                                     # setting background colour for the window


# Declaring variables for username and password
username = tk.StringVar()
password = tk.StringVar()

# Declaring an empty dictionary
# data stored in the file is later copied into this empty dictionary
dict = {}

# Defining functions
# Submit function: to validate the login credentials
def login():
    # Accessing Global variables
    global username
    global password
    global dict

    # Opening the file containing login credentials in the read-binary mode
    with open('Login_Credentials.pickle', 'rb') as f:
        dict = pickle.load(f)                                                                                       # loading data from the file onto the dictionary

    # Getting the credentials from the entry box
    username = username_entry.get()
    password = password_entry.get()

    # Deleting the entry boxes
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

    # Checking the username entered against its corresponding password stored in the dictionary
    if dict[username] == password:
        tk.messagebox.showinfo('Welcome', 'Login successful')                                                       # displaying the messagebox
        root.destroy()                                                                                              # closing the main window of operation

    else:
        tk.messagebox.showerror('Error', 'Incorrect username or password. Try again')                               # displaying the error message when the login credentials don't match
    return

# Function to save new user credentials into the Login credentials file
def save():
    # Accessing Global variables
    global username_register_entry
    global password_register_entry
    global reg_window
    global username
    global password
    global dict

    # Opening the Login credentials file in the read-binary mode
    with open('Login_Credentials.pickle', 'rb') as f:
        dict = pickle.load(f)                                                                                       # loads the values from the file onto the dictionary

    # Getting the user credentials from the Registration window
    username = username_register_entry.get()
    password = password_register_entry.get()

    # Updating the dictionary with new user credentials
    dict.update({username:password})

    # Opening the Login credential file to write new data into
    with open('Login_Credentials.pickle','wb') as f:
        pickle.dump(dict,f)                                                                                         # dumps the updated dictionary into the file

    reg_window.destroy()                                                                                            # destroys the registration window
    return

# Function to register new users
def register():
    # Accessing Global variables
    global username_register_entry
    global password_register_entry
    global reg_window

    # Creating a new(Registration) window
    reg_window = tk.Tk()
    reg_window.title("Welcome to registration")
    reg_window.colormapwindows
    reg_window.geometry("350x200")
    reg_window.configure(bg = '#E1CEB1')                                                                            # setting a background colour for the window

    # Creating entry widgets
    username_register_entry = tk.Entry(reg_window, width=30, borderwidth=5, textvariable=username)
    password_register_entry = tk.Entry(reg_window, width=30, textvariable=password, show='*', borderwidth=5)

    # Placing the entry widgets on the screen
    username_register_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
    password_register_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    # Creating labels
    username_register_label = tk.Label(reg_window, text="Choose your username",bg = '#E1CEB1')
    password_register_label = tk.Label(reg_window, text="Choose your password",bg = '#E1CEB1')

    # Placing the labels on the screen
    username_register_label.grid(row=1, column=0)
    password_register_label.grid(row=2, column=0)

    # Save Button
    save_btn = tk.Button(reg_window, text = 'Save',bg= '#D86C70', font = 'Calibri', borderwidth = 1, height =1, width = 5, command = save)
    save_btn.grid(row = 3, column = 2)
    return


# Creating entry widgets
username_entry = tk.Entry(root, width = 50, borderwidth = 5, textvariable = username)
password_entry = tk.Entry(root, width = 50, textvariable = password, show = '*', borderwidth = 5)

# Placing the entry widgets on the screen
username_entry.grid(row = 1, column = 1, columnspan = 3, padx = 10, pady = 10)
password_entry.grid(row = 2, column = 1, columnspan = 3, padx = 10, pady = 10)

# Creating labels
log_in_label = tk.Label(root, text = 'Login with your credentials', font = ('Calibri','16'))
username_label = tk.Label(root, text = "Enter your username")
password_label = tk.Label(root, text = "Enter your password")

# Placing the labels on the screen
log_in_label.grid(row = 0, column = 1)
username_label.grid(row = 1, column = 0)
password_label.grid(row = 2, column = 0)

# Creating Login, Register and submit buttons
#log_in_btn = tk.Button(root, text = 'Login', bg = '#76C4AE', font = 'Calibri', borderwidth = 2, height = 1, width = 5)
register_btn = tk.Button(root, text ='Register', bg = '#76C4AE', font = 'Calibri', borderwidth = 2, height = 1, width = 7, command = register)
log_in_btn = tk.Button(root, text = 'Login', bg= '#D86C70', font = 'Calibri', borderwidth = 1, height =1, width = 5, command = login)


# Placing the Login and Register Buttons on the screen
#log_in_btn.grid(row = 0, column = 1, sticky = tk.E)
register_btn.grid(row = 0, column = 3, sticky = tk.E)
log_in_btn.grid(row = 3, column = 2)

# Start of the program
root.mainloop()