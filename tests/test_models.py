import unittest
from book_inventory.model import Book


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
