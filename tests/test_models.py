import unittest
from book_inventory.model import Book, Inventory
from unittest.mock import MagicMock
from copy import deepcopy


class CreateFromDictTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.book_data = [('12345678910', 'title', 'author', 12.22, 1),
                         ('12345678911', 'title2', 'author2', 13.33, 2)]
        cls.book_model = Book
        cls.inventory = Inventory()
        cls.books = []

    def setUp(self):
        self.books = [Book(*book_data) for book_data in self.book_data]
        self.inventory.books = []
        self.book_dicts = []
        for book in self.books:
            book_dict = {}
            for key in self.book_model.__slots__:
                value = getattr(book, key)
                book_dict[key] = value
            self.book_dicts.append(book_dict)

    def test_books_creates_a_book(self):
        book_dict = self.book_dicts[0]
        resulting_book = self.book_model.create_book_from_dict(book_dict)
        self.assertIsInstance(resulting_book, Book,
                              "Should have created an object of a Book class")

    def test_books_type_error_if_dict_doesnt_match_slots(self):
        book_dict = {"doesnt match": "doesnt match"}
        self.assertRaises(TypeError, self.book_model.create_book_from_dict,
                          book_dict)


class CreateFromListTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.book_data = [('12345678910', 'title', 'author', 12.22, 1),
                         ('12345678911', 'title2', 'author2', 13.33, 2)]
        cls.book_model = Book
        cls.inventory = Inventory()
        cls.books = []

    def test_books_gives_invalid_arguments_if_too_little(self):
        book_data_lists = ('one_argument')
        self.assertRaises(TypeError, Book.create_book_from_list,
                          book_data_lists)

    def test_books_gives_invalid_arguments_if_too_much(self):
        book_data_list = ('12345678910', 'title', 'author', 12.22, 1, 2)
        self.assertRaises(TypeError, Book.create_book_from_list,
                          book_data_list)

    def test_books_creates_a_book(self):
        book_data_list = ('12345678910', 'title', 'author', 12.22, 1)
        resulting_book = self.book_model.create_book_from_list(book_data_list)
        self.assertIsInstance(resulting_book, Book,
                              "Should have created an object of a Book class")


class AddBookToInventoryTest(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.inventory.books = []
        self.books = [MagicMock(spec=Book)]

    def test_creates_one_book_from_list(self):
        self.inventory.add_book_to_inventory(self.books[0])
        self.assertEqual(len(self.inventory.books), 1,
                         "Should have created 1 book")

    def test_throws_type_error_if_argument_is_not_a_book(self):
        self.inventory.add_book_to_inventory(self.books[0])
        self.assertRaises(TypeError, self.inventory.add_book_to_inventory,
                          "not a book")


# def test_creates_multiple_books_from_list(self):
#     book_data_lists = [self.book_data[0], self.book_data[1]]
#     results = self.book_model.create_books_from_list(book_data_lists)
#     self.assertEqual(len(results), 2, "Should have created 2 books")
#
# def test_creates_no_books_from_empty_list(self):
#     book_data_lists = []
#     results = self.book_model.create_books_from_list(book_data_lists)
#     self.assertEqual(len(results), 0, "Should have created 0 books")
#
# def test_books_creates_multiple_books(self):
#     book_dicts = [self.book_dicts[0], self.book_dicts[1]]
#     self.book_model.create_books_from_dict(book_dicts)
#     self.assertEqual(len(self.inventory.books), 2)


class BookDeletionTestCase(unittest.TestCase):

    def setUp(self):
        self.book_model = Inventory()
        self.book_model.books = [MagicMock(), MagicMock()]
        self.book_model.books[0].isbn = "1111"
        self.book_model.books[1].isbn = "2222"

    def test_deletes_existing_book_that_succeeds(self):
        self.book_model.delete("1111")
        self.assertEqual(len(self.book_model.books), 1)

    def test_book_not_found(self):
        self.assertRaises(ValueError, self.book_model.delete, "3333")

    def test_gives_value_error_if_multiple_books_were_found(self):
        self.book_model.books[1].isbn = "111111"
        self.assertRaises(ValueError, self.book_model.delete, "1111")


class FindOneTest(unittest.TestCase):

    def setUp(self):
        self.book_model = Inventory()
        self.book_model.books = [MagicMock(), MagicMock()]
        self.book_model.books[0].isbn = "1111"
        self.book_model.books[1].isbn = "2222"

    def test_finds_one_existing_book(self):
        result = self.book_model.find_one_book("1111", ["isbn"])
        self.assertEqual(result, self.book_model.books[0])

    def test_raises_value_error_if_not_found(self):
        self.assertRaises(ValueError, self.book_model.find_one_book, "3333",
                          ["isbn"])

    def test_raises_value_error_if_found_more_then_one(self):
        self.book_model.books[0].isbn = "1111"
        self.book_model.books[1].isbn = "111111"
        self.assertRaises(ValueError, self.book_model.find_one_book, "1111",
                          ["isbn"])


class CheckIsbnUniqueTest(unittest.TestCase):

    def setUp(self):
        self.book_model = Inventory()
        self.book_model.books = [MagicMock()]
        self.book_model.books[0].isbn = "1111"

    def test_isbn_is_unique(self):
        result = self.book_model.check_unique_isbn("2222")
        self.assertTrue(result)

    def test_isbn_is_not_unique(self):
        result = self.book_model.check_unique_isbn("1111")
        self.assertFalse(result)

    def test_raises_type_error_if_not_string(self):
        self.assertRaises(TypeError, self.book_model.check_unique_isbn, 22)


class UpdateBookTest(unittest.TestCase):

    def setUp(self):
        self.book_model = Inventory()
        self.book_model.books = [MagicMock()]
        self.book_model.books[0].isbn = "1111"
        self.book_model.books[0].title = "title"

    def test_finds_and_updates_whole_model(self):
        new_book = deepcopy(self.book_model.books[0])
        new_book.title = "new_title"
        self.book_model.update("1111", new_book)
        self.assertEqual(self.book_model.books[0].title, "new_title")

    def test_raises_value_error_if_book_is_not_found(self):
        new_book = deepcopy(self.book_model.books[0])
        new_book.title = "new_title"
        self.assertRaises(ValueError, self.book_model.update, "3333", new_book)


class SearchBooksTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
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

    def test_search_book_by_one_attribute(self):
        results = Book.search_by_attributes("10",
                                            [self.books[0], self.books[1]],
                                            ["isbn"])
        self.assertEqual(results, [self.books[0]])

    def test_search_book_by_two_attributes(self):
        self.books[0].title = "unique_string"
        self.books[1].title = self.books[0].title

        results = Book.search_by_attributes(
            "unique_string", [self.books[0], self.books[1], self.books[2]],
            ["isbn", "title"])
        for res in results:
            print(res.title)
        self.assertEqual(results, [self.books[0], self.books[1]])

    def test_search_book_from_empty_book_list(self):
        books = []
        results = Book.search_by_attributes("any_string", books,
                                            ["isbn", "title"])
        self.assertEqual(
            results, [],
            "Search shouldn't yield any results from and empty list")

    def test_search_book_returns_every_book_if_prompt_is_empty(self):
        results = Book.search_by_attributes("", [self.books[0]],
                                            ["isbn", "title"])
        self.assertEqual(
            results, [self.books[0]],
            "Results of empty search prompt should return every book")

    def test_search_book_raises_attribute_exception_on_non_existing_search_prompt(
            self):
        self.assertRaises(AttributeError, Book.search_by_attributes, "prompt",
                          [self.books[0]], ["non-existing"])
