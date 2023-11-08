from unittest import TestCase
from unittest.mock import MagicMock
from book_inventory.commands import IndexBooksCommand, CreateBookCommand, DeleteBookCommand
from book_inventory.controllers import BookController


class IndexBooksTest(TestCase):

    def setUp(self):
        self.controller = MagicMock()
        self.inventory = MagicMock()
        self.view = MagicMock()
        self.command = IndexBooksCommand(self.controller, self.inventory,
                                         self.view)

    def test_existing_command_executes(self):
        self.command.execute()
        self.controller.index.assert_called_once()

    def test_command_raises_type_error_if_no_such_method_exists(self):
        self.command.controller_method_name = "non-existing"
        self.assertRaises(TypeError, self.command.execute())

    def test_command_calls_index_with_view_and_books(self):
        self.command.execute()
        self.controller.index.assert_called_once_with(self.inventory,
                                                      self.view)


class CreateBookCommandTest(TestCase):

    def setUp(self):
        self.controller = MagicMock()
        self.inventory = MagicMock()
        self.command = CreateBookCommand(self.controller, self.inventory)

    def test_command_executes(self):
        self.command.execute()
        self.controller.create_book.assert_called_once()

    def test_command_raises_type_error_if_no_such_method_exists(self):
        self.command.controller_method_name = "non-existing"
        self.assertRaises(
            TypeError,
            self.command.execute(),
        )


class DeleteBookCommandTest(TestCase):

    def setUp(self):
        self.controller = MagicMock()
        self.inventory = MagicMock()
        self.command = DeleteBookCommand(self.controller, self.inventory)

    def test_command_executes(self):
        self.command.execute()
        getattr(self.command.controller,
                self.command.controller_method_name).assert_called_once()

    def test_command_raises_type_error_if_no_such_method_exists(self):
        self.command.controller_method_name = "non-existing"
        self.assertRaises(
            TypeError,
            self.command.execute(),
        )
