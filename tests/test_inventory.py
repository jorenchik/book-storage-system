import unittest
from unittest.mock import patch, mock_open, MagicMock
from book_inventory.model import Book
from book_inventory.stores import Inventory
from copy import deepcopy


class InventoryCreationTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.book_data = [('12345678910', 'title', 'author', 12.22, 1),
                         ('12345678911', 'title2', 'author2', 13.33, 2)]
        cls.inventory = Inventory()
        cls.books = []

    def setUp(self):
        self.books = [Book(*book_data) for book_data in self.book_data]
        self.inventory.books = []
        self.book_dicts = []
        for book in self.books:
            book_dict = {}
            for key in Book.__slots__:
                value = getattr(book, key)
                book_dict[key] = value
            self.book_dicts.append(book_dict)

    def test_books_creates_a_book(self):
        book_dicts = [self.book_dicts[0]]
        self.inventory.create_books_from_dict(book_dicts)
        self.assertIsInstance(self.inventory.books[0], Book,
                              "Should have created an object of a Book class")

    def test_books_creates_multiple_books(self):
        book_dicts = [self.book_dicts[0], self.book_dicts[1]]
        self.inventory.create_books_from_dict(book_dicts)
        self.assertEqual(len(self.inventory.books), 2)

    def test_books_gives_invalid_arguments_if_too_little(self):
        book_data_lists = [('one_argument')]
        self.assertRaises(TypeError, self.inventory.create_books_from_list,
                          book_data_lists)

    def test_books_gives_invalid_arguments_if_too_much(self):
        book_data = [str(x) for x in range(0, len(Book.__slots__) + 1)]
        book_data_lists = [book_data]
        self.assertRaises(TypeError, self.inventory.create_books_from_list,
                          book_data_lists)

    def test_creates_one_book_from_list(self):
        book_data_lists = [self.book_data[0]]
        self.inventory.create_books_from_list(book_data_lists)
        self.assertEqual(len(self.inventory.books), 1,
                         "Should have created 1 book")

    def test_creates_multiple_books_from_list(self):
        book_data_lists = [self.book_data[0], self.book_data[1]]
        self.inventory.create_books_from_list(book_data_lists)
        self.assertEqual(len(self.inventory.books), 2,
                         "Should have created 2 books")

    def test_creates_no_books_from_empty_list(self):
        book_data_lists = []
        self.inventory.create_books_from_list(book_data_lists)
        self.assertEqual(len(self.inventory.books), 0,
                         "Should have created 0 books")


class BookDeletionTestCase(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.inventory.books = [MagicMock(), MagicMock()]
        self.inventory.books[0].isbn = "1111"
        self.inventory.books[1].isbn = "2222"

    def test_deletes_existing_book_that_succeeds(self):
        self.inventory.delete("1111")
        self.assertEqual(len(self.inventory.books), 1)

    def test_book_not_found(self):
        self.assertRaises(ValueError, self.inventory.delete, "3333")

    def test_gives_value_error_if_multiple_books_were_found(self):
        self.inventory.books[1].isbn = "111111"
        self.assertRaises(ValueError, self.inventory.delete, "1111")


class FindOneTest(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.inventory.books = [MagicMock(), MagicMock()]
        self.inventory.books[0].isbn = "1111"
        self.inventory.books[1].isbn = "2222"

    def test_finds_one_existing_book(self):
        result = self.inventory.find_one_book("1111", ["isbn"])
        self.assertEqual(result, self.inventory.books[0])

    def test_raises_value_error_if_not_found(self):
        self.assertRaises(ValueError, self.inventory.find_one_book, "3333",
                          ["isbn"])

    def test_raises_value_error_if_found_more_then_one(self):
        self.inventory.books[0].isbn = "1111"
        self.inventory.books[1].isbn = "111111"
        self.assertRaises(ValueError, self.inventory.find_one_book, "1111",
                          ["isbn"])


class CheckIsbnUniqueTest(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.inventory.books = [MagicMock()]
        self.inventory.books[0].isbn = "1111"

    def test_isbn_is_unique(self):
        result = self.inventory.check_unique_isbn("2222")
        self.assertTrue(result)

    def test_isbn_is_not_unique(self):
        result = self.inventory.check_unique_isbn("1111")
        self.assertFalse(result)

    def test_raises_type_error_if_not_string(self):
        self.assertRaises(TypeError, self.inventory.check_unique_isbn, 22)


class UpdateBookTest(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.inventory.books = [MagicMock()]
        self.inventory.books[0].isbn = "1111"
        self.inventory.books[0].title = "title"

    def test_finds_and_updates_whole_model(self):
        new_book = deepcopy(self.inventory.books[0])
        new_book.title = "new_title"
        self.inventory.update("1111", new_book)
        self.assertEqual(self.inventory.books[0].title, "new_title")

    def test_raises_value_error_if_book_is_not_found(self):
        new_book = deepcopy(self.inventory.books[0])
        new_book.title = "new_title"
        self.assertRaises(ValueError, self.inventory.update, "3333", new_book)
