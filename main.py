from backend.cadastro import Cadastra
from backend.login import Login
import flet as ft


def main(page: ft.Page):
    page.title = "Login"
    page.auto_scroll = True

    # Define a função para lidar com o clique no botão "Login"
    def login(e):
        # Define uma função interna para lidar com a validação e entrada do login
        def enter_login(e):
            # Cria uma instância da classe Login
            Usuar_login = Login()
            # Chama a função login_usuario da classe Login para verificar as credenciais
            if Usuar_login.login_usuario(user.value, password.value):
                # Limpa a página atual se o login for bem-sucedido
                page.clean()
                
            # Imprime o nome de usuário e senha para fins de depuração

            
        # Limpa a página atual
        page.clean()
        # Cria campos de entrada para nome de usuário e senha
        user = ft.TextField(label='Usuario', hint_text="@ABCD")
        password = ft.TextField(label='Senha', hint_text="#Password#1234!", password=True)

        # Cria botões para Login e Cadastro
        login_buttons = ft.ElevatedButton(text="Login", on_click=enter_login)
        cadastra_buttons = ft.ElevatedButton(text="Cadastra", on_click=index_cadastra)
        
        # Adiciona os elementos à página usando um Container e um Column para centralização e estilização
        page.add(
            ft.Column(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Row(
                                    [user],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Row(
                                    [password],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Row(
                                    [login_buttons, cadastra_buttons],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        border=ft.border.all(color=ft.colors.BLACK45, width=1),
                        padding=ft.padding.all(125),
                        margin=ft.margin.all(150),
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    # Define a função para lidar com o clique no botão "Cadastra"
    def index_cadastra(e):
        # Define uma função interna para lidar com o processo de cadastro
        def cadastrar(e):
            # Cria uma instância da classe Cadastra
            cadastra = Cadastra(user.value, email.value, password.value, Confirma_password.value)
            # Chama a função cadastra_usuario da classe Cadastra para registrar o usuário
            cadastra.cadastra_usuario()

        # Limpa a página atual
        page.clean()
        # Cria campos de entrada para nome de usuário, email, senha e confirmação de senha
        user = ft.TextField(label='Usuario', hint_text="@ABCD")
        email = ft.TextField(label="email", hint_text="exemplo@gmail.com")
        password = ft.TextField(label='Senha', hint_text="#senh@1233!")
        Confirma_password = ft.TextField(label='confirmar senha', hint_text="#senh@1233!")
        # Cria botões para Login e Cadastro
        login_buttons = ft.ElevatedButton(text="Login", on_click=login)
        cadastra_buttons = ft.ElevatedButton(text="Cadastra", on_click=cadastrar)

        # Adiciona os elementos à página usando um Container e um Column para centralização e estilização
        page.add(
            ft.Container(
                ft.Column(
                    [
                        ft.Row(
                            [user],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [email],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [password],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [Confirma_password],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [
                                login_buttons,
                                cadastra_buttons,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                border=ft.border.all(color=ft.colors.BLACK45, width=1),
                padding=ft.padding.all(125),
                margin=ft.margin.all(100),
                alignment=ft.alignment.center,

            )
        )

    # Chama a função login para renderizar a tela de login inicial
    login(None)


if __name__ == "__main__":
    ft.app(target=main)