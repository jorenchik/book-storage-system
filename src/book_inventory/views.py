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
        self.root.title('Book listing')
        self.root.geometry('500x500+50+50')
        self.root.resizable(False, False)
        self.add_table()

    def open(self) -> None:
        self.root.mainloop()

    def add_table(self) -> None:

        self.button_frame = tk.Frame(self.root, width=600, pady=10)
        self.delete_button = tk.Button(self.button_frame,
                                       text="Delete",
                                       padx=20)
        self.button_frame.pack()
        self.frame = tk.Frame(self.root, width=600, pady=10)
        self.delete_button.pack(side=tk.LEFT)

        game_scroll = tk.Scrollbar(self.frame)
        game_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree_view = tk.ttk.Treeview(self.frame,
                                         yscrollcommand=game_scroll.set,
                                         height=600)

        self.lst = [
            ('1', 'Atr_2', 'Atr_3', 'Atr_4'),
            ('2', 'Atr_2', 'Atr_3', 'Atr_4'),
        ]

        self.tree_view.column("#0", width=0, stretch=tk.NO)

        self.tree_view["columns"] = ("Isbn", "Title", "Author", "Quantity",
                                     "Price")
        for column in self.tree_view["columns"]:
            self.tree_view.column(column, anchor=tk.CENTER, width=80)
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
        game_scroll.config(command=self.tree_view.yview)

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
