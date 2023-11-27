import time
import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, master):
        self.master = master
        master.title("Notepad")

        self.text = tk.Text(master)
        self.text.pack()

        self.create_menu()
        self.create_toolbar()

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)

        edit_menu = tk.Menu(menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)

    def create_toolbar(self):
        toolbar = tk.Frame(self.master, bg="gray")
        toolbar.pack(side=tk.TOP, fill=tk.X)

        cut_btn = tk.Button(toolbar, text="Cut", command=self.cut)
        cut_btn.pack(side=tk.LEFT)

        copy_btn = tk.Button(toolbar, text="Copy", command=self.copy)
        copy_btn.pack(side=tk.LEFT)

        paste_btn = tk.Button(toolbar, text="Paste", command=self.paste)
        paste_btn.pack(side=tk.LEFT)

        real_time_clock_btn = tk.Button(toolbar, text="RTC", command=self.real_time_clock)
        real_time_clock_btn.pack(side=tk.RIGHT)

    def new_file(self):
        self.text.delete("1.0", tk.END)

    def open_file(self):
        filepath = filedialog.askopenfilename()
        with open(filepath, 'r') as file:
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, file.read())

    def save_file(self):
        filepath = filedialog.asksaveasfilename()
        with open(filepath, 'w') as file:
            file.write(self.text.get("1.0", tk.END))

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")
    def real_time_clock(self):
        while True:
            current_time = time.strftime("%H:%M:%S")
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, current_time)
            self.master.update()
            time.sleep(1)
root = tk.Tk()
notepad = Notepad(root)
root.mainloop()