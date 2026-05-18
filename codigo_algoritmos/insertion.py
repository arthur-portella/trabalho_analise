"""" 
Algoritmo de ordenação Insertion Sort desenvolvido por
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

# Algoritmo Insertion Sort
def insertionSort(arr):
    # Variáveis locais utilizadas para fazer a contagem do número de comparações e de movimentações
    movimentacao = 0 
    comparacao = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
 
        while j >= 0:
            comparacao += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                movimentacao += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
        movimentacao += 1

    # Retorna as variáveis locais
    return comparacao, movimentacao

# Função para printar o vetor de tamanho n
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    # Função que cria o array que será ordenado, você pode escolher o tamanho e a distribuição (aleatorio, ordenado, inverso e repetido)
    arr = cria_dados.retorna_entrada(100000, 'inverso')

    
    # Inicia o rastreio da memória que é utilizada no programa desconsiderando a memória do vetor de entrada
    tracemalloc.start()
    # Começa a fazer a contagem do tempo de execução do algoritmo
    inicio = time.perf_counter()

    comparacao, movimentacao = insertionSort(arr)

    # Para a contagem do tempo de execução do algoritmo
    fim = time.perf_counter()
    
    # Calcula a memória utilizada
    atual, pico = tracemalloc.get_traced_memory()
    # Calcula o tempo de duração do algoritmo
    duracao = fim - inicio

    # Impressão dos resultados
    print(f"Tempo de execução: {duracao:.8f} s")
    print(f"Comparações: {comparacao}")
    print(f"Movimentações: {movimentacao}")
    print(f"Pico de Memória: {pico / 1024:.2f} KB")

    # Termina o rastreio da memória que é utilizada no programa desconsiderando a memória do vetor de entrada
    tracemalloc.stop()