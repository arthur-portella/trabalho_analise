import matplotlib.pyplot as plt

tamanhos_entrada = [1000, 10000, 100000, 1000000]

#troca (aleatorio)
insertion_aleatorio = [241845, 25167901, 2504285139, None]
merge_aleatorio = [9976, 133616, 1668928, 19951424]
quick_aleatorio = [6739, 88742, 1219188, 13262783]
heap_aleatorio = [9097, 124140, 1574803, 19047762]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_aleatorio, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_aleatorio, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_aleatorio, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_aleatorio, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Número de trocas/movimentações')
plt.title('Trocas/Movimentações - Entrada aleatória')
plt.legend()
plt.grid(True)

plt.show()


#troca (ordenado)
insertion_ordenado = [999, 9999, 99999, 999999]
merge_ordenado = [9976, 133616, 1668928, 19951424]
quick_ordenado = [6459, 93552, 1167109, 13771049]
heap_ordenado = [9708, 131956, 1650854, 19787792]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_ordenado, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_ordenado, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_ordenado, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_ordenado, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Número de trocas/movimentações')
plt.title('Trocas/Movimentações - Entrada ordenada')
plt.legend()
plt.grid(True)

plt.show()


#troca (invertido)
insertion_invertido = [500499,50004999,5000049999, None]
merge_invertido = [9976, 133616, 1668928, 19951424]
quick_invertido = [6718,101483, 1197577, 13745281]
heap_invertido = [8316, 116696,1497434, 18333408]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_invertido, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_invertido, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_invertido, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_invertido, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Número de trocas/movimentações')
plt.title('Trocas/Movimentações - Entrada invertida')
plt.legend()
plt.grid(True)

plt.show()


#troca (repetido)
insertion_repetido = [224187, 22785387, 2275661944, None]
merge_repetido = [9976, 133616, 1668928, 19951424]
quick_repetido = [4151, 36059, None, None]
heap_repetido = [8422, 113993, 1436132, 17293345]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_repetido, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_repetido, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_repetido, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_repetido, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Número de trocas/movimentações')
plt.title('Trocas/Movimentações - Entrada repetida')
plt.legend()
plt.grid(True)

plt.show()
