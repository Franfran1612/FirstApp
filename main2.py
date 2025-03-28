import flet as ft


def main(page: ft.Page):
     # Configuração da página
     page.title = "Minha Aplicação Flet"
     page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
     page.window.width = 375
     page.window.height = 667

    #Definição de funções
     def numero(e):
         txt_resultado.value = input_numero.value
         page.update()

     def impar_e_par(e):
         valor = input_numero.value
         if int(valor) % 2 == 0:
             txt_resultado.value = "par"
             page.update()
         else:
             txt_resultado.value = "impar"
             page.update()


    #Criação de componentes
     input_numero = ft.TextField(label="Número", hint_text="Digite um número")
     btn_enviar = ft.FilledButton(
         text="Enviar",
         width=page.window.width,
         on_click=impar_e_par,
     )
     txt_resultado = ft.Text(value="")
    #Construir o layout
     page.add(
          ft.Column(
               [
                    input_numero,
                    txt_resultado,
                    btn_enviar,

               ]
          )
     )
ft.app(main)