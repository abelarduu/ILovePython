from customtkinter import CTk,CTkLabel,CTkImage,CTkButton,set_appearance_mode
from os.path import dirname
from random import randint
from PIL import Image

#Janela Padronizada
class Master(CTk):
    def __init__(self, width= int, height= int, title= str, resizable= bool):
        super().__init__()
        self.minsize(width,height)
        self.title(title)
        self.resizable(resizable,resizable)
        self.iconbitmap(dirname(__file__) +"\\resources/icon.ico")
        set_appearance_mode("Light")

#Elementos da interface
class App:
    def __init__(self, master):
        master.columnconfigure(3, weight=3)
        master.rowconfigure(6, weight=6)
        
        self.lbl=CTkLabel(master, text="Você ama programar em python?")
        self.lbl.grid(row=1, column=2, columnspan=3, pady=5)
        
        img=CTkImage(Image.open(dirname(__file__) +"\\resources/py.png"))
        image=CTkLabel(master,image= img, text=None)
        image.grid(row=2, column=2, columnspan=3, pady=5)
        
        self.btnYes=CTkButton(master, text="Sim", command= master.destroy)
        self.btnNo=CTkButton(master, text="Não", command= lambda :self.btnNo.grid(row=4, column=randint(2,4), pady=5))
        self.btnYes.grid(row=3, column=2, columnspan=3, pady=5)
        self.btnNo.grid(row=4, column=3, pady=5)

##########################################
#Verificação de execução direta do módulo#
##########################################
if __name__ == "__main__":
    master= Master(400,200,"ILovePython", False)
    app= App(master)
    master.mainloop()