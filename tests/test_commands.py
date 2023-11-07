from unittest import TestCase
from unittest.mock import MagicMock
from book_inventory.commands import IndexBooksCommand
from book_inventory.controller import BookController


class IndexBooksTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_command_executes(self):
        controller = MagicMock()
        command = IndexBooksCommand(controller)
        command.execute()
        controller.index.assert_called_once()

    def test_command_raises_type_error_if_no_such_method_exists(self):
        controller = MagicMock()
        command = IndexBooksCommand(controller)
        self.assertRaises(TypeError, command.execute())

    def test_command_calls_index_with_view_and_books(self):
        controller = MagicMock()
        inventory = MagicMock()
        inventory.books = [MagicMock()]
        view = MagicMock()
        command = IndexBooksCommand(controller, inventory, view)
        command.execute()
        controller.index.assert_called_once_with(inventory.books, view)
