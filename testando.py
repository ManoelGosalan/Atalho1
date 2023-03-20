import os
import webbrowser
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Minha Janela Principal")
        self.master.geometry("500x500+700+250")
        
        
        
        self.background_image = Image.open("image\PDV.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = Label(self.master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.open_folder_button = Button(
            self.master, text="Abrir Pasta", command=self.open_folder)
        self.open_folder_button.pack(pady=5)

        self.open_site_button = Button(
            self.master, text="Abrir Site", command=self.open_site)
        self.open_site_button.pack(pady=5)

        self.open_second_window_button = Button(
            self.master, text="Abrir Segunda Janela", command=self.show_second_window)
        self.open_second_window_button.pack(pady=5)

    def open_folder(self):
        folder_path = filedialog.askdirectory()
        os.startfile(folder_path)

    def open_site(self):
        webbrowser.open_new_tab("https://www.google.com")

    def show_second_window(self):
        self.master.withdraw()
        self.new_window = Toplevel(self.master)
        self.app = SecondWindow(self.new_window, self)

    def show(self):
        self.master.deiconify()


class SecondWindow:
    def __init__(self, master, parent):
        self.master = master
        self.master.title("Minha Segunda Janela")
        self.master.geometry("500x500+700+250")

        self.parent = parent
        
        self.background_image = Image.open("image/Suporte.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = Label(self.master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.open_folder_button = Button(
            self.master, text="Abrir Pasta", command=self.open_folder)
        self.open_folder_button.pack(pady=5)

        self.open_site_button = Button(
            self.master, text="Abrir Site", command=self.open_site)
        self.open_site_button.pack(pady=5)

        self.close_button = Button(
            self.master, text="Fechar Janela", command=self.close)
        self.close_button.pack(pady=5)

    def open_folder(self):
        folder_path = filedialog.askdirectory()
        os.startfile(folder_path)

    def open_site(self):
        webbrowser.open_new_tab("https://www.google.com")

    def close(self):
        self.master.withdraw()
        self.parent.show()


root = Tk()
app = MainWindow(root)
root.mainloop()
