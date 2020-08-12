import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

#open, save file name
file_name = "mynote.txt"


menu = Menu(root)

def open_file():
    if os.path.isfile(file_name): #if file exist -> True, else -> False
        with open(file_name, "r", encoding = "utf8") as file:
            txt.delete("1.0", END) #clean text widget
            txt.insert(END, file.read()) #write file contents


def save_file():
    with open(file_name, "w", encoding = "utf8") as file:
        file.write(txt.get("1.0", END)) #import everything and save

#add file menu
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "열기(O)", command = open_file)
menu_file.add_command(label = "저장(S)", command = save_file)
menu_file.add_separator()
menu_file.add_command(label = "끝내기(X)", command = root.quit)

menu.add_cascade(label = "파일(F)", menu = menu_file)

#편집, 서식, 보기, 도움말
menu.add_cascade(labe = "편집(E)")
menu.add_cascade(labe = "서식(O)")
menu.add_cascade(labe = "보기(V)")
menu.add_cascade(labe = "도움말(H)")

#scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")

#body field
txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side = "left", fill = "both", expand = True)

scrollbar.config(command = txt.yview)
root.config(menu = menu)
root.mainloop()
