
#Etapa-1: Crie uma lista com os nomes de 5 objetos.
objetos = ['mesa', 'cadeira','celular','sofa','televisão','cama']
print('5 tipo de objetos')

#Etapa-2:Adicione mais um objeto ao final da lista.
objetos.append('faca')
print('objeto adicionado')

#Etapa-3:Acesse o objeto que está na 2a posição.
objeto = objetos[2]
print('este mostrando o segundo intem da lista')

#Etapas-4: Remova um objeto da lista.
objetos.remove('cadeira')
print('cadeira removido')

#Etapa-5: Exiba o tamanho da lista.
len(objetos)
print(len(objetos))

#Etapa-6:Mostre todos os itens com um laço for.
for objeto in objetos:
    print(objeto)

#Etapa-7:Verifique se 'cadeira' está na lista. Se sim remova-a, senão adicione.
if 'cadeira' in objetos:
    objetos.remove('cadeira')
    print('cadeira adicionada')
else:
    objetos.append('cadeira')
    print('cadeira removido')

#ETAPA-8: Ordene a lista em ordem alfabética.
objetos.sort()

#Etapa-9:
primeiro = objetos[0]
print('pegar o primeiro numero da lista')

ultimo = objetos[len(objeto)-1]
print('pegar o ultimo numero da lista')

#Etapa-10:Limpe toda a lista
objetos.clear()
print('remover tudo da lista')
