from tkinter import *
from tkinter import messagebox
import cryptocode


window = Tk()
window.config(bg="black")
window.title("SecretNotes")


def encrypt():
    basliktmetni = titleInput.get()
    notmetni = textInput.get("1.0", END)
    masterkey= masterkeyInput.get()
    if len(basliktmetni) == 0 or len(notmetni) == 0 or len(masterkey) == 0:
        messagebox.showinfo("Hata", "Lütfen tüm bilgileri giriniz.")
    else:
        sifrelenmismetin = cryptocode.encrypt(notmetni, masterkey)
        with open("secretnotes.txt", "a") as dosya:
            dosya.write(("\n" + basliktmetni + ":" + "\n" + sifrelenmismetin + "\n"))
        notLabel.config(text=f"{basliktmetni} başlıklı notunuz kaydedildi.")
    textInput.delete("1.0", END)
    titleInput.delete(0, END)
    masterkeyInput.delete(0, END)


def decrypt():
    notunsifresi= textInput.get("1.0", END)
    masterkey= masterkeyInput.get()
    if len(notunsifresi) == 0 or len(masterkey) == 0:
        messagebox.showinfo("Hata", "Lütfen tüm bilgileri giriniz.")
    else:
        try:
            cozulmusmesaj= cryptocode.decrypt(notunsifresi, masterkey)
            textInput.delete("1.0", END)
            textInput.insert("1.0", cozulmusmesaj)
            notLabel.config(text="Notunuz çözüldü.")
        except:
            messagebox.showinfo("Hata", "Şifrelenmemiş notu çözmeye çalışma!")
            textInput.delete("1.0", END)
    masterkeyInput.delete(0, END)



#ui

logo= PhotoImage(file="secretnotes1.png")
logoLabel = Label(image=logo, pady=50)
logoLabel.pack()

titleLabel = Label(text="Enter your title", pady=10, bg="black", fg="white", font=("Arial", 20, "normal"))
titleLabel.pack()

titleInput = Entry(width=25)
titleInput.pack()

textLabel= Label(text="Enter your secret", pady=10, bg="black", fg="white",font=("Arial", 20, "normal"))
textLabel.pack()

textInput= Text(width=30, height=15)
textInput.pack()

notLabel= Label(text="", pady=10, bg="black", fg="white",font=("Arial", 15, "normal"))
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