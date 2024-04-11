import tkinter as tk
from tkinter import messagebox, filedialog


class NotepadApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.search_button = None
        self.search_entry = None
        self.search_frame = None
        self.text_field = None
        self.title("Notepad")
        self.geometry('700x700')

        self.view_colors = {
            'dark': {'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'},
            'light': {'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'}
        }

        self.fonts = {'Times New Roman': 'Times New Roman', 'Calibri': 'Calibri', 'Arial': 'Arial'}

        self.create_menu()
        self.create_text_field()
        self.bind("<Control-t>", lambda event: self.fast_change_theme())
        self.bind("<Control-o>", lambda event: self.open_file())
        self.bind("<Control-s>", lambda event: self.save_file())
        self.bind("<Control-x>", lambda event: self.notepad_exit())
        self.bind("<Control-f>", lambda event: self.search())

    def create_menu(self):
        main_menu = tk.Menu(self)
        file_menu = tk.Menu(main_menu, tearoff=0)
        file_menu.add_command(label='Открыть', command=self.open_file)
        file_menu.add_command(label='Сохранить', command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label='Закрыть', command=self.notepad_exit)
        main_menu.add_cascade(label='Файл', menu=file_menu)

        view_menu = tk.Menu(main_menu, tearoff=0)
        theme_menu = tk.Menu(view_menu, tearoff=0)
        theme_menu.add_command(label='Темная', command=lambda: self.change_theme('dark'))
        theme_menu.add_command(label='Светлая', command=lambda: self.change_theme('light'))
        view_menu.add_cascade(label='Тема', menu=theme_menu)

        font_menu = tk.Menu(view_menu, tearoff=0)
        for font in self.fonts:
            font_menu.add_command(label=font, command=lambda f=font: self.change_font(f))
        view_menu.add_cascade(label='Шрифт', menu=font_menu)
        main_menu.add_cascade(label='Вид', menu=view_menu)

        help_menu = tk.Menu(main_menu, tearoff=0)
        help_menu.add_command(label='О программе', command=self.show_info)
        main_menu.add_cascade(label='Справка', menu=help_menu)

        self.config(menu=main_menu)

    def show_info(self):
        info = """
                Notepad

                Команды:
                - Открыть: Ctrl+O
                - Сохранить: Ctrl+S
                - Закрыть: Ctrl+X
                - Изменить тему: Ctrl+T
                - Поиск: Ctrl+F

                Вы также можете изменить тему и шрифт через меню "Вид".

                Автор: Карим Мазитов, Б05-322
                """

        messagebox.showinfo("О программе", info)

    def create_text_field(self):
        frame_text = tk.Frame(self)
        frame_text.pack(fill=tk.BOTH, expand=1, side=tk.BOTTOM)

        self.text_field = tk.Text(frame_text, bg='black', fg='lime', padx=5, pady=5, wrap=tk.WORD, spacing3=5, width=60,
                                  font='Arial', insertbackground='brown', selectbackground='#8D917A')
        self.text_field.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

        scrollbar = tk.Scrollbar(frame_text, command=self.text_field.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.text_field.config(yscrollcommand=scrollbar.set)

        self.search_frame = tk.Frame(self)
        self.search_frame.pack(fill=tk.X, side=tk.TOP)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=20)

        self.search_button = tk.Button(self.search_frame, text="Поиск", command=self.search_word)
        self.search_button.pack(side=tk.LEFT)

        self.search_frame.pack_forget()

    def fast_change_theme(self):
        if self.text_field['bg'] == 'black':
            self.change_theme('light')
        else:
            self.change_theme('dark')

    def change_theme(self, theme):
        colors = self.view_colors[theme]
        self.text_field['bg'] = colors['text_bg']
        self.text_field['fg'] = colors['text_fg']
        self.text_field['insertbackground'] = colors['cursor']
        self.text_field['selectbackground'] = colors['select_bg']

    def change_font(self, font):
        self.text_field['font'] = self.fonts[font]

    def notepad_exit(self):
        answer = messagebox.askokcancel(title='Выход', message='Вы уверены, что хотите выйти?')
        if answer:
            self.destroy()

    def open_file(self):
        file_path = filedialog.askopenfilename(title='Выбор файла',
                                               filetypes=[('Текстовые документы', '*.txt'),
                                                          ('Все файлы', '*.*')])
        if file_path:
            self.text_field.delete('1.0', tk.END)
            self.text_field.insert('1.0', open(file_path, encoding='utf-8').read())

    def save_file(self):
        try:
            file_path = filedialog.asksaveasfilename(filetypes=[('Текстовые документы', '*.txt'),
                                                                ('Все файлы', '*.*')])
            file = open(file_path, 'w', encoding='utf-8')
            text = self.text_field.get('1.0', tk.END)
            file.write(text)
            file.close()
        except:
            messagebox.showerror(title=None, message="Сохранение файла не выполнено!")

    def search_word(self):
        self.text_field.tag_remove("highlight", "1.0", "end")
        word1 = self.search_entry.get()
        self.highlight(word1)
        self.delete_highlight(word1)

    def highlight(self, word):
        if word:
            start_index = "1.0"
            while True:
                start_index = self.text_field.search(word, start_index, stopindex=tk.END)
                if not start_index:
                    break
                end_index = f"{start_index}+{len(word)}c"
                self.text_field.tag_add("highlight", start_index, end_index)
                start_index = end_index

            self.text_field.tag_config("highlight", background="gray", foreground="black")

    def delete_highlight(self, word):
        if word:
            start_index = '1.0'
            while True:
                start_index = self.text_field.search(word, start_index, tk.END)
                if not start_index:
                    break
                end_index = f"{start_index}+{len(word)}c"
                self.text_field.tag_remove("search", start_index, end_index)
                start_index = end_index
            self.text_field.tag_config("search", background="yellow", foreground="black")

    def search(self):
        if self.search_frame.winfo_viewable():
            self.search_frame.pack_forget()
            self.text_field.tag_remove("highlight", "1.0", "end")
        else:
            self.search_frame.pack(fill=tk.X)


if __name__ == "__main__":
    app = NotepadApp()
    app.mainloop()
