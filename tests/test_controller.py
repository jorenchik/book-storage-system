import unittest
from unittest.mock import patch, mock_open, MagicMock
from book_inventory.model import Book, Inventory
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
        self.book_controller.index(inventory, view)
        view.print_books.assert_called_once_with(inventory.books)

    def test_print_without_books_given(self):
        view = MagicMock()
        inventory = MagicMock()
        inventory.books = []
        self.book_controller.index(inventory, view)
        view.print_books.assert_called_once_with(inventory.books)

    def test_print_invalid_inventory_supplied(self):
        view = MagicMock()
        inventory = MagicMock(spec=[])
        self.assertRaises(AttributeError, self.book_controller.index,
                          inventory, view)

    def test_print_invalid_view_supplied(self):
        view = MagicMock(spec=[])
        inventory = MagicMock()
        self.assertRaises(AttributeError, self.book_controller.index,
                          inventory, view)


class DeleteBookTest(unittest.TestCase):

    def setUp(self):
        self.controller = BookController()
        self.controller.model = MagicMock()
        self.controller.model.delete = MagicMock()

    def test_calls_delete_book(self):
        key = "11111"
        self.controller.delete(key)
        self.controller.model.delete.assert_called_once_with(key)

    def test_raises_value_error_if_deletion_failed(self):
        key = "11111"
        self.controller.model.delete = MagicMock(spec="callable",
                                                 return_value=False)
        self.assertRaises(ValueError, self.controller.delete, key)
