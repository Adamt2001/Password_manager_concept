# this code is a proof of concept code to understand tkinter and learn more about GUI with python, i do not recommend
# using this code to actually store passwords as this is not a secure system and there is no encryption on the master
# password, or the passwords stored in the txt file.

import tkinter as tk
from tkinter import messagebox
from itertools import islice

# setting the window variables
height = 500
width = 600
root = tk.Tk()
root.title("Password Manager")
root.iconbitmap("icon.ico")
v = tk.StringVar()

# creating the variable using the dimensions and background I chose
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()
background_image = tk.PhotoImage(file="KGzRuTD.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


# function to run the login page
def login_page():
    print("login page")
    login_frame = tk.Frame(root, bg="#80c1ff", bd=5)
    login_frame.place(anchor="nw", relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)

    login_label = tk.Label(login_frame, text="Enter Admin Password to Login", bg="white")
    login_label.place(relwidth=1, relheight=0.2)

    login_entry = tk.Entry(login_frame, font=30)
    login_entry.place(rely=0.4, relwidth=0.65, relheight=0.2)

    login_button = tk.Button(login_frame, text="Login", font=10, command=lambda: [
        access_tester(login_entry.get()),
        login_frame.destroy(),
        login_label.destroy(),
        login_entry.destroy(),
        login_button.destroy()])
    login_button.place(relx=0.7, rely=0.25, relwidth=0.3, relheight=0.5)


# testing to see if the user has entered the correct password, if yest it will open the password page, if not,
# it will show a popup error. set the temp password to Admin123.
def access_tester(entry):
    if entry == "Admin123":
        print("Password Accepted")
        password_page()
    else:
        messagebox.showerror("Error", "Wrong Password Entered!")
        login_page()
        print("Incorrect Password Entered")


# opens the password page to view and search for passwords
def password_page():
    global v
    searching = 0
    print("passwords_page")
    home_frame = tk.Frame(root, bg="#80c1ff", bd=5)
    home_frame.place(anchor="n", relx=0.35, rely=0.1, relwidth=0.6, relheight=0.1)

    home_search_button = tk.Button(home_frame, text="Get Password", font=20, command=lambda: [
        password_search(entry.get())])
    home_search_button.place(relx=0.7, relwidth=0.3, relheight=1)

    entry = tk.Entry(home_frame, font=30)
    entry.place(relwidth=0.65, relheight=1)

    new_frame = tk.Frame(root, bg="#80c1ff", bd=5)
    new_frame.place(anchor="n", relx=0.83, rely=0.1, relwidth=0.25, relheight=0.1)

    new_account_button = tk.Button(new_frame, text="New Account", font=30, command=lambda: [
        home_frame.destroy(),
        home_search_button.destroy(),
        new_frame.destroy(),
        new_account_button.destroy(),
        entry.destroy(),
        result_frame.destroy(),
        result_frame.destroy(),
        logout_frame.destroy(),
        logout_button.destroy(),
        new_account()])
    new_account_button.place(relwidth=1, relheight=1)

    result_frame = tk.Frame(root, bg="#80c1ff", bd=10)
    result_frame.place(anchor="n", relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6)

    result_label = tk.Label(result_frame, bg="white", textvariable=v, font=40)
    result_label.place(relwidth=1, relheight=1)

    logout_frame = tk.Frame(root, bg="#80c1ff", bd=5)
    logout_frame.place(anchor="n", relx=0.92, rely=0.025, relwidth=0.12, relheight=0.057)

    logout_button = tk.Button(logout_frame, text="Logout", font=20, command=lambda: [
        home_frame.destroy(),
        home_search_button.destroy(),
        new_frame.destroy(),
        new_account_button.destroy(),
        entry.destroy(),
        result_frame.destroy(),
        result_frame.destroy(),
        logout_frame.destroy(),
        logout_button.destroy(),
        login_page()
    ])
    logout_button.place(relwidth=1, relheight=1)

    if searching == 1:
        print("searching for password")


# page for entering new passwords
def new_account():
    print("New Accounts Page")
    na_frame = tk.Frame(root, bg="#80c1ff", bd=5)
    na_frame.place(anchor="nw", relx=0.25, rely=0.25, relwidth=0.5, relheight=0.4)

    na_label = tk.Label(na_frame, text="Enter new entry here: (Name email password)", bg="white")
    na_label.place(relwidth=1, relheight=0.2)

    na_entry = tk.Entry(na_frame, font=30)
    na_entry.place(rely=0.45, relwidth=0.65, relheight=0.2)

    na_exit_button = tk.Button(na_frame, text="Submit", font=10, command=lambda: [
        new_data_write(na_entry.get()),
        na_frame.destroy(),
        na_label.destroy(),
        na_entry.destroy(),
        na_exit_button.destroy(),
        logout_frame.destroy(),
        logout_button.destroy()
    ])
    na_exit_button.place(relx=0.7, rely=0.4, relwidth=0.3, relheight=0.3)

    logout_frame = tk.Frame(root, bg="#80c1ff", bd=5)
    logout_frame.place(anchor="n", relx=0.92, rely=0.025, relwidth=0.12, relheight=0.057)

    logout_button = tk.Button(logout_frame, text="Exit", font=20, command=lambda: [
        password_page(),
        na_frame.destroy(),
        na_label.destroy(),
        na_entry.destroy(),
        na_exit_button.destroy(),
        logout_frame.destroy(),
        logout_button.destroy()
    ])
    logout_button.place(relwidth=1, relheight=1)


# function to write new data entries to the txt file containing all the passwords
def new_data_write(na_entry):
    print("new data write")
    with open("extension.txt", "a+") as my_file:
        my_file.seek(0)
        data = my_file.read(100)
        if len(data) > 0:
            my_file.write("\n")
        my_file.write(na_entry)
        new_account()
        messagebox.showinfo(title="New Data Write", message="New Credentials Added!")


# function to read the password txt file
def password_search(entry):
    global v
    print("searching for ", entry)
    with open("extension.txt", "r") as my_file:
        for line in my_file:
            if line.startswith(entry):
                my_list = [line.split()]
                my_list.extend(extra.strip() for extra in islice(my_file, 0))
                result = line
                print(result)
                v.set(line)
                return v, line


login_page()
root.mainloop()
