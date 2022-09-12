# import tkinter as tk
# import tkinter.ttk as ttk



# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Ttk Notebook")
#         todos = {
#             "Дом": ["Постирать", "Сходить за продуктами"],
#             "Работа": ["Установить Python", "Учить Tkinter", "Разобрать почту"],
#             "Отпуск": ["Отдых!"]
#             }
#         self.notebook = ttk.Notebook(self, width=250, height=100, padding=10)
#         for key, value in todos.items():
#             frame = ttk.Frame(self.notebook)
#             self.notebook.add(frame, text=key, underline=0, sticky=tk.NE + tk.SW)
#             for text in value:
#                 ttk.Label(frame, text=text).pack(anchor=tk.W)
#         self.label = ttk.Label(self)
#         self.notebook.pack()
#         self.label.pack(anchor=tk.W)
#         self.notebook.enable_traversal()
#         self.notebook.bind("<<NotebookTabChanged>>", self.select_tab)

#     def select_tab(self, event):
#         tab_id = self.notebook.select()
#         tab_name = self.notebook.tab(tab_id, "text")
#         text = "Ваш текущий выбор: {}".format(tab_name)       
#         self.label.config(text=text)



# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

import tkinter as tk
from tkinter.filedialog import askopenfilename
 
 
def open_file():
    """Открываем файл для редактирования"""
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Простой текстовый редактор - {filepath}")
 
 
window = tk.Tk()
window.title("Простой текстовый редактор")
 
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
 
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Открыть", command=open_file)
btn_save = tk.Button(fr_buttons, text="Сохранить как...")
 
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
 
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
 
window.mainloop()