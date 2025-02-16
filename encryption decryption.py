from tkinter import *
from tkinter import messagebox
import base64
import os


# Caesar Cipher encryption function
def encrypt_message(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted


# Caesar Cipher decryption function
def decrypt_message(encrypted_message, shift):
    decrypted = ""
    for char in encrypted_message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift - shift_base) % 26 + shift_base)
        else:
            decrypted += char
    return decrypted


def main_screen():
    screen = Tk()
    screen.geometry("375x398")
    screen.title("Encryption-Decryption Tool")

    # Check if the image file exists (optional)
    image_path = "keys.png"
    if os.path.exists(image_path):
        image_icon = PhotoImage(file=image_path)
        screen.iconphoto(False, image_icon)

    # Label for user input
    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)

    # Text field for input message
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    # Label for encrypted/decrypted message output
    output_label = Label(text="Output:", fg="black", font=("calibri", 13))
    output_label.place(x=10, y=160)

    # Text field for output
    text_output = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text_output.place(x=10, y=180, width=355, height=100)

    # Shift input for Caesar Cipher
    Label(text="Enter shift (1-25):", fg="black", font=("calibri", 13)).place(x=10, y=290)
    shift_entry = Entry(font="Roboto 12")
    shift_entry.place(x=10, y=320, width=100, height=25)

    def encrypt():
        message = text1.get("1.0", "end-1c")
        try:
            shift = int(shift_entry.get())
            if shift < 1 or shift > 25:
                messagebox.showerror("Error", "Shift must be between 1 and 25!")
                return
            encrypted_message = encrypt_message(message, shift)
            text_output.delete(1.0, "end")
            text_output.insert("1.0", encrypted_message)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid shift value!")

    def decrypt():
        encrypted_message = text1.get("1.0", "end-1c")
        try:
            shift = int(shift_entry.get())
            if shift < 1 or shift > 25:
                messagebox.showerror("Error", "Shift must be between 1 and 25!")
                return
            decrypted_message = decrypt_message(encrypted_message, shift)
            text_output.delete(1.0, "end")
            text_output.insert("1.0", decrypted_message)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid shift value!")

    # Encrypt button
    encrypt_button = Button(screen, text="Encrypt", width=15, height=2, command=encrypt)
    encrypt_button.place(x=10, y=350)

    # Decrypt button
    decrypt_button = Button(screen, text="Decrypt", width=15, height=2, command=decrypt)
    decrypt_button.place(x=180, y=350)

    screen.mainloop()


main_screen()
