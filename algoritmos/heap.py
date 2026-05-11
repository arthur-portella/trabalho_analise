import time
import tracemalloc
import dados

comparacao = 0
troca = 0

# To heapify a subtree rooted with node i
def heapify(arr, n, i):
    global comparacao
    global troca

    # Initialize largest as root
    largest = i

    # left index = 2*i + 1
    l = 2 * i + 1

    # right index = 2*i + 2
    r = 2 * i + 2

    # If left child is larger than root
    if l < n: 
        comparacao += 1
        if arr[l] > arr[largest]:
            largest = l

    # If right child is larger than largest so far
    if r < n: 
        comparacao += 1
        if arr[r] > arr[largest]:
            largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        troca += 1

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

# Main function to do heap sort
def heapSort(arr):
    global troca

    n = len(arr)

    # Build heap (rearrange vector)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):

        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        troca += 1

        # Call max heapify on the reduced heap
        heapify(arr, i, 0)

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = dados.retorna_entrada(1000000, 'repetido')

    tracemalloc.start()
    inicio = time.perf_counter()

    heapSort(arr)

    fim = time.perf_counter()
    atual, pico = tracemalloc.get_traced_memory()
    duracao = fim - inicio

    print(f"Tempo de execução: {duracao:.8f} s")
    print(f"Comparações: {comparacao}")
    print(f"Trocas: {troca}")
    print(f"Pico de Memória: {pico / 1024:.2f} KB")

    tracemalloc.stop()
