from typing import Dict
import controller


if __name__ == "__main__":

    menu_options = {'Exit': controller.exit_option,
                    'Add book': controller.add_book_option,
                    'Search a book': controller.search_book_by_arg_option,
                    'Search a book (ISBN)': controller.search_book_option,
                    'List books': controller.list_books_option,
                    'Delete book': controller.delete_book_option}

    while True:
        controller.menu_option(menu_options)
        option_index = int(input(">"))
        list(menu_options.values())[option_index]()
