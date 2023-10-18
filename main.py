from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cryptocode


window = Tk()
window.config(bg="black")
window.title("SecretNotes")


def encrypt():
    basliktmetni = titleInput.get()
    notmetni = textInput.get("1.0", END)
    masterkey= masterkeyInput.get()
    if basliktmetni == "":
        messagebox.showinfo("Hata", "Lütfen bir başlık giriniz.")
    sifrelenmismetin = cryptocode.encrypt(notmetni, masterkey)
    with open("secretnotes4.txt", "a") as dosya:
        dosya.write((basliktmetni + ":" + "\n" + sifrelenmismetin + "\n"))
    textInput.delete("1.0", END)
    titleInput.delete(0, END)
    masterkeyInput.delete(0, END)


def decrypt():
    notunsifresi= textInput.get("1.0", END)
    masterkey= masterkeyInput.get()
    cozulmusmesaj= cryptocode.decrypt(notunsifresi, masterkey)
    notLabel.config(text=cozulmusmesaj)
    textInput.delete("1.0", END)
    masterkeyInput.delete(0, END)



#ui

logo = Image.open("secretnotes1.png")
logo1 = ImageTk.PhotoImage(logo)

logoLabel = Label(image=logo1, pady=50)
logoLabel.pack()

titleLabel = Label(text="Enter your title", pady=10, bg="black", fg="white", font=("Arial", 20, "normal"))
titleLabel.pack()

titleInput = Entry(width=25)
titleInput.pack()

textLabel= Label(text="Enter your secret", pady=10, bg="black", fg="white",font=("Arial", 20, "normal"))
textLabel.pack()

textInput= Text(width=30, height=15)
textInput.pack()

notLabel= Label(text="", pady=10, bg="black", fg="white",font=("Arial", 20, "normal"))
notLabel.pack()

masterkeyLabel = Label(text="Enter your master key", pady=10, bg="black", fg="white",font=("Arial", 20, "normal"))
masterkeyLabel.pack()

masterkeyInput = Entry(width=25)
masterkeyInput.pack()

encryptButton = Button(text="Save & Encrypt", command=encrypt)
encryptButton.pack()
decryptButton = Button(text="Decrypt", command=decrypt)
decryptButton.pack()




window.mainloop()