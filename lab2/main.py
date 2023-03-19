from tkinter import filedialog
import tkinter as tk
import re


class DeleteWindow(tk.Toplevel):
    text: tk.Text

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Знищити")
        self.geometry("300x200")

        mask_frame = tk.Frame(self)
        mask_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        tk.Label(mask_frame, text="Текст пошуку:").grid(
            row=0, column=0, sticky=tk.W)
        self.mask_entry = tk.Entry(mask_frame)
        self.mask_entry.grid(row=0, column=1, sticky=tk.W + tk.E)

        options_frame = tk.Frame(self)
        options_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        self.start_position = tk.StringVar()
        self.start_position.set('start')

        start_frame = tk.Frame(options_frame)
        start_frame.grid(row=0, column=0, sticky=tk.W)

        tk.Radiobutton(start_frame, text="З початку",
                       variable=self.start_position, value='start').pack(side=tk.TOP)
        tk.Radiobutton(start_frame, text="З курсора",
                       variable=self.start_position, value='cursor').pack(side=tk.TOP)

        buttons_frame = tk.Frame(options_frame)
        buttons_frame.grid(row=0, column=1, sticky=tk.W)

        delete_button = tk.Button(
            buttons_frame, text="Знищити", command=self.delete_word)
        delete_button.pack(side="top")
        delete_all_button = tk.Button(
            buttons_frame, text="Знищити все", command=self.delete_words)
        delete_all_button.pack(side="top")
        close_button = tk.Button(
            buttons_frame, text="Закрити вікно", command=self.destroy)
        close_button.pack(side="top")

    def replace_mask(self, mask):
        mask = self.mask_entry.get()
        pattern = r"\{(\w),\s*(\d)\}"

        def replace(match):
            letter = match.group(1)
            digit = int(match.group(2))
            return letter * digit

        return re.sub(pattern, replace, mask) if mask else None

    def get_index(self):
        start_index = "1.0"
        match self.start_position.get():
            case 'start':
                start_index = "1.0"
            case 'cursor':
                start_index = self.text.index("insert")
        return start_index

    def delete_word(self):
        word = self.replace_mask(self.mask_entry.get())

        if word:
            start_index = self.get_index()
            word_index = self.text.search(fr"\m{re.escape(word)}\M",
                                          start_index, stopindex="end",
                                          regexp=True)
            print(word_index)
            if word_index:
                end_index = f"{word_index}+{len(word)}c"
                self.text.delete(word_index, end_index)

    def delete_words(self):
        word = self.replace_mask(self.mask_entry.get())

        if word:
            start_index = self.get_index()
            while True:
                start_index =  self.text.search(fr"\m{re.escape(word)}\M",
                                          start_index, stopindex="end",
                                          regexp=True)
                if not start_index:
                    break
                end_index = f"{start_index}+{len(word)}c"
                self.text.delete(start_index, end_index)


class TextEditor(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.text = tk.Text(self)
        self.text.pack(fill="both", expand=True)

        self.menu = tk.Menu(self)
        self.menu.add_command(label="Відкрити файл", command=self.open_file)
        self.menu.add_command(label="Знищити", command=self.open_delete_window)
        self.master.config(menu=self.menu)

    def open_delete_window(self):
        delete_window = DeleteWindow(self)
        delete_window.text = self.text
        delete_window.focus_set()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Текстові файли", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                file_content = f.read()
                self.text.delete("1.0", "end")
                self.text.insert("1.0", file_content)


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    editor.pack(fill="both", expand=True)
    root.mainloop()
