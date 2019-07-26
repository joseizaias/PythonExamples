def lista_lista (lista):
    if len(lista) == 0:
        print ('Lista Vazia!!!')
        
    for i in lista:
        print (i)

def add_right_lista (lista, vagao):
    lista.append(vagao)
    return lista

def add_left_lista (lista, vagao):
    lista.insert(0, vagao)
    return lista

def remove_right_lista (lista):
    if len(lista) != 0:
        lista.pop()
        
    return lista

def remove_left_lista (lista):
    if len(lista) != 0:
        lista.pop(0)
        
    return lista

lista = []
comando = 9

while comando != '-1':
    print ('Entre o comando: 1 - lista, 2 add esq, 3 add dir, 4 rem esq, 5 rem dir: ')
    comando = input()

    if comando == '2' or comando == '3':
        print ('Entre com o número do vagão: ')
        vagao = input()

    if comando == '1':
        lista_lista (lista)
        
    if comando == '2':
        lista = add_left_lista(lista, vagao)
        
    if comando == '3':
        lista = add_right_lista(lista, vagao)
        
    if comando == '4':
        lista = remove_left_lista(lista)
        
    if comando == '5':
        lista = remove_right_lista(lista)

print('Fim!!!')
