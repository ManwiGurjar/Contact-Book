#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

def add_contact():
    name = name_entry.get()
    contact_number = contact_number_entry.get()
    
    if name and contact_number:
        names.append(name)
        contact_numbers.append(contact_number)
        update_contact_list()
        name_entry.delete(0, tk.END)
        contact_number_entry.delete(0, tk.END)

def search_contact():
    search_term = search_entry.get()
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    
    if search_term:
        found = False
        for i in range(len(names)):
            if search_term.lower() in names[i].lower():
                result_text.insert(tk.END, f"Name: {names[i]}, Phone Number: {contact_numbers[i]}\n")
                found = True
        if not found:
            result_text.insert(tk.END, "No records found.")
    else:
        result_text.insert(tk.END, "Please enter a search term.")
    
    result_text.config(state=tk.DISABLED)

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in names:
        contact_listbox.insert(tk.END, name)

# Initialize empty lists to store names and contact numbers
names = []
contact_numbers = []

# Create the main GUI window
root = tk.Tk()
root.title("Contact Management")

# Create and configure the entry fields and buttons
name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

contact_number_label = tk.Label(root, text="Contact Number:")
contact_number_label.pack()

contact_number_entry = tk.Entry(root)
contact_number_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()

search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

# Create a listbox to display contact names
contact_listbox = tk.Listbox(root)
contact_listbox.pack()

# Create a text widget to display search results
result_text = tk.Text(root, height=5, width=40)
result_text.pack()
result_text.config(state=tk.DISABLED)

# Start the GUI main loop
root.mainloop()

