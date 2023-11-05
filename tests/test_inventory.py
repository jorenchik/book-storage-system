import unittest
from unittest.mock import patch, mock_open
from book_inventory.model import Book
from book_inventory.stores import Inventory


class TestInventory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.book_data_1: tuple = ('12345678910', 'title', 'author', 12.22, 1)
        cls.book_data_2: tuple = ('12345678911', 'title2', 'author2', 13.33, 2)
        cls.inventory = Inventory()

    def tearDown(self):
        self.inventory.books = []

    def test_books_creates_a_book(self):
        # Test that create_books_from_dict creates the correct Book objects
        book_data_list = [self.book_data_1]
        self.inventory.create_books_from_dict(book_data_list)
        self.assertIsInstance(self.inventory.books[0], Book,
                              "Should have created an object of a Book class")

    def test_books_creates_multiple_books(self):
        book_data_list = [self.book_data_1, self.book_data_2]
        self.inventory.create_books_from_dict(book_data_list)
        self.assertEqual(len(self.inventory.books), 2)

    def test_books_gives_invalid_arguments_if_too_much(self):
        book_data_list = [['one_argument']]
        self.assertRaises(TypeError, self.inventory.create_books_from_dict,
                          [book_data_list])

    def test_books_gives_invalid_arguments_if_too_little(self):
        book_data_list = [[*self.book_data_1, 'another_argument']]
        self.assertRaises(TypeError, self.inventory.create_books_from_dict,
                          [book_data_list])

    # @patch(
    #     'pathlib.Path.open',
    #     new_callable=mock_open,
    #     read_data=
    #     '{"books": [{"isbn": "1234567890", "title": "Test Book", "author": "Test Author", "price": 9.99, "quantity_in_stock": 5}]}'
    # )
    # def test_load_json_from_storage(self, mock_file):
    #     # Test that load_json_from_storage correctly loads and processes the JSON
    #     self.inventory.load_json_from_storage()
    #     self.assertEqual(len(self.inventory.books), 1)
    #
    # @patch('pathlib.Path.open',
    #        new_callable=mock_open,
    #        read_data='{"books": []}')
    # def test_load_json_from_storage_with_empty_list(self, mock_file):
    #     # Test that load_json_from_storage handles an empty list correctly
    #     self.inventory.load_json_from_storage()
    #     self.assertEqual(len(self.inventory.books), 0)
    #
    # @patch('pathlib.Path.open',
    #        new_callable=mock_open,
    #        read_data='invalid json')
    # def test_load_json_from_storage_with_invalid_json(self, mock_file):
    #     # Test that load_json_from_storage handles invalid JSON correctly
    #     with self.assertRaises(ValueError):
    #         self.inventory.load_json_from_storage()


# if __name__ == '__main__':
#     unittest.main()
