from unittest import TestCase

from unittest.mock import MagicMock
from book_inventory.views import TkinterWindow


class StartTest(TestCase):

    def setUp(self):
        self.tk_window = TkinterWindow()
        self.tk_window.root = MagicMock()
        self.tk_window.root.mainloop = MagicMock()

    def test_open_calls_mainloop(self):
        self.tk_window.open()
        self.tk_window.root.mainloop.assert_called_once()
