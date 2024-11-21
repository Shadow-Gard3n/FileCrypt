import tkinter as tk
from cryptography.fernet import Fernet

def submiten():
    fileToget = entryaskfile.get()
    fileTosave = entryaskloc.get()
    try:
        key = Fernet.generate_key()
        cipher = Fernet(key)
        with open(f'{fileTosave}\\secret.key', 'wb') as key_file:
            key_file.write(key)
        with open(f'{fileToget}', 'rb') as f:
            file_data = f.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(f'{fileTosave}\\EncryptedFile.txt', 'wb') as f:
            f.write(encrypted_data)
        labelendone.config(text = f'File encrypted successfully in {fileTosave}\\EncryptedFile.txt !')
        labelendone.place(x = 380,y = 480)      
    except Exception as e:
        print(f"Error during encryption: {e}")

def submitde():
    fileToget = entryaskfile.get()
    fileTosave = entryaskloc.get()
    try:
        with open(f'{fileToget}\\secret.key', 'rb') as key_file:
            key = key_file.read()
        cipher = Fernet(key)
        with open(f'{fileToget}\\EncryptedFile.txt', 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(fileTosave, 'wb') as f:
            f.write(decrypted_data)
        labeldedone.config(text = f"File decrypted successfully in {fileTosave}")
        labeldedone.place(x = 380,y = 480)    
    except Exception as e:
        print(f"Error during decryption: {e}")

def encryption():
    entryaskfile.delete(0, tk.END)
    entryaskloc.delete(0, tk.END)
    labelaskfile.config(text = "File location")
    labelaskfile.place(x = 450,y = 200)
    labelaskloc.config(text = "Folder location to save ?")
    labelaskloc.place(x = 450,y = 300)
    entryaskfile.place(x = 450,y = 250)
    entryaskloc.place(x = 450, y = 350)
    buttonen.place(x = 560, y = 405)
    labelendone.place_forget()
    labeldedone.place_forget()
    labelfilecrypt.place_forget()
    labeltext.place_forget()
    
def decryption():
    entryaskfile.delete(0, tk.END)
    entryaskloc.delete(0, tk.END)
    labelaskfile.config(text = "Folder location")
    labelaskfile.place(x = 450,y = 200)
    labelaskloc.config(text = "File location to save ?")
    labelaskloc.place(x = 450,y = 300)
    entryaskfile.place(x = 450,y = 250)
    entryaskloc.place(x = 450, y = 350)
    buttonde.place(x = 560, y = 405)
    labeldedone.place_forget()
    labelendone.place_forget()
    labelfilecrypt.place_forget()
    labeltext.place_forget()

def help():
    entryaskfile.place_forget()
    entryaskloc.place_forget()
    labelaskfile.place_forget()
    labelaskloc.place_forget()
    buttonde.place_forget()
    buttonen.place_forget()
    labeldedone.place_forget()
    labelendone.place_forget()
    labelfilecrypt.place(x = 350,y = 20)
    labeltext.place(x = 350,y = 80)

# window strt
window = tk.Tk()
icon_image = tk.PhotoImage(file="logo.png")
window.iconphoto(True, icon_image)
window.title("FileCrypt")
window.geometry("1920x1080")
window.config(background='black')

label_image = tk.PhotoImage(file="logo.png")
label_image = label_image.subsample(3, 3) 

labelside = tk.Label(window,
                bg='white',
                width = 47,
                height = 50,
                )
labelside.place(x = 0,y = 0)

labeldedone = tk.Label(window,
                        text = '',
                        font = ('Arial',20,'bold'),
                        fg = '#00FF00',
                        bg = 'black',
                        )

labelendone = tk.Label(window,
                        text = '',
                        font = ('Arial',20,'bold'),
                        fg = '#00FF00',
                        bg = 'black',
                        )    
labelendone.place(x = 450,y = 480)

labellogo = tk.Label(window,
                text = "FILECRYPT",
                font = ('Arial',30,'bold'),
                fg = 'black',
                bg='white',
                image = label_image,
                compound='top',
                padx = 30,
                pady = 5,
                )
labellogo.place(x = 40, y = 0)

buttonencrypt = tk.Button(window, text = "ENCRYPTION",
                        font = ("Comic Sans",20,'bold'),
                        fg = 'black',bg = '#00FF00',
                        width = 19,
                        command = encryption,
                        borderwidth=3,
                        activebackground='black',activeforeground='#00FF00')
buttonencrypt.place(x = 0,y = 170)

buttondecrypt = tk.Button(window, text = "DECRYPTION",
                        font = ("Comic Sans",20,'bold'),
                        fg = 'black',bg = '#00FF00',
                        width = 19,
                        command = decryption,
                        borderwidth=3,
                        activebackground='black',activeforeground='#00FF00')
buttondecrypt.place(x = 0,y = 240)

labelaskfile = tk.Label(window,
                    text = "File location",
                    font = ('Arial',20,'bold'),
                    fg = '#00FF00',
                    bg = 'black',
                    )

labelaskloc = tk.Label(window,
                    text = "Folder location to save ?",
                    font = ('Arial',20,'bold'),
                    fg = '#00FF00',
                    bg = 'black'
                    )

labelfilecrypt = tk.Label(window,
                    text = "WELCOME TO FILECRYPT",
                    font = ('Arial',30,'bold'),
                    fg = '#00FF00',
                    bg = 'black'
                    )

labeltext = tk.Label(window,
                    text = """
For Encryption:
    1. Click on Encryption button.
    2. Type the location of file you need to encrypt in File location.
        Example: "D:\\Folder\\Filename.txt"
    3. Type the Folder location where you want to put encrypted file with 
        secret key in Folder location.
    4. Your encrypted file can be found in that folder location.

For Decryption:
    1. Click on Decryption button.
    2. Type the location of folder which contains secret key and Encrypted 
        file together in Folder location.
    3. Type the File location where you want to put decrypted file in File 
        location.
    4. Your decrypted file can be found in that file location.
""",
                    font = ('Arial',18,'bold'),
                    justify="left",  
                    fg = '#00FF00',
                    bg = 'black'
                    )

entryaskfile = tk.Entry(window, 
                    font = ('Arial',20),
                    fg = 'black',
                    bg = "white")

entryaskloc = tk.Entry(window,
                    font = ('Arial',20),
                    fg = 'black',
                    bg = "white")

buttonen = tk.Button(window,text = "SUBMIT", 
                    font = ("Comic Sans",15,'bold'), 
                    fg = 'black',bg = '#00FF00',
                    command=submiten,
                    relief = 'raised',
                    borderwidth=3,
                    activebackground='#00FF00',activeforeground='white')

buttonde = tk.Button(window,text = "SUBMIT", 
                    font = ("Comic Sans",15,'bold'), 
                    fg = 'black',bg = '#00FF00',
                    command = submitde,
                    relief = 'raised',
                    borderwidth=3,
                    activebackground='#00FF00',activeforeground='white')

buttonhelp = tk.Button(window, text = "HELP",
                        font = ("Comic Sans",20,'bold'),
                        fg = 'black',bg = '#00FF00',
                        width = 19,
                        command = help,
                        borderwidth=3,
                        activebackground='black',activeforeground='#00FF00')
buttonhelp.place(x = 0,y = 550)

window.mainloop()
# window end




