import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from sqlalchemy import select

from models_livro import *

def main(page: ft.Page):
    # Configuração da pagina

    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeModo.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista_usuario = []

    def salvar_usuario(e):

        if  nome.value == "" or profissao.value == "" or salario.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
            print('O campo esta vazio')

        else:
            print('O campo esta preenchido')
            obj_usuario = Usuario (
                nome = nome.value,
                profissao=profissao.value,
                salario=salario.value,
            )
            lista_usuario.append(obj_usuario)
            obj_usuario.save()
            nome.value = ""
            profissao.value = ""
            salario.value = ""

            page.overlay.append(msg_sucesso)
            msg_sucesso.open=True
            page.update()

    def  detalhes_usuario(e):
        # clear é pra apagar o negocio da lista para não repitir
        lv_nome.controls.clear()
        for usuario in lista_usuario:
            lv_nome.controls.append(
                ft.Text(value = f"{usuario.nome} - {usuario.profissao}- {usuario.salario} ")
            )
        page.update()

    def exibir_usuario(e):
        # clear é pra apagar o negocio da lista para não repitir
        lv_nome.controls.clear()
        sql_usuario = select(Usuario).where()
        result = db_session.execute(sql_usuario).scalars()

        for usuario in result:

            lv_nome.controls.append(
                ft.ListTile(
                    title=ft.Text(f"Nome - {usuario.nome}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Vizualizar Detalhes", on_click=lambda _: page.go("/terceira")),
                        ]

                    )
                )
            )
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    nome,
                    profissao,
                    salario,
                    ft.Button(
                        text = "Salvar",
                        on_click=lambda _:  salvar_usuario(e),

                    ),
                    ft.Button(
                        text = "Exibir lista ",
                        on_click=lambda _: page.go("/segunda"),
                    )
                ],
            )
        )
        if page.route == "/segunda":
            exibir_usuario(e)

            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,

                    ],
                )
            )
        page.update()
        if page.route == "/terceira":
            detalhes_usuario(e)
            page.views.append(
                View(
                    "Detalhes de usuario",
                    [
                        lv_nome,
                        ft.Button(
                            text="Exibir livros ", on_click=lambda _: page.go("/segunda"))

                    ]
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("Usuario salvo com sucesso"),
        bgcolor=Colors.GREEN,

    )
    msg_erro = ft.SnackBar(
        content=ft.Text("Preecha o campo"),
        bgcolor=Colors.RED,

    )

    nome=ft.TextField(label='Nome', hint_text='Digite seu nome')
    profissao = ft.TextField(label='Profissão', hint_text='Digite sua Prifissão')
    salario = ft.TextField(label='Salario', hint_text='Digite seu salario')

    lv_nome = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1,
    )

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)