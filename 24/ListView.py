import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors


class usuario():
    def __init__(self, nome,salario,profissão):
        self.profissão= profissão
        self.nome = nome
        self.salario = salario


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []
    def salvar_nome(e):

        if  nome.value == "" or profissão.value == "" or salario.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()

        else:
            obj_usuario = usuario (
                nome = nome.value,
                profissão=profissão.value,
                salario=salario.value,
            )
            lista.append(obj_usuario)
            page.overlay.append(msg_sucesso)
            msg_sucesso.open=True
            page.update()

    def  exibir_lista(e):
        # clear é pra apagar o negocio da lista para não repitir
        lv_nome.controls.clear()
        for usuario in lista:
            lv_nome.controls.append(
                ft.Text(value = f"{usuario.nome} - {usuario.profissão}- {usuario.salario} ")
            )
        page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    nome,
                    profissão,
                    salario,
                    ft.Button(
                        text = "Salvar",
                        on_click=lambda _: salvar_nome(e),

                    ),
                    ft.Button(
                        text = "Exibir lista ",
                        on_click=lambda _: page.go("/segunda"),
                    )
                ],
            )
        )
        if page.route == "/segunda":
            exibir_lista(e)

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

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("Nome salvo com sucesso"),
        bgcolor=Colors.GREEN,

    )
    msg_erro = ft.SnackBar(
        content=ft.Text("Preecha o campo"),
        bgcolor=Colors.RED,

    )

    nome=ft.TextField(label='Nome')
    profissão = ft.TextField(label='Profissão')
    salario = ft.TextField(label='Salario')

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