from unittest import TestCase
from book_inventory.menu import Menu
from unittest.mock import MagicMock


class ExecuteOptionTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.menu = Menu()
        cls.commands: list[MagicMock] = [MagicMock(), MagicMock()]

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

    # def test_not_execute_non_existing_option(self):
    #     self.menu.menu_options = {"1": self.option, "2": self.another_option}
    #     self.assertRaises(ValueError, self.menu.execute_option,
    #                       self.another_command)
    #
    # def test_execute_existing_with_args(self):
    #     command: MagicMock = MagicMock()
    #     args = ["arg_1", "arg_2"]
    #     self.menu.menu_options = {
    #         "1": {
    #             "name": "option_name",
    #             "command": self.command,
    #             "args": args
    #         }
    #     }
    #     self.menu.execute_option(self.command)
    #     command.execute.assert_called_once_with(args)
