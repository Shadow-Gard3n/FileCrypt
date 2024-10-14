import tkinter as tk
from cryptography.fernet import Fernet

# key made
key = Fernet.generate_key()
cipher = Fernet(key)
with open('secret.key', 'wb') as key_file:
    key_file.write(key) 
# key made end   

def submiten():
    fileToget = entryaskfile.get()
    fileTosave = entryaskloc.get()
    try:
        with open('secret.key', 'rb') as key_file:
            key = key_file.read()
        cipher = Fernet(key)
        with open(fileToget, 'rb') as f:
            file_data = f.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(fileTosave, 'wb') as f:
            f.write(encrypted_data)
        labelendone.config(text = f'File encrypted successfully in {fileTosave}!')
        labelendone.place(x = 450,y = 480)      
    except Exception as e:
        print(f"Error during encryption: {e}")
    
def submitde():
    fileToget = entryaskfile.get()
    fileTosave = entryaskloc.get()
    try:
        with open('secret.key', 'rb') as key_file:
            key = key_file.read()
        cipher = Fernet(key)
        with open(fileToget, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(fileTosave, 'wb') as f:
            f.write(decrypted_data)
        labeldedone.config(text = f"File decrypted successfully in {fileTosave}")
        labeldedone.place(x = 450,y = 480)    
    except Exception as e:
        print(f"Error during decryption: {e}")

def encryption():
    labelaskfile.place(x = 450,y = 200)
    labelaskloc.place(x = 450,y = 300)
    entryaskfile.place(x = 450,y = 250)
    entryaskloc.place(x = 450, y = 350)
    buttonen.place(x = 560, y = 405)
    labeldedone.place_forget()
    
def decryption():
    labelaskfile.place(x = 450,y = 200)
    labelaskloc.place(x = 450,y = 300)
    entryaskfile.place(x = 450,y = 250)
    entryaskloc.place(x = 450, y = 350)
    buttonde.place(x = 560, y = 405)
    labelendone.place_forget()

# window strt
window = tk.Tk()
icon_image = tk.PhotoImage(file="D:/Tinkercad/extra/1335179.png")
window.iconphoto(True, icon_image)
window.title("GUI")
window.geometry("1920x1080")
window.config(background='black')

label_image = tk.PhotoImage(file="D:/Tinkercad/extra/1335179.png")
label_image = label_image.subsample(50, 50) 


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
                text = "LOGO",
                font = ('Arial',30,'bold'),
                fg = 'black',
                bg='white',
                image = label_image,
                compound='top',
                padx = 30,
                pady = 5,
                )
labellogo.place(x = 50, y = 0)

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
                    text = "Where to save",
                    font = ('Arial',20,'bold'),
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


window.mainloop()
# window end




