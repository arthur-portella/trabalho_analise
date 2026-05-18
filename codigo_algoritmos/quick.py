"""" 
Algoritmo de ordenação Quick Sort desenvolvido por
André Zanin de Moraes, Arthur Cesar de Oliveira Portella,
Kauã Guimarães Esperança Moreira como parte do 
trabalho 1 da disciplina Análise de Algoritmos.

O algoritmo desenvolvido visa colocar as métricas de tempo de execução, 
número de comparações, número de trocas e pico de memória utilizada para cada um 
dos casos (aleatório, ordenado, inverso e repetido) 
para que seja possível a análise dos resultados.
"""

import time
import tracemalloc  
import random
import codigo_algoritmos.cria_dados as cria_dados

random.seed(42)

# Variáveis globais utilizadas para fazer a contagem do número de comparações e de trocas
comparacao = 0
troca = 0

# Função de partição
def partition(arr, low, high):
    global comparacao
    global troca  

    # Escolhe o pivô aleatoriamente
    pivot_index = random.randint(low, high)

    swap(arr, pivot_index, high)
    troca += 1
    
    pivot = arr[high]

    # Indíce do menor elemento e indica a posição certa do pivô
    i = low - 1
    
    # Atravessa o arr[low..high] e move todos ellementos menores para o lado esquerdo.
    for j in range(low, high):
        comparacao += 1
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)  
            troca += 1
    
    # Move o pivô após os elementos menores e retorna a sua posição
    swap(arr, i + 1, high)
    troca += 1
    return i + 1

# Função que troca posição dos elementos
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Implementação do Quick Sort
def quickSort(arr, low, high):
    if low < high:
        
        # Pi é o índice de retorno da partição do pivô
        pi = partition(arr, low, high)
        
        # Chamadas de recursão para elementos menores e elementos maiores ou iguais
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def printArray(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    # Função que cria o array que será ordenado, você pode escolher o tamanho e a distribuição (aleatorio, ordenado, inverso e repetido)
    arr = cria_dados.retorna_entrada(100000, 'repetido')
    n = len(arr)

    # Inicia o rastreio da memória que é utilizada no programa desconsiderando a memória do vetor de entrada
    tracemalloc.start()
    # Começa a fazer a contagem do tempo de execução do algoritmo
    inicio = time.perf_counter()

    quickSort(arr, 0, n - 1)

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