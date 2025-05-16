import flet as ft

def main(page: ft.Page):
    # configuração da pagina
    page.title = 'Minha Aplicação Flet'
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de função
    def mostrar_nome(e):  #sempre tem q deixar o e
        txt_resultado.value = input_nome.value +' '+ input_sobrenome.value
        page.update()

    # Criação de componentes
    input_nome = ft.TextField(label='Nome', hint_text='digite seu nome')  # hint_text : exemplo de algo
    input_sobrenome = ft.TextField(label='Sobrenome', hint_text='digite seu sobrenome')
    btn_enviar = ft.FilledButton(text='Enviar',
                                 width=page.window.width,
                                 on_click=mostrar_nome,)
    txt_resultado = ft.Text(value='')

    # Construir o layot
    page.add(
        ft.Column(
            [
                input_nome,
                input_sobrenome,
                btn_enviar,
                txt_resultado,
            ]
        )
    )
ft.app(main)

# ft.TextField(label="Digite um numero:") # no label da pra mudar a cor
