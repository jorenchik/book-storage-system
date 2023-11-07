from unittest import TestCase
from book_inventory.menu import Menu
from unittest.mock import MagicMock
from book_inventory.commands import Command


class ExecuteOptionTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.menu = Menu()
        cls.commands: list[MagicMock] = [Command(), Command()]
        cls.commands[0].execute = MagicMock()

    def test_execute_existing_option(self):
        self.menu.menu_options: dict[MagicMock] = {
            "0": self.commands[0],
        }
        self.menu.execute_option("0")
        self.commands[0].execute.assert_called_once()

    def test_raise_value_error_if_no_such_option_exists(self):
        self.menu.menu_options: dict[MagicMock] = {
            "0": self.commands[0],
        }
        self.assertRaises(ValueError, self.menu.execute_option,
                          "non_existing_option")

    def test_execute_function_if_option_is_not_command(self):
        foo = MagicMock(return_value="True")
        self.menu.menu_options: dict[MagicMock] = {
            "0": foo,
        }
        self.menu.execute_option("0")
        foo.assert_called_once()
