#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())

    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main Tkinter window
root = tk.Tk()
root.title("Random Password Generator")

# Label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

# Label and entry to display generated password
password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()

