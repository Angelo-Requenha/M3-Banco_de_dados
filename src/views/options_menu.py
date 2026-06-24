from src.views.functions_menu import FunctionsMenu
from os import system, name

class OptionsMenu:
    def __init__(self, functions_menu: FunctionsMenu):
        self.functions_menu = functions_menu

    def display_login_options(self):
        while True:
            system('cls' if name == 'nt' else 'clear')
            title ="📺 SISTEMA DE STREAMING".center(50)
            options = [
            " 1 │ 👤 Criar Usuário",
            " 2 │ 👤 Acessar um usuario",
            " 3 │ 🚪 Sair",
            ]

            choice = self.functions_menu.menu_setas(options, title)

            match choice:
                case 0:
                    self.functions_menu.crate_user()
                case 1:
                    user = self.functions_menu.login_user()
                    if user != "Erro ao fazer login. Verifique suas credenciais.":
                        if user.name == "admin":
                            login = (True, user)
                        else:
                            login = (False, user)

                        if login[0] == True:
                            self.admin_menu(login[1])
                        else:
                            self.user_menu(login[1])
                    else:
                        print(f"\n❌ {user}")
                case 2:
                    print("\n👋 Encerrando sistema...")
                    break
                case _:
                    print("\n❌ Opção inválida!")

    def user_menu(self, user):
        while True:
            system('cls' if name == 'nt' else 'clear')
            title = f"📺 SISTEMA DE STREAMING - Usuário: {user.name}".center(50)
            options = [
            " 1 │ 📋 Listar Todos os videos",
            " 2 │ ⚙️  Configurações",
            " 3 │ 🚪 Sair"
            ]

            choice = self.functions_menu.menu_setas(options, title)

            match choice:
                case 0:
                    self.functions_menu.interactive_menu(
                        self.functions_menu.list_all_videos(),
                        title="VÍDEOS",
                        icon="🎥",
                        formatter=lambda video: print(
                            f"🆔 ID         : {video.id}\n"
                            f"🎬 Título     : {video.title}\n"
                            f"📝 Descrição  : {video.description}\n"
                            f"📅 Criado em  : {video.created_at}"
                        )
                    )
                    video_id = input("escolha um video para assistir: ")
                    input("Pressione enter para continuar...")
                case 1:
                    self.config_user_menu(user)
                case 2:
                    print("\n👋 Encerrando sistema...")
                    break
                case _:
                    print("\n❌ Opção inválida!")
    
    def config_user_menu(self, user):
        while True:
            system('cls' if name == 'nt' else 'clear')
            title = f"⚙️ CONFIGURAÇÕES - Usuário: {user.name}".center(50)
            options = [
                " 1 │ 🔑 Alterar Senha",
                " 2 │ 🗑️  Excluir Usuário",
                " 3 │ 🚪 Sair"
            ]

            choice = self.functions_menu.menu_setas(options, title)

            match choice:
                case 0:
                    self.functions_menu.change_password(user.id)
                case 1:
                    self.functions_menu.delete_user(user.id)
                    break
                case 2:
                    print("\n👋 Encerrando sistema...")
                    break
                case _:
                    print("\n❌ Opção inválida!")

    def admin_menu(self, user):
        while True:
            system('cls' if name == 'nt' else 'clear')
            title = f"⚙️ ADMIN - Usuário: {user.name}".center(50)
            options = [
                "│ 📋 Listar Todos os usuários",
                "│ 🗑️  Excluir Usuário",
                "│ 🎥 Criar Vídeo",
                "│ 🗑️  Criar Vídeo",
                "│ 🚪 Sair"
            ]

            choice = self.functions_menu.menu_setas(options, title)

            match choice:
                case 0:
                    self.functions_menu.interactive_menu(
                        self.functions_menu.list_all_users(),
                        title="USUARIOS",
                        icon="🎥",
                        formatter=lambda user: print(
                            f"🆔 ID        : {user.id}\n"
                            f"👤 Nome      : {user.name}\n"
                            f"📧 Email     : {user.email}\n"
                            f"📅 Criado em : {user.created_at}\n"
                        )
                    )
                    id_user_delete = input("Digite o ID do usuario para deletar: ")
                    self.functions_menu.delete_user(id_user_delete)

                    input("Pressione enter para continuar...")
                case 1:
                    self.functions_menu.delete_user_by_admin()
                case 2:
                    self.functions_menu.create_video()
                case 3:
                    self.functions_menu.delete_video()
                case 4:
                    print("\n👋 Encerrando sistema...")
                    break
                case _:
                    print("\n❌ Opção inválida!")
