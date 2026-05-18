"""" 
Algoritmo de ordenação Heap Sort desenvolvido por
André Zanin de Moraes, Arthur Cesar de Oliveira Portella,
Kauã Guimarães Esperança Moreira como parte do 
Trabalho 1 da disciplina Análise de Algoritmos.

O algoritmo desenvolvido visa colocar as métricas de tempo de execução, 
número de comparações, número de trocas e pico de memória utilizada para cada um 
dos casos (aleatório, ordenado, inverso e repetido) 
para que seja possível a análise dos resultados.
"""

import time
import tracemalloc
import codigo_algoritmos.cria_dados as cria_dados

# Variáveis globais utilizadas para fazer a contagem do número de comparações e de trocas
comparacao = 0
troca = 0

# Faz o heapify da sub-árvore que tem como raiz o nó i
def heapify(arr, n, i):
    global comparacao
    global troca

    # Inicializa largest como a raiz
    largest = i

    # Filho da esquerda = 2*i + 1
    l = 2 * i + 1

    # Filho da direita = 2*i + 2
    r = 2 * i + 2

    # Se o filho da esquerda é maior do que a raiz
    if l < n: 
        comparacao += 1
        if arr[l] > arr[largest]:
            largest = l

    # Se o filho da direita é maior que o maior até agora
    if r < n: 
        comparacao += 1
        if arr[r] > arr[largest]:
            largest = r

    # Se o maior não for raiz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        troca += 1

        # Faz o heapify da sub-árvore afetada recursivamente
        heapify(arr, n, largest)

# Função principal que executa o algoritmo
def heapSort(arr):
    global troca

    n = len(arr)

    # Constrói a heap a partir do vetor original
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraçãoo um por um de cada elemento da heap 
    for i in range(n - 1, 0, -1):

        # Move a raiz atual para o fim
        arr[0], arr[i] = arr[i], arr[0]
        troca += 1

        # Chama heapify máximo na heap reduzida
        heapify(arr, i, 0)

# Função para printar o vetor de tamanho n
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    # Função que cria o array que será ordenado, você pode escolher o tamanho e a distribuição (aleatorio, ordenado, inverso e repetido)
    arr = cria_dados.retorna_entrada(1000000, 'repetido')

    # Inicia o rastreio da memória que é utilizada no programa desconsiderando a memória do vetor de entrada
    tracemalloc.start()
    # Começa a fazer a contagem do tempo de execução do algoritmo
    inicio = time.perf_counter()

    heapSort(arr)

    # Para a contagem do tempo de execução do algoritmo
    fim = time.perf_counter()

    # Calcula a memória utilizada
    atual, pico = tracemalloc.get_traced_memory()
    # Calcula o tempo de duração do algoritmo
    duracao = fim - inicio

    # Impressão dos resultados
    print(f"Tempo de execução: {duracao:.8f} s")
    print(f"Comparações: {comparacao}")
    print(f"Trocas: {troca}")
    print(f"Pico de Memória: {pico / 1024:.2f} KB")

    # Termina o rastreio da memória que é utilizada no programa desconsiderando a memória do vetor de entrada
    tracemalloc.stop()