from src.view.functions_menu import FunctionsMenu
import os

class OptionsMenu:
    def __init__(self, functions_menu: FunctionsMenu):
        self.functions_menu = functions_menu

    def display_login_options(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n" + "=" * 50)
            print("📺 SISTEMA DE STREAMING".center(50))
            print("=" * 50)
            print(" 1 │ 👤 Criar Usuário")
            print(" 2 │ 👤 Acessar um usuario")
            print(" 3 │ 🚪 Sair")
            print("=" * 50)

            choice = input("➜ Escolha uma opção: ")

            match choice:
                case "1":
                    self.functions_menu.crate_user()
                case "2":
                    user = self.functions_menu.login_user()
                    if user != "Erro ao fazer login. Verifique suas credenciais.":
                        if user.name == "admin":
                            return (True, user)
                        return (False, user)
                    else:
                        print(f"\n❌ {user}")
                case "3":
                    print("\n👋 Encerrando sistema...")
                    break
                case _:
                    print("\n❌ Opção inválida!")

    def user_menu(self, user):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n" + "=" * 50)
            print(f"📺 SISTEMA DE STREAMING - Usuário: {user.name}".center(50))
            print("=" * 50)
            print(" 1 │ 📋 Listar Todos os videos")
            print(" 2 │ ⚙️  Configurações")
            print(" 3 │ 🚪 Sair")
            print("=" * 50)

            choice = input("➜ Escolha uma opção: ")

            match choice:
                case "1":
                    self.functions_menu.interactive_menu(
                        self.functions_menu.list_all_videos(),
                        title="VÍDEOS",
                        icon="🎥",
                        formatter=lambda video: print(
                            f"🎬 Título     : {video.title}\n"
                            f"📝 Descrição  : {video.description}\n"
                            f"📅 Criado em  : {video.created_at}"
                        )
                    )
                case "2":
                    self.config_user_menu(user)
                case "3":
                    print("\n👋 Encerrando sistema...")
                    break
                case _:
                    print("\n❌ Opção inválida!")
    
    def config_user_menu(self, user):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n" + "=" * 50)
            print(f"⚙️ CONFIGURAÇÕES - Usuário: {user.name}".center(50))
            print("=" * 50)
            print(" 1 │ 🔑 Alterar Senha")
            print(" 2 │ 🗑️  Excluir Usuário")
            print(" 3 │ 🚪 Sair")
            print("=" * 50)

            choice = input("➜ Escolha uma opção: ")

            match choice:
                case "1":
                    self.functions_menu.change_password(user.id)
                case "2":
                    self.functions_menu.delete_user(user.id)
                    break
                case "3":
                    print("\n👋 Encerrando sistema...")
                    break
                case _:
                    print("\n❌ Opção inválida!")

    def admin_menu(self, user):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            title = f"⚙️ ADMIN - Usuário: {user.name}".center(50)
            options = [
                "│ 📋 Listar Todos os usuários",
                "│ 🗑️ Excluir Usuário",
                "│ 🎥 Criar Vídeo",
                "│ 🗑️ Criar Vídeo",
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
