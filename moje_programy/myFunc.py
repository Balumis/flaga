content_list = [[2, 8, 9], [1,2,3], [3,5,6]]
#print(content_list[2][2], content_list[0][2])
lista2 = ['wyraz', 'xd', 'marchewka', 'brokół']
def pick_3_element(lista):
    #print(lista)
    element = lista[1]
    print(lista, element)
    return element

lista2.sort(reverse=True, key=pick_3_element)

print((lista2))