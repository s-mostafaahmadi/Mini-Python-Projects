import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64

def encrypt_text():
    password = password_entry.get()
    text = text_entry.get()
    
    if not password or not text:
        messagebox.showwarning("Input Error", "Please enter both password and text.")
        return
    
    key = base64.urlsafe_b64encode(password.ljust(32).encode('utf-8'))
    fernet = Fernet(key)
    
    encrypted_txt = fernet.encrypt(text.encode('utf-8'))
    encrypted_text_var.set(encrypted_txt.decode('utf-8'))

def decrypt_text():
    password = password_entry.get()
    encrypted_txt = encrypted_text_var.get()
    
    if not password or not encrypted_txt:
        messagebox.showwarning("Input Error", "Please enter both password and encrypted text.")
        return
    
    key = base64.urlsafe_b64encode(password.ljust(32).encode('utf-8'))
    fernet = Fernet(key)
    
    try:
        decrypted_txt = fernet.decrypt(encrypted_txt.encode('utf-8'))
        decrypted_text_var.set(decrypted_txt.decode('utf-8'))
    except Exception as e:
        messagebox.showerror("Decryption Error", "Decryption failed. Please check the password or encrypted text.")

# Create the main window
root = tk.Tk()
root.title("Encrypt/Decrypt Text")

# Create and place the widgets
tk.Label(root, text="Password:").grid(row=0, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Text:").grid(row=1, column=0, padx=10, pady=10)
text_entry = tk.Entry(root, width=40)
text_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Encrypt", command=encrypt_text).grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text="Encrypted Text:").grid(row=3, column=0, padx=10, pady=10)
encrypted_text_var = tk.StringVar()
encrypted_text_entry = tk.Entry(root, textvariable=encrypted_text_var, width=40)
encrypted_text_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Button(root, text="Decrypt", command=decrypt_text).grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(root, text="Decrypted Text:").grid(row=5, column=0, padx=10, pady=10)
decrypted_text_var = tk.StringVar()
decrypted_text_entry = tk.Entry(root, textvariable=decrypted_text_var, width=40)
decrypted_text_entry.grid(row=5, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
