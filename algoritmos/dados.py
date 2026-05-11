import random

random.seed(42)

def retorna_entrada(tamanho, tipo):

    if tipo == 'aleatorio':
        return [random.randint(0, tamanho) for _ in range(tamanho)]
    
    elif tipo == 'ordenado':
        return list(range(tamanho))
    
    elif tipo == 'inverso':
        return list(range(tamanho - 1, -1, -1))

    elif tipo == 'repetido':
        return [random.randint(0, 10) for _ in range(tamanho)]

# random.shuffle(lista): Embaralha os elementos de uma lista diretamente.
# Para garantir a reprodutibilidade dos experimentos, foi utilizada uma semente fixa no gerador de números aleatórios durante a criação das entradas.

# A medição de memória foi realizada utilizando a biblioteca `tracemalloc` da linguagem Python. O monitoramento foi iniciado após a geração do vetor de entrada, permitindo medir apenas a memória auxiliar utilizada pelos algoritmos durante o processo de ordenação.
