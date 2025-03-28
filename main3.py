import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def soma(e):
        resultado = int(input_num.value) + int(input_num1.value)
        txt_resultado.value = f'{resultado}'
        page.update()

    def subtracao(e):
        resultado = int(input_num.value) - int(input_num1.value)
        txt_resultado.value = f'{resultado}'

        page.update()

    def dividir(e):
        resultado = int(input_num.value) / int(input_num1.value)
        txt_resultado.value = f'{resultado}'
        page.update()

    def multiplicacao(e):
        resultado = int(input_num.value) * int(input_num1.value)
        txt_resultado.value = f'{resultado}'
        page.update()


    input_num= ft.TextField(label="Número1", hint_text="Digite um número")
    input_num1 = ft.TextField(label="Número2", hint_text="Digite um número")
    btm_mais= ft.FilledButton(
        text="somar",
        width=page.window.width,
        on_click=soma,)
    btm_menos = ft.FilledButton(
        text="subtrai",
        width=page.window.width,
        on_click=subtracao, )
    btm_dividi = ft.FilledButton(
        text="divide",
        width=page.window.width,
        on_click=dividir)
    btm_multiplicacao = ft.FilledButton(
        text="multiplica",
        width=page.window.width,
        on_click=multiplicacao,)

    txt_resultado = ft.Text(value="")
# Construir o layout

    page.add(
          ft.Column(
               [
                   input_num,
                   input_num1,
                   txt_resultado,
                   btm_mais,
                   btm_menos,
                   btm_dividi,
                   btm_multiplicacao,
               ]
          )
    )
ft.app(main)

