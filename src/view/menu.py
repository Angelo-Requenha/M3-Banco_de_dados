from src.view.options_menu import OptionsMenu

class Menu:
    def __init__(self, options_menu: OptionsMenu):
        self.options_menu = options_menu

    def display_menu(self):
        user = None
        user = self.options_menu.display_login_options()
        if user:
            if user[0] == True:
                self.options_menu.admin_menu(user[1])
            else:
                self.options_menu.user_menu(user[1])
    