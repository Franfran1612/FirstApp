from locale import windows_locale
from tkinter.constants import HORIZONTAL

import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
import datetime
from flet import AppBar, ElevatedButton, Text, View
from flet.core.dropdown import Option
from flet.core.types import MainAxisAlignment, CrossAxisAlignment


def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeModo.DARK
    page.window.width = 375
    page.window.height = 667

    def verifica_aposentadoria(e):
        idade = int(idade_atual.value)
        contribuicao = int(tempo_contribuicao.value)

        try:
            if genero.value == "Masc":
                if categoria_aposentadoria.value == "idade":
                    if idade >= 65 and contribuicao >= 15:
                        txt_resultado.value = f'Você ja pode se aposentar'
                    else:
                        txt_resultado.value = f'você não pode se aposentar'
                else:
                    if contribuicao >= 35:
                        txt_resultado.value = f'Você ja pode se aposentar'


            else:
                if categoria_aposentadoria.value == "idade":
                    if idade >= 62 and contribuicao == 15:
                        txt_resultado.value = f'Você ja pode se aposentar'

                    else:
                        txt_resultado.value = f'você não pode se aposentar'

                else:
                    if contribuicao >= 30:
                        txt_resultado.value = f'Você ja pode se aposentar'


        except ValueError:
            txt_resultado.value = 'Invalido'

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Tela inicial"), bgcolor=Colors.BLACK),
                    ft.Image(src='../img.png'),
                    ElevatedButton(text="Regras", on_click=lambda _: page.go("/Regras")),
                    ElevatedButton(text="Simulação", on_click=lambda _: page.go("/Simulação")),
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                bgcolor=Colors.BLUE,
            )
        )

        if page.route == "/Regras":
            page.views.append(
                View(
                    "/Regras",
                    [
                        AppBar(title=Text("Tela sobre as regras"), bgcolor=Colors.BLACK),
                        Text(value=f'\nAposentadoria por Idade:\n\n'

                                   f'Homens: 65 anos de idade e pelo menos 15 anos de contribuição.\n'
                                   f'Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n\n'
                                   f'\nAposentadoria por Tempo de Contribuição:\n\n'
                                   f'Homens: 35 anos de contribuição.\n'
                                   f'Mulheres: 30 anos de contribuição.\n\n'
                                   f'\nValor Estimado do Benefício:\n\n'
                                   f'O valor da aposentadoria será uma média de 60% Valor Estimado do Benefício: '
                                   f' O valor da aposentadoria será uma média de 60% da média salarial informada,'
                                   f' acrescido de 2% por ano que exceder o tempo mínimode contribuição.'),
                    ],
                    bgcolor=Colors.BLUE,
                )  # INDIGO_500
            )

        elif page.route == "/Simulação":
            page.views.append(
                View(
                    "/Simulação",
                    [
                        AppBar(title=Text("Tela de simulação "), bgcolor=Colors.BLACK),
                        idade_atual,
                        genero,
                        tempo_contribuicao,
                        categoria_aposentadoria,
                        salario,
                        ElevatedButton(text="Enviar", on_click=lambda _: page.go("/Pagina")),
                    ],
                    bgcolor=Colors.BLUE,
                )
            )
        elif page.route == "/Pagina":
            page.views.append(
                View(
                    "/Pagina",
                    [
                        AppBar(title=Text("Resposta"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value=f'Resposta: {idade_atual}'),
                        Text(value=f'Resposta: {tempo_contribuicao}'),
                        Text(value=f'Resposta: {salario}'),
                        Text(value=f'Resposta: {genero}'),
                        Text(value=f'Resposta: {categoria_aposentadoria}'),
                    ]
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    txt_resultado = ft.TextField()
    idade_atual = ft.TextField(label='Idade', hint_text='digite sua idade')
    tempo_contribuicao = ft.TextField(label='Contribuição',
                                      hint_text='digite seu tempo de contribuição')  # hint_text : exemplo de algo
    salario = ft.TextField(label='Salario', hint_text='digite seu Salario')  # hint_text : exemplo de algo
    genero = ft.Dropdown(
        label='Genero',
        width=page.window.width,
        options=[Option(key='Masc', text='Masculino'), Option(key='Fem', text='Feminino')]
    )
    categoria_aposentadoria = ft.Dropdown(
        label='Categoria da Aposentadoria',
        width=page.window.width,
        options=[Option(key='Aposentadoria por Idade', text='Aposentadoria por Idade'),
                 Option(key='Aposentadoria por Tempo de Contribuição', text='Aposentadoria por Tempo de Contribuição')]
    )
    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)
