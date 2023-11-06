from controller import BookController


class BookIndexCommand:

    def __init__(self):
        self.book_controller = BookController()

    def execute(self):
        inventory = self.book_controller.inventory
        view = self.book_controller.view
        self.book_controller.index(inventory, view)


class Menu:
    menu_options: dict
    book_controller: BookController

    def __init__(self):
        self.book_controller = BookController()
        self.menu_options = {
            "0": {
                "name": "Exit",
                "function": self.book_controller.exit
            },
            "1": {
                "name": "Add book",
                "function": self.book_controller.create_book
            },
            "2": {
                "name": "Search a book",
                "function": self.book_controller.search_book_by_all_slots
            },
            "3": {
                "name": "Search a book (ISBN)",
                "function": self.book_controller.search_book_by_isbn
            },
            "4": {
                "name": "List books",
                "function": self.book_controller.index,
                "args":
                [self.book_controller.inventory, self.book_controller.view]
            },
            "5": {
                "name": "Delete book",
                "function": self.book_controller.delete_book_by_isbn
            },
            "?": {
                "name": "Help",
                "function": self.print_menu_cli
            },
        }

    def menu_loop(self):
        while True:
            choice = input("> ")
            option: tuple = self.menu_options.get(choice)
            if "args" in option:
                option["function"](*option["args"])
            elif option["name"] == "List books":
                BookIndexCommand().execute()
            else:
                option["function"]()

    def menu_option(self):
        # TODO: choose show behaviour
        self.print_menu_cli(self.menu_options)

    def print_menu_cli(self):
        for key, val in self.menu_options.items():
            print(key, val["name"], sep=": ")
