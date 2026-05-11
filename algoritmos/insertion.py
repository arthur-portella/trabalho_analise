import time
import tracemalloc
import dados

def insertionSort(arr):
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

    return comparacao, movimentacao

# A utility function to print array of size n
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver method
if __name__ == "__main__":
    arr = dados.retorna_entrada(100000, 'inverso')

    tracemalloc.start()
    inicio = time.perf_counter()

    comparacao, movimentacao = insertionSort(arr)
    
    fim = time.perf_counter()
    atual, pico = tracemalloc.get_traced_memory()
    duracao = fim - inicio

    print(f"Tempo de execução: {duracao:.8f} s")
    print(f"Comparações: {comparacao}")
    print(f"Movimentações: {movimentacao}")
    print(f"Pico de Memória: {pico / 1024:.2f} KB")

    tracemalloc.stop()

# Neste trabalho, a métrica de movimentações corresponde à quantidade de operações de escrita realizadas sobre o vetor durante o processo de ordenação, incluindo deslocamentos de elementos e inserções de chaves.

# O Insertion Sort apresentou desempenho inviável para grandes entradas em ordem inversa, devido à sua complexidade quadrática no pior caso, tornando a execução impraticável para volumes elevados de dados.

