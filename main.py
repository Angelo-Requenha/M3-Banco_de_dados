from create_db.create_db import create_db
from src.services.video_service import VideoService
from src.services.user_service import UserService
from src.services.history_service import HistoryService
from src.view.menu import Menu
from src.view.options_menu import OptionsMenu
from src.view.functions_menu import FunctionsMenu

if __name__ == "__main__":
    try:
        create_db()

    except Exception as e:
        print(f"Error occurred: {e}")

    video_service_instance = VideoService()
    history_service_instance = HistoryService()
    user_service_instance = UserService()
    function_menu_instance = FunctionsMenu(user_service_instance, video_service_instance, history_service_instance)
    option_menu_instance = OptionsMenu(function_menu_instance)
    menu = Menu(option_menu_instance)
    menu.display_menu()
