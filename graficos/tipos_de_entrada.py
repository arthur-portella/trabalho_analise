import matplotlib.pyplot as plt

tamanhos_entrada = [1000, 10000, 100000, 1000000]

#insertion (tempo de execução)
insertion_aleatorio = [0.090642, 7.997416, 1810.75249, None]
insertion_ordenado = [0.000496, 0.00599, 0.059592, 0.597006]
insertion_inverso = [0.166968, 19.994136, 4161.13717, None]
insertion_repetido = [0.029922, 3.0826, 1104.25276, None]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, insertion_aleatorio, label='Aleatório', marker='s')
plt.plot(tamanhos_entrada, insertion_ordenado, label='Ordenado', marker='o')
plt.plot(tamanhos_entrada, insertion_inverso, label='Invertido', marker='D')
plt.plot(tamanhos_entrada, insertion_repetido, label='Repetido', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo de execução (s)')
plt.title('Tempo de execução - Insertion')
plt.legend()
plt.grid(True)

plt.show()


#merge (tempo de execução)
merge_aleatorio = [0.010649, 0.164204, 2.158827, 26.55476]
merge_ordenado = [0.010252, 0.162393, 2.118334, 26.025026]
merge_inverso = [0.010214, 0.156198, 2.05454, 25.289852]
merge_repetido = [0.007462, 0.132854, 1.85738, 22.935144]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, merge_aleatorio, label='Aleatório', marker='s')
plt.plot(tamanhos_entrada, merge_ordenado, label='Ordenado', marker='o')
plt.plot(tamanhos_entrada, merge_inverso, label='Invertido', marker='D')
plt.plot(tamanhos_entrada, merge_repetido, label='Repetido', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo de execução (s)')
plt.title('Tempo de execução - Merge')
plt.legend()
plt.grid(True)

plt.show()


#quick (tempo de execução)
quick_aleatorio = [0.00693, 0.091784, 1.333012, 15.132496]
quick_ordenado = [0.006216, 0.097778, 1.26296, 15.29898]
quick_inverso = [0.006408, 0.10092, 1.295532, 15.066548]
quick_repetido = [0.018552, 7.50069, None, None]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, quick_aleatorio, label='Aleatório', marker='s')
plt.plot(tamanhos_entrada, quick_ordenado, label='Ordenado', marker='o')
plt.plot(tamanhos_entrada, quick_inverso, label='Invertido', marker='D')
plt.plot(tamanhos_entrada, quick_repetido, label='Repetido', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo de execução (s)')
plt.title('Tempo de execução - Quick')
plt.legend()
plt.grid(True)

plt.show()


#heap (tempo de execução)
heap_aleatorio = [0.007054, 0.106124, 1.50106, 19.47927]
heap_ordenado = [0.007984, 0.121086, 1.587482, 19.942518]
heap_inverso = [0.00653, 0.103792,1.408082, 18.01554]
heap_repetido = [0.002776, 0.060236, 1.015872, 13.019494]

plt.figure(figsize=(10, 5))

plt.plot(tamanhos_entrada, heap_aleatorio, label='Aleatório', marker='s')
plt.plot(tamanhos_entrada, heap_ordenado, label='Ordenado', marker='o')
plt.plot(tamanhos_entrada, quick_inverso, label='Invertido', marker='D')
plt.plot(tamanhos_entrada, heap_repetido, label='Repetido', marker='^')

plt.xscale('log')
plt.yscale('log')

plt.xticks(tamanhos_entrada, ['1e3', '1e4', '1e5', '1e6'])

plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo de execução (s)')
plt.title('Tempo de execução - Heap')
plt.legend()
plt.grid(True)

plt.show()
