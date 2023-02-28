from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile, askopenfilenames
import os, os.path, time
from tkinter import ttk
from tkinter.messagebox import askyesno


window = Tk()
window.title("Заметки")
window.geometry("440x400+700+300")
window.resizable(False, False)


data_field = Text(width=400, height=3, bd=0.5, bg="#7B68EE", fg="#F0F8FF", font=("Century Gothic", 12, "bold"))
data_field.pack(side="top")
data_field.configure(state="disabled")


text= Text(width=400, height=300, bd=0, bg="#7B68EE", fg="#F0F8FF", font=("Segoe Script", 16, "bold"))
text.pack(side="bottom")


def new_file():
    if text.get("1.0", END) != "\n" and clicked():
        save_as()
        text.delete("1.0", END)
    else:
        text.delete("1.0", END)


def save_as():
    file_path = asksaveasfile(mode="w", defaultextension=".json", initialdir="C:/Users/vgard/OneDrive/Рабочий стол/РАЗРАБОТКА/Python/NotepadProject/Notes", title="Сохранить заметку")
    if file_path != None:
        text_field = text.get("1.0", END)
        with open(file_path.name, "w", encoding="UTF-8") as file:
            file.write(text_field)
    data_field.configure(state="normal")
    data_field.delete("1.0", END)
    data_field.configure(state="disabled")
    text.delete("1.0", END)


def open_file():
    def opn():
        file_path = askopenfilename(initialdir="Notes", title="Список заметок")
        if file_path != "":
            tm = time.ctime(os.path.getmtime(file_path))
            data_field.configure(state="normal")
            data_field.delete("1.0", END)
            data_field.insert("1.0", f"Заметка: {file_path[76:-5]}\nПоследнее изменение:\n{tm}")
            data_field.configure(state="disabled")
            with open(file_path, "r", encoding="UTF-8") as file:
                text_editor=file.read()
                text.delete("1.0", END)
                text.insert("1.0", text_editor)

    if text.get("1.0", END) == "\n":
        opn()
    elif clicked():
        save_as()
        opn()
    else:
        opn()


def delete_file():
    file_path = askopenfilenames(initialdir="Notes", title="Удаление заметок")
    for i in file_path:
        os.remove(i)
    data_field.configure(state="normal")
    data_field.delete("1.0", END)
    data_field.configure(state="disabled")
    text.delete("1.0", END)


def clicked():
    ttk.Button(command=clicked)
    result = askyesno(title="Сохранить заметку?", message="Вы не сохранили заметку, сохранить её?")
    if result: return True
    else: return False


menu_bar = Menu(window)
window.config(menu=menu_bar)

menu_bar.add_command(label="Новая заметка", command=new_file)
menu_bar.add_cascade(label="Открыть заметку", command=open_file)
menu_bar.add_command(label="Сохранить заметку", command=save_as)
menu_bar.add_command(label="Удаление заметок", command=delete_file)


window.mainloop()
