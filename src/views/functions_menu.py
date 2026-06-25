import os
import readchar  # leitura de teclas multiplataforma (substitui o msvcrt, que só existe no Windows)
from readchar import key

from src.services.user_service import UserService
from src.services.video_service import VideoService
from src.services.history_service import HistoryService 

class FunctionsMenu:
    def __init__(self, user_service: UserService, video_service: VideoService, history_service: HistoryService):
        self.user_service = user_service
        self.video_service = video_service
        self.history_service = history_service

    def crate_user(self):
        name = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        password = input("Digite a senha do usuário: ")
        self.user_service.create_user(name, email, password)

    def login_user(self):
        email = input("Digite o email do usuário: ")
        password = input("Digite a senha do usuário: ")
        user = self.user_service.login_user(email, password)
        if user:
            return user
        else:
            return "Erro ao fazer login. Verifique suas credenciais."

    def create_video(self):
        title = input("Digite o título do vídeo: ")
        description = input("Digite a descrição do vídeo: ")
        category = input("Digite a categoria do vídeo: ")
        url = input("Digite a URL do vídeo: ")
        self.video_service.create_video(title, description, category, url)

    def delete_user(self, user_id):
        self.user_service.delete_user_by_id(user_id)
    
    def change_password(self, user_id):
        new_password = input("Digite a nova senha: ")
        self.user_service.change_user_password(user_id, new_password)

    def delete_video(self):
        video_id = int(input("Digite o ID do vídeo a ser excluído: "))
        self.video_service.delete_video_by_id(video_id)

    def list_all_videos(self):
        videos = self.video_service.get_all_videos()
        if videos:
            return videos
        else:
            return "Nenhum vídeo encontrado."
        
    def list_all_users(self):
        users = self.user_service.get_all_users()
        if users:
            return users
        else:
            return "Nenhum usuário encontrado."
        
    def interactive_menu(self, items, title: str, icon: str, formatter):
        os.system('cls' if os.name == 'nt' else 'clear')

        if not items or isinstance(items, str):
            print("\n" + "=" * 50)
            print(f"📭 Nenhum {title.lower()} encontrado.")
            print("=" * 50)
        else:
            print("\n" + "=" * 50)
            print(f"{icon} LISTA DE {title}".center(50))
            print("=" * 50)

            for i, item in enumerate(items, start=1):
                print(f"\n🔢 {title[:-1]} #{i}".center(50))
                print("-" * 50)
                formatter(item)
                print("-" * 50)

    def menu_setas(self, opcoes, title: str):
        selecionado = 0

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f"\n{title}".center(50))
            print("=" * 50)
            for i, opcao in enumerate(opcoes):
                prefixo = "➜  " if i == selecionado else "   "
                print(f"{prefixo}{opcao}")
            print("=" * 50)

            tecla = readchar.readkey()

            if tecla == key.UP: # Seta para cima
                selecionado = (selecionado - 1) % len(opcoes)
            elif tecla == key.DOWN: # Seta para baixo
                selecionado = (selecionado + 1) % len(opcoes)
            elif tecla == key.ENTER: # Enter
                return selecionado