import time
import tracemalloc  

comparacao = 0
troca = 0

# partition function
def partition(arr, low, high):
    global comparacao
    global troca  

    # choose the pivot
    pivot = arr[high]
    
    # index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    
    # traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        comparacao += 1
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)  
            troca += 1
    
    # move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    troca += 1
    return i + 1

# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# the QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def printArray(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [10, 7, 8, 9]
    n = len(arr)

    tracemalloc.start()
    inicio = time.perf_counter()

    quickSort(arr, 0, n - 1)

    fim = time.perf_counter()
    atual, pico = tracemalloc.get_traced_memory()
    duracao = fim - inicio
    
    printArray(arr)
    print(f"Tempo de execução: {duracao:.8f} s")
    print(f"Comparações: {comparacao}")
    print(f"Trocas: {troca}")
    print(f"Pico de Memória: {pico / 1024:.2f} KB")

    tracemalloc.stop()

    # Neste trabalho, a métrica de trocas corresponde à quantidade de operações de troca executadas pelo algoritmo, independentemente de ocorrer alteração efetiva entre posições distintas do vetor.
