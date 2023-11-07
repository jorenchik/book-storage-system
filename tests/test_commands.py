from unittest import TestCase
from unittest.mock import MagicMock
from book_inventory.commands import IndexBooksCommand, CreateBookCommand, DeleteBookCommand
from book_inventory.controller import BookController


class IndexBooksTest(TestCase):

    def test_existing_command_executes(self):
        controller = MagicMock()
        command = IndexBooksCommand(controller)
        command.execute()
        controller.index.assert_called_once()

    def test_command_raises_type_error_if_no_such_method_exists(self):
        controller = MagicMock()
        command = IndexBooksCommand(controller)
        command.controller_method_name = "non-existing"
        self.assertRaises(TypeError, command.execute())

    def test_command_calls_index_with_view_and_books(self):
        controller = MagicMock()
        inventory = MagicMock()
        inventory.books = [MagicMock()]
        view = MagicMock()
        command = IndexBooksCommand(controller, inventory, view)
        command.execute()
        controller.index.assert_called_once_with(inventory, view)


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
