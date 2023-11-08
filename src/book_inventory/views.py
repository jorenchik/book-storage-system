from typing import Dict
from .models import Book
from tabulate import tabulate
import tkinter as tk
from tkinter.messagebox import showinfo
from tksheet import Sheet
from tkinter import Entry, END


class BookViewCLI:

    def input_book_data(self) -> Dict:
        isbn: str = input("Enter the ISBN:")
        title: str = input("Enter the TITLE:")
        author: str = input("Enter the AUTHOR:")
        price: str = input("Enter the PRICE:")
        quantity_in_stock: str = input("Enter the QUANTITY:")
        return isbn, title, author, price, quantity_in_stock

    def print_books(self, books) -> None:
        table = []
        for i, book in enumerate(books):
            tr = []
            for key in Book.__slots__:
                tr.append(getattr(book, key))
            table.append(tr)

        print(
            tabulate(table,
                     headers=Book.__slots__,
                     tablefmt='psql',
                     showindex=False))


class TkinterWindow:

    def __init__(self):
        self.root = tk.Tk()
        width = 500
        height = 600
        screen_width = self.root.winfo_screenwidth()  # Width of the screen
        screen_height = self.root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, 500, 500))
        self.root.title('Book listing')

        self.add_table()

    def popup_showinfo(self):
        tk.messagebox.showinfo("Info", "Book has been deleted!")

    def open(self) -> None:
        self.root.mainloop()

    def add_table(self) -> None:

        self.button_frame = tk.Frame(self.root, width=600, pady=10)
        self.delete_button = tk.ttk.Button(self.button_frame, text="Delete")
        self.button_showinfo = tk.ttk.Button(self.button_frame,
                                             text="Show Info",
                                             command=self.popup_showinfo)
        self.button_frame.pack()
        self.frame = tk.Frame(self.root, pady=10)
        self.button_showinfo.pack(side=tk.LEFT, padx=10)
        self.delete_button.pack(side=tk.LEFT)

        y_scroll = tk.Scrollbar(self.frame)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll = tk.Scrollbar(self.frame, orient="horizontal")
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree_view = tk.ttk.Treeview(self.frame,
                                         yscrollcommand=y_scroll.set,
                                         xscrollcommand=x_scroll.set,
                                         height=600)

        self.lst = [
            ('1', 'Atr_2', 'Atr_3', 'Atr_4'),
            ('2', 'Atr_2', 'Atr_3', 'Atr_4'),
        ]

        self.tree_view.column("#0", width=0, stretch=tk.NO)

        self.tree_view["columns"] = ("Isbn", "Title", "Author", "Quantity",
                                     "Price")
        for column in self.tree_view["columns"]:
            self.tree_view.column(column, anchor=tk.CENTER, width=140)
        for column in self.tree_view["columns"]:
            self.tree_view.heading(column, text=column, anchor=tk.CENTER)
        for i, value_list in enumerate(self.lst):
            self.tree_view.insert(parent='',
                                  index='end',
                                  iid=i,
                                  text='',
                                  values=value_list)

        self.frame.pack()
        self.tree_view.pack()
        y_scroll.config(command=self.tree_view.yview)
        x_scroll.config(command=self.tree_view.xview)

        self.tree_view.bind('<Button-1>', self.on_item_click)

    def on_item_click(self, event):
        item = self.tree_view.identify('item', event.x, event.y)
        print(self.lst[int(item)])

    def on_frame_configure(self, event):
        # Reset the scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # def on_frame_configure(self, event):
    #     # Set the scrollregion to encompass the inner frame
    #     self.canvas.configure(scrollregion=self.canvas.bbox("all"))


class BookViewGUI:
    pass
