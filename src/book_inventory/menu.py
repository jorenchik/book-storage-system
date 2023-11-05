from controller import BookController


class Menu:
    menu_options: dict
    book_controller: BookController

    def __init__(self):
        self.book_controller = BookController()
        self.menu_options = {
            "0": {
                "name": "Exit",
                "function": self.book_controller.exit_option
            },
            "1": {
                "name": "Add book",
                "function": self.book_controller.add_book_option
            },
            "2": {
                "name": "Search a book",
                "function": self.book_controller.search_book_by_arg_option
            },
            "3": {
                "name": "Search a book (ISBN)",
                "function": self.book_controller.search_book_isbn_option
            },
            "4": {
                "name": "List books",
                "function": self.book_controller.list_books_option
            },
            "5": {
                "name": "Delete book",
                "function": self.book_controller.delete_book_option
            },
            "?": {
                "name": "Help",
                "function": self.print_menu_cli
            },
        }

    def menu_loop(self):
        while True:
            option = input("> ")
            print(self.menu_options.get(option)["function"])
            self.menu_options.get(option)["function"]()

    def menu_option(self):
        # TODO: choose show behaviour
        self.print_menu_cli(self.menu_options)

    def print_menu_cli(self):
        for key, val in self.menu_options.items():
            print(key, val["name"], sep=": ")