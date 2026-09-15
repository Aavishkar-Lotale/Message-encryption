import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter import *
import base64
import pyperclip

root = tk.Tk()
root.title("Secure Line")
root.geometry('1920x1200')

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


def Mode():
    if mode.get() == 'e':
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode.get() == 'd':
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Error')


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


def copy_to_clipboard():
    pyperclip.copy(Result.get())


Label(root, font='Arial 20 bold', text='MESSAGE').grid(
    row=0, column=0, padx=10, pady=10)
Entry(root, font='Arial 16', textvariable=Text, bg='ghost white').grid(
    row=0, column=1, padx=10, pady=10)

Label(root, font='Arial 20 bold', text='KEY').grid(
    row=1, column=0, padx=10, pady=10)
Entry(root, font='Arial 16', textvariable=private_key,
      bg='ghost white').grid(row=1, column=1, padx=10, pady=10)

mode_frame = tk.Frame(root)
mode_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

encode_radio = tk.Radiobutton(
    mode_frame, text="Encode", variable=mode, value="e", font='Arial 16')
encode_radio.grid(row=0, column=0, padx=10, pady=10)

decode_radio = tk.Radiobutton(
    mode_frame, text="Decode", variable=mode, value="d", font='Arial 16')
decode_radio.grid(row=0, column=1, padx=10, pady=10)

Entry(root, font='Arial 16 bold', textvariable=Result, bg='ghost white',
      state='disabled').grid(row=3, column=0, columnspan=2, padx=10, pady=10)

Button(root, font='Arial 16 bold', text='Enter', padx=2, bg='LightGrey',
       command=Mode, width=10).grid(row=4, column=0, padx=10, pady=10)

Button(root, font='Arial 16 bold', text='Copy', padx=2, bg='LightGrey',
       command=copy_to_clipboard, width=10).grid(row=4, column=1, padx=10, pady=10)

Button(root, font='Arial 16 bold', text='Clear', width=10, command=Reset,
       bg='LimeGreen', padx=2).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

#pyinstaller --noconfirm --onefile --windowed --name "SecureLine"  "C:\Users\aavis\OneDrive\Desktop\Programming\Python\Programming Projects\Learning\Practice.py"
