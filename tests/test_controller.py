import unittest
from unittest.mock import patch, mock_open, MagicMock
from book_inventory.model import Book
from book_inventory.stores import Inventory
from book_inventory.controller import BookController


class SearchByArgumentsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.book_controller = BookController()
        cls.book_data: tuple = [('12345678910', 'title', 'author', 12.22, 1),
                                ('12345678911', 'title2', 'author2', 13.33, 2),
                                ('12345678912', 'title3', 'author3', 14.44, 3)]
        cls.books = [
            Book(*cls.book_data[0]),
            Book(*cls.book_data[1]),
            Book(*cls.book_data[2]),
        ]

    def setUp(self):
        self.books = [Book(*book_values) for book_values in self.book_data]

    def test_print_with_a_book_given(self):
        view = MagicMock()
        inventory = MagicMock()
        inventory.books = [self.books[0]]
        self.book_controller.list_books_option(inventory, view)
        view.print_books.assert_called_once_with(inventory.books)

    def test_print_without_books_given(self):
        view = MagicMock()
        inventory = MagicMock()
        inventory.books = []
        self.book_controller.list_books_option(inventory, view)
        view.print_books.assert_called_once_with(inventory.books)

    def test_print_invalid_inventory_supplied(self):
        view = MagicMock()
        inventory = MagicMock(spec=[])
        self.assertRaises(AttributeError,
                          self.book_controller.list_books_option, inventory,
                          view)

    def test_print_invalid_view_supplied(self):
        view = MagicMock(spec=[])
        inventory = MagicMock()
        self.assertRaises(AttributeError,
                          self.book_controller.list_books_option, inventory,
                          view)
