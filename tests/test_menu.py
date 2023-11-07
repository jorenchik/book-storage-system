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

    def test_execute_existing_option_command(self):
        self.menu.menu_options: dict[MagicMock] = {
            "0": self.commands[0],
        }
        self.menu.execute_option("0")
        self.commands[0].execute.assert_called_once()

    def test_execute_existing_option_tuple(self):
        function = MagicMock()
        function_tuple = ("name", function)
        self.menu.menu_options: dict[MagicMock] = {
            "0": function_tuple,
        }
        self.menu.execute_option("0")
        function.assert_called_once()

    def test_raise_value_error_if_no_such_option_exists(self):
        self.menu.menu_options: dict[MagicMock] = {
            "0": self.commands[0],
        }
        self.assertRaises(ValueError, self.menu.execute_option,
                          "non_existing_option")

    def test_raise_type_error_if_the_option_is_not_tuple_or_command(self):
        self.menu.menu_options: dict[MagicMock] = {
            "0": "not_tuple_or_command",
        }
        self.assertRaises(TypeError, self.menu.execute_option, "0")


class GetMenuEntriesTest(TestCase):

    def setUp(self):
        self.commands: list[MagicMock] = [Command(), Command()]
        self.menu = Menu()
        self.commands[0].name = "name_0"
        self.commands[1].name = "name_1"

    def test_get_menu_entries_from_commands(self):
        self.menu.menu_options = {
            "0": self.commands[0],
            "1": self.commands[1],
        }
        menu_entries = self.menu.get_menu_entries()
        self.assertEqual(menu_entries, ["0: name_0", "1: name_1"])

    def test_get_menu_entries_from_function_tuples(self):
        functions = [MagicMock(), MagicMock()]
        self.menu.menu_options = {
            "0": ("name_0", functions[0]),
            "1": ("name_1", functions[1]),
        }
        menu_entries = self.menu.get_menu_entries()
        self.assertEqual(menu_entries, ["0: name_0", "1: name_1"])

    def test_raises_value_error_if_tuple_is_not_appropriate_length(self):
        functions = [MagicMock(), MagicMock()]
        self.menu.menu_options = {
            "0": ("name_0", functions[0], "another_el"),
        }
        self.assertRaises(ValueError, self.menu.get_menu_entries)

    def test_raises_value_error_if_option_is_not_tuple_or_command(self):
        self.menu.menu_options = {
            "0": "not_option_of_command",
        }
        self.assertRaises(TypeError, self.menu.get_menu_entries)
