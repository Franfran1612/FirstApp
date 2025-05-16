import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.view import View

class livro():
    def __init__(self,titulo_livro,descricao,categoria ,autor):
        self.titulo_livro = titulo_livro
        self.descricao = descricao
        self.categoria = categoria
        self.autor = autor


def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeModo.DARK
    page.window.width = 375
    page.window.height = 667

    livro= []
    def salvar_livro(e):

        if titulo_livro.value == "" or descricao.value == "" or categoria.value == "" or autor.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()

        else:
            obj_livro = livros(
                titulo_livro=titulo_livro.value,
                descricao=descricao.value,
                categoria=categoria.value,
                autor=autor.value,
            )
            livro.append(obj_livro)
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        # clear é pra apagar o negocio da lista para não repitir
        lv_nome.controls.clear()
        for livros in livro:
            lv_nome.controls.append(
                ft.Text(value=f"{livros.titulo_livro} - {livros.descricao} - {livros.categoria} - {livros.autor}")
            )
        page.update()

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    titulo_livro,
                    descricao,
                    categoria,
                    autor,
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda")),
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "segunda",
                    [
                        AppBar(title=Text("segunda tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value=f'Titulo "{titulo_livro.value}"'),
                        Text(value=f'descrição "{descricao.value}"'),
                        Text(value=f'Categoria"{categoria.value}"'),
                        Text(value=f'Autor "{autor.value}"'),
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
        content=ft.Text("Livro salvo com sucesso"),
        bgcolor=Colors.GREEN,

    )
    msg_erro = ft.SnackBar(
        content=ft.Text("Preecha o campo"),
        bgcolor=Colors.RED,

    )

    titulo_livro=ft.TextField(label='Titulo do livro')
    descricao = ft.TextField(label='Descrição do livro')
    categoria = ft.TextField(label='Categoria do livro')
    autor = ft.TextField(label='Autor do livro')

    lv_nome = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1,
    )

    page.on_route_change = gerenciar_rotas
    page.go(page.route)
    page.on_view_pop = voltar
    titulo_livro = ft.TextField(label='Titulo', hint_text='Digite o titulo do livro')
    descricao = ft.TextField(label='Descrição', hint_text='Digite a descrição')
    categoria = ft.TextField(label='Categoria', hint_text='Digite a categoria')
    autor = ft.TextField(label='Autor', hint_text='Digite o nome do Autor')# hint_text : exemplo de algo



ft.app(main)
