from src.views.options_menu import OptionsMenu

class Menu:
    def __init__(self, options_menu: OptionsMenu):
        self.options_menu = options_menu

    def display_menu(self):
        self.options_menu.display_login_options()
