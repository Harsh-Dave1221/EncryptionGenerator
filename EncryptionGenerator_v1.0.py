import tkinter as tk
from tkinter import simpledialog

# Updated encryption function to handle rotation based on user input
def encrypt(text, shift):
    # Ensure shift is within 0-25 range
    shift = shift % 26  # To handle shifts larger than 25 (e.g., ROT30 would be equivalent to ROT4)
    
    encrypted_text = ""
    
    # Iterate through each character in the text
    for c in text:
        if c.isupper():  # Encrypt uppercase letters
            encrypted_text += chr(((ord(c) - 65 + shift) % 26) + 65)
        elif c.islower():  # Encrypt lowercase letters
            encrypted_text += chr(((ord(c) - 97 + shift) % 26) + 97)
        else:
            encrypted_text += c  # Non-alphabetic characters are not changed

    return encrypted_text

# Function to handle when the button is clicked
def on_click():
    # Prompt user to enter plaintext
    plaintext = simpledialog.askstring("Input", "Enter plaintext for ROT / Rotation encryption:", parent=root)
    
    if plaintext:
        # Prompt the user for the rotation value (0-25)
        shift = simpledialog.askinteger("Input", "How much do you want to rotate by? (0-25)", parent=root, minvalue=0, maxvalue=25)
        
        if shift is not None:
            # Encrypt the plaintext using the rotation method with the selected shift value
            ciphertext = encrypt(plaintext, shift)
            
            # Display the ciphertext in the textbox
            ciphertext_display.config(state=tk.NORMAL)  # Enable editing
            ciphertext_display.delete(1.0, tk.END)  # Clear any previous content
            ciphertext_display.insert(tk.END, ciphertext)  # Insert new ciphertext
            ciphertext_display.config(state=tk.DISABLED)  # Disable editing (readonly)

# Create the main window
root = tk.Tk()
root.title("Encryption Program")

# Encryption button for ROT / Rotation
button_rot = tk.Button(root, text="ROT / Rotation", command=on_click)
button_rot.pack(padx=20, pady=5)

# Textbox to display the resulting ciphertext
ciphertext_display = tk.Text(root, height=5, width=40, wrap=tk.WORD, state=tk.DISABLED)
ciphertext_display.pack(padx=20, pady=20)

# Start the main event loop
root.mainloop()
