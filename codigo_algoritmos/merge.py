"""" 
Algoritmo de ordenação Merge Sort desenvolvido por
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
import codigo_algoritmos.cria_dados as cria_dados

# Variáveis globais utilizadas para fazer a contagem do número de comparações e de movimentações
comparacao = 0
movimentacao = 0

def merge(arr, left, mid, right):
    global comparacao
    global movimentacao 

    n1 = mid - left + 1
    n2 = right - mid

    # Criando vetores temporários
    L = [0] * n1
    R = [0] * n2

    # Copia os dados para os vetores temporários L[] e R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    # Une os vetores temporários de volta
    # no vetor original arr[left..right]
    while i < n1 and j < n2:
        comparacao += 1
        movimentacao += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1  
        k += 1 # avança o índice do array resultante

    # Copia os elementos restantes de L[],
    # se houver algum
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        movimentacao += 1

    # Copia os elementos restantes de R[],
    # se houver algum
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        movimentacao += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    # Função que cria o array que será ordenado, você pode escolher o tamanho e a distribuição (aleatorio, ordenado, inverso e repetido)
    arr = cria_dados.retorna_entrada(1000000, 'ordenado')

    # Inicia o rastreio da memória que é utilizada no programa desconsiderando a memória do vetor de entrada
    tracemalloc.start()
    # Começa a fazer a contagem do tempo de execução do algoritmo
    inicio = time.perf_counter()
   
    mergeSort(arr, 0, len(arr) - 1)

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