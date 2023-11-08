from .models import Book
import tkinter as tk
from tkinter import ttk
import re
from controllers import BookController
from models import Inventory


def camel_to_sentence(camel_str):
    sentence_str = re.sub(r'_', ' ', camel_str)
    return sentence_str[0].upper() + sentence_str[1:]


class TkinterWindow:

    def __init__(self, width, height):
        self.root = tk.Tk()
        self.set_geometry_center(self.root, width, height)
        self.root.title('Book listing')

        self.deletion_item_index = -1
        self.deletion_item = None
        self.deletion_item_isbn = ""

        self.book_controller = BookController(Inventory())
        self.inventory = Inventory()
        self.add_form_entries = []
        self.get_all_items()
        self.deletion_item = ""

    def get_all_items(self):
        self.index_items = self.book_controller.index()

    def load_items_to_treeview(self):
        pass

    def set_geometry_center(self, target, width, height):
        screen_width = self.root.winfo_screenwidth()  # Width of the screen
        screen_height = self.root.winfo_screenheight()  # Height of the screen
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        target.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def popup_showinfo(self):
        tk.messagebox.showinfo("Info", "Book has been deleted!")

    def open(self) -> None:
        self.add_top_frame()
        self.add_table()
        self.root.mainloop()

    def add_label(self, frame, name, side) -> None:
        label_text_variable = tk.StringVar(frame)
        label_text_variable.set(camel_to_sentence(name))
        label = tk.Label(frame, textvariable=label_text_variable, height=1)
        label.pack(side=side, padx=20)

    def add_entry(self, frame: tk.Frame, name: str) -> tk.Entry:
        self.add_label(frame, name, "top")
        entry = tk.Entry(frame, name=name)
        entry.pack(side="top")

    def add_form(self, parent, entry_names) -> tk.Frame:
        form_frame = tk.Frame(self.top_frame, width=100)
        entry_frame = tk.Frame(self.root, width=600, pady=10)
        for slot in entry_names:
            self.add_form_entries.append(self.add_entry(entry_frame, slot))
        action_frame = tk.Frame(entry_frame)
        self.add_action_button(action_frame,
                               "Delete",
                               self.on_item_delete,
                               side="left")
        self.add_action_button(action_frame,
                               "Add",
                               self.on_item_add,
                               side="left")
        entry_frame.pack()
        action_frame.pack()
        form_frame.pack(side=tk.TOP)
        return form_frame

    def add_action_button(self, parent, text, bind, side="top"):
        delete_button = ttk.Button(parent, text=text)
        delete_button.pack(padx=10, pady=10, side=side)
        delete_button.bind("<Button-1>", bind)

    def create_search_bar(self, parent, text):
        self.add_label(self.action_frame, text, "top")
        search_bar = tk.Entry(parent, width=50)
        search_bar.pack(side="top")
        return search_bar

    def add_top_frame(self) -> None:
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(side=tk.TOP)
        self.top_frame.pack()
        self.add_form(self.top_frame, Book.__slots__)
        self.add_action_frame()

    def add_action_frame(self):
        self.action_frame = tk.Frame(self.top_frame, width=100)
        self.action_frame.pack(side=tk.TOP)

        self.isbn_search_bar = self.create_search_bar(self.action_frame,
                                                      "Search by isbn")

        self.add_action_button(self.action_frame, "Search",
                               self.on_search_by_isbn)

        self.author_or_title_search_bar = self.create_search_bar(
            self.action_frame, "Search but author or title")

        self.add_action_button(self.action_frame, "Search",
                               self.on_search_by_author_or_title)

    def add_table(self):

        self.frame = tk.Frame(self.root, pady=10)
        y_scroll = tk.Scrollbar(self.frame)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll = tk.Scrollbar(self.frame, orient="horizontal")
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree_view = tk.ttk.Treeview(self.frame,
                                         yscrollcommand=y_scroll.set,
                                         xscrollcommand=x_scroll.set,
                                         height=600)

        self.tree_view.column("#0", width=0, stretch=tk.NO)

        self.tree_view["columns"] = ("Isbn", "Title", "Author", "Quantity",
                                     "Price")
        for column in self.tree_view["columns"]:
            self.tree_view.column(column, anchor=tk.CENTER, width=140)
        for column in self.tree_view["columns"]:
            self.tree_view.heading(column, text=column, anchor=tk.CENTER)
        for i, value_list in enumerate(self.index_items):
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

    def on_item_add(self, event):
        print("item add")

    def on_item_delete(self, event):
        if self.deletion_item_index != -1:
            self.tree_view.delete(self.deletion_item_index)
            self.book_controller.delete(self.deletion_item_isbn)

    def on_search_by_isbn(self, event):
        print("search_by_isbn:")
        print(self.isbn_search_bar.get())

    def on_search_by_author_or_title(self, event):
        print("search_author_or_title:")
        print(self.author_or_title_search_bar.get())

    def on_item_click(self, event):
        try:
            item_index = self.tree_view.identify('item', event.x, event.y)
            item = self.tree_view.item(item_index)
            self.deletion_item = item
            self.deletion_item_index = item_index
            self.deletion_item_isbn = item["values"][0]
        except KeyError:
            self.deletion_item = None
            self.deletion_item_index = -1
            self.deletion_item_isbn = ""

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
