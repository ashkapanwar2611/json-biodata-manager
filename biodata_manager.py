import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "biodata.json"

# Load existing JSON data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


# Save biodata to JSON file
def save_biodata():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    edu = edu_text.get("1.0", tk.END).strip()
    skills = skills_text.get("1.0", tk.END).strip()
    projects = proj_text.get("1.0", tk.END).strip()

    if not name or not email or not phone:
        messagebox.showwarning("Warning", "Name, Email & Phone are required!")
        return

    # Load existing entries
    data = load_data()

    new_biodata = {
        "name": name,
        "email": email,
        "phone": phone,
        "education": edu,
        "skills": skills,
        "projects": projects
    }

    data.append(new_biodata)

    # Write back to JSON file
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    messagebox.showinfo("Saved", "Biodata saved successfully!")

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    edu_text.delete("1.0", tk.END)
    skills_text.delete("1.0", tk.END)
    proj_text.delete("1.0", tk.END)


# View Biodata from JSON
def view_biodata():
    output.delete("1.0", tk.END)

    data = load_data()

    if not data:
        output.insert(tk.END, "No biodata records found.")
        return

    for i, entry in enumerate(data, start=1):
        output.insert(tk.END, f"Record #{i}\n")
        output.insert(tk.END, f"Name: {entry['name']}\n")
        output.insert(tk.END, f"Email: {entry['email']}\n")
        output.insert(tk.END, f"Phone: {entry['phone']}\n")
        output.insert(tk.END, f"Education: {entry['education']}\n")
        output.insert(tk.END, f"Skills: {entry['skills']}\n")
        output.insert(tk.END, f"Projects: {entry['projects']}\n")
        output.insert(tk.END, "-----------------------------\n")


# GUI Window
app = ttk.Window("JSON Biodata Manager", "superhero", size=(850, 650))

title = ttk.Label(app, text="📄 JSON-Based Biodata Management System",
                  font=("Segoe UI", 22, "bold"))
title.pack(pady=15)

form = ttk.Frame(app, padding=20, bootstyle="secondary")
form.pack(padx=20, pady=10, fill="x")

ttk.Label(form, text="Full Name:", font=("Segoe UI", 12)).grid(row=0, column=0, pady=5, sticky="w")
name_entry = ttk.Entry(form, width=50, bootstyle="info")
name_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(form, text="Email:", font=("Segoe UI", 12)).grid(row=1, column=0, pady=5, sticky="w")
email_entry = ttk.Entry(form, width=50, bootstyle="info")
email_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(form, text="Phone:", font=("Segoe UI", 12)).grid(row=2, column=0, pady=5, sticky="w")
phone_entry = ttk.Entry(form, width=50, bootstyle="info")
phone_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(form, text="Education:", font=("Segoe UI", 12)).grid(row=3, column=0, pady=5, sticky="nw")
edu_text = tk.Text(form, height=3, width=50, font=("Segoe UI", 10))
edu_text.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(form, text="Skills:", font=("Segoe UI", 12)).grid(row=4, column=0, pady=5, sticky="nw")
skills_text = tk.Text(form, height=3, width=50, font=("Segoe UI", 10))
skills_text.grid(row=4, column=1, padx=10, pady=5)

ttk.Label(form, text="Projects:", font=("Segoe UI", 12)).grid(row=5, column=0, pady=5, sticky="nw")
proj_text = tk.Text(form, height=3, width=50, font=("Segoe UI", 10))
proj_text.grid(row=5, column=1, padx=10, pady=5)

btn_frame = ttk.Frame(app)
btn_frame.pack(pady=10)

save_btn = ttk.Button(btn_frame, text="💾 Save Biodata", bootstyle="success",
                      width=18, command=save_biodata)
save_btn.grid(row=0, column=0, padx=10)

view_btn = ttk.Button(btn_frame, text="📂 View All", bootstyle="info",
                      width=18, command=view_biodata)
view_btn.grid(row=0, column=1, padx=10)

output = tk.Text(app, height=12, font=("Consolas", 11),
                 bg="#1e1e1e", fg="white", relief="flat")
output.pack(padx=20, pady=10, fill="both")

app.mainloop()