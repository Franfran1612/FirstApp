import requests


def exemplo_cep():
    cep = '16708374'
    url = f'https://viacep.com.br/ws/{cep}/json'
    response = requests.get(url)
    if response.status_code == 200:
        dados_cep = response.json()
        print(f'logradouro: {dados_cep["logradouro"]}')
        print(f'bairro: {dados_cep["bairro"]}')
        print(f'localidade: {dados_cep["localidade"]}')
        print(f'ddd: {dados_cep["ddd"]}')
        print(f'regiao: {dados_cep["regiao"]}')
    else:
        print(f'erro :{response.status_code}')

def exemplo_get(id):
    url = f'https://jsonplaceholder.typicode.com/posts/{id}'
    response = requests.get(url)

    if response.status_code == 200:
        dados_get_postagem = response.json()

        print(f'titulo: {dados_get_postagem["title"]}\n')
        print(f'conteudo: {dados_get_postagem["body"]}')
    else:
        print(f'erro :{response.status_code}')
        #no parentece de exeplo eu posso escolhar o numero que eu quero
exemplo_get(4)

def exemplo_post():
    url ='https://jsonplaceholder.typicode.com/posts'

#pode usar do 1 ao 100
    nova_postagem  = {
        'title': 'novo titulo',
        'body': 'novo conteudo',
        'user_Id': 1
    }
    response = requests.post(url, json=nova_postagem)

    if response.status_code == 201:
        dados_post = response.json()
        print(f'titulo: {dados_post["title"]}\n')
        print(f'conteudo: {dados_post["body"]}')

    else:
        print(f'erro :{response.status_code}')
        # no parentece de exeplo eu posso escolhar o numero que eu quero
# exemplo_post()


def exemplo_put(id):
    url=f'https://jsonplaceholder.typicode.com/posts/{id}'

    nova_postagem = {
        'id': id,
        'title': 'novo titulo',
        'body': 'novo conteudo',
        'user_Id': 1
    }
    antes = requests.get(url)
    response = requests.put(url, json=nova_postagem)

    if response.status_code == 200:
        if antes.status_code == 200:
            dados_antes = antes.json()
            print(f'titulo antigo: {dados_antes["title"]}\n')
        else:
            print(f'erro :{response.status_code}')
        dados_postagem = response.json()
        print(f'titulo: {dados_postagem["title"]}\n')
    else:
        print(f'erro :{response.status_code}')

#exemplo_put(1)