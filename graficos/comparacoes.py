import matplotlib.pyplot as plt

tamanhos_entrada = [1000, 10000, 100000, 1000000]

#comparacao (aleatorio)
insertion_aleatorio = [241840, 25167894, 2504285128, None]
merge_aleatorio = [8660, 120429, 1536559, 18674019]
quick_aleatorio = [10089, 153262, 2121134, 24272989]
heap_aleatorio = [16867, 235381, 3019248, 36792855]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_aleatorio, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_aleatorio, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_aleatorio, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_aleatorio, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Número de comparações')
plt.title('Comparações - Entrada aleatória')
plt.legend()
plt.grid(True)

plt.show()


#comparacao (ordenado)
insertion_ordenado = [999, 9999, 99999, 999999]
merge_ordenado = [5044, 69008, 853904, 10066432]
quick_ordenado = [10259, 153731, 2027044, 24973365]
heap_ordenado = [17583, 244460, 3112517, 37692069]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_ordenado, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_ordenado, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_ordenado, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_ordenado, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Número de comparações')
plt.title('Comparações - Entrada ordenada')
plt.legend()
plt.grid(True)

plt.show()


#comparacao (invertido)
insertion_invertido = [499500, 49995000, 4999950000, None]
merge_invertido = [4932, 64608, 815024, 9884992]
quick_invertido = [10807, 159503, 2110478, 24232608]
heap_invertido = [15965, 226682, 2926640, 36001436]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_invertido, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_invertido, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_invertido, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_invertido, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Número de comparações')
plt.title('Comparações - Entrada invertida')
plt.legend()
plt.grid(True)

plt.show()


#comparacao (repetido)
insertion_repetido = [224185, 22785385, 2275661942, None]
merge_repetido = [8516, 116826, 1487548, 18038332]
quick_repetido = [48868, 4584527, None, None]
heap_repetido = [15990, 220035, 2793289, 33804696]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_repetido, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_repetido, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_repetido, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_repetido, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Número de comparações')
plt.title('Comparações - Entrada repetida')
plt.legend()
plt.grid(True)

plt.show()
