import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.view import View

def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeModo.DARK
    page.window.width = 375
    page.window.height = 667

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Tela inicial"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text="Regras", on_click=lambda _: page.go("/regras")),
                    ElevatedButton(text="Simulação", on_click=lambda _: page.go("/segunda")),
                    ElevatedButton(text="Resultado", on_click=lambda _: page.go("/segunda")),
                ],
            )
        )
        if page.route == "/regras":
            page.views.append(
                View(
                    "segunda",
                    [
                        AppBar(title=Text("segunda tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value=f'\n\n\nAposentadoria por Idade:\n'
                                   
                                   f'Homens: 65 anos de idade e pelo menos 15 anos de contribuição.\n'
                                   f'Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n\n'
                                   f'Aposentadoria por Tempo de Contribuição:\n'
                                   f'Homens: 35 anos de contribuição.\n'
                                   f'Mulheres: 30 anos de contribuição.\n\n'
                                   f'Valor Estimado do Benefício:\n '
                                   f'O valor da aposentadoria será uma média de 60%Valor Estimado do Benefício: O valor da aposentadoria será uma média de 60%da média salarial informada, acrescido de 2% por ano que exceder o tempo mínimode contribuição.'),
                    ],
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerenciar_rotas
    page.go(page.route)
    page.on_view_pop = voltar
    titulo_livro = ft.TextField(label='Titulo', hint_text='Digite o titulo do livro')
    descricao = ft.TextField(label='Descrição', hint_text='Digite a descrição')
    categoria = ft.TextField(label='Categoria', hint_text='Digite a categoria')
    autor = ft.TextField(label='Autor', hint_text='Digite o nome do Autor')# hint_text : exemplo de algo



ft.app(main)