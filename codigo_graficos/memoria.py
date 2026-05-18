import matplotlib.pyplot as plt

tamanhos_entrada = [1000, 10000, 100000, 1000000]

#memoria (aleatorio)
insertion_aleatorio = [0.09, 0.06, 0.2, None]
merge_aleatorio = [8.48, 78.98, 782.35, 7813.79]
quick_aleatorio = [2.06, 2.59, 3.56, 3.94]
heap_aleatorio = [0.28, 0.5, 0.72, 0.91]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_aleatorio, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_aleatorio, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_aleatorio, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_aleatorio, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Memória utilizada (KB)')
plt.title('Memória - Entrada aleatória')
plt.legend()
plt.grid(True)

plt.show()


#memoria (ordenado)
insertion_ordenado = [0.12, 0.12, 0.12, 0.12]
merge_ordenado = [8.51, 79.04, 782.38, 7813.82]
quick_ordenado = [2.03, 2.97, 3.47, 3.94]
heap_ordenado = [0.31, 0.56, 0.75, 0.94]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_ordenado, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_ordenado, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_ordenado, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_ordenado, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Memória utilizada (KB)')
plt.title('Memória - Entrada ordenada')
plt.legend()
plt.grid(True)

plt.show()


#memoria (invertido)
insertion_invertido = [0.09, 0.09, 0.20, None]
merge_invertido = [8.48, 79.01, 782.35, 7813.79]
quick_invertido = [2.31, 2.81, 13.38, 3.88]
heap_invertido = [0.28, 0.53, 0.72, 0.91]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_invertido, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_invertido, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_invertido, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_invertido, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Memória utilizada (KB)')
plt.title('Memória - Entrada invertida')
plt.legend()
plt.grid(True)

plt.show()


#memoria (repetido)
insertion_repetido = [0, 0, 0.11, None]
merge_repetido = [8.16, 78.70, 782.04, 7813.48]
quick_repetido = [6.75, 61.72, None, None]
heap_repetido = [0.00, 0.22, 0.41, 0.59]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_repetido, label='Insertion', marker='s')
plt.plot(tamanhos_entrada, merge_repetido, label='Merge', marker='o')
plt.plot(tamanhos_entrada, quick_repetido, label='Quick', marker='D')
plt.plot(tamanhos_entrada, heap_repetido, label='Heap', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Memória utilizada (KB)')
plt.title('Memória - Entrada repetida')
plt.legend()
plt.grid(True)

plt.show()
