def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:

                lista[i], lista[i+1] = lista[i+1], lista[i]

lista = [9, 4, 2, 4, 8, 5, 7, 6, 3, 9 ]
bubble_sort(lista)
print(lista)