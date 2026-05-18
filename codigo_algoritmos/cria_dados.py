import random

random.seed(42)

# Função que gera uma lista com tamanho e distribuição de dados específicas
def retorna_entrada(tamanho, tipo):

    # Gera uma lista com 'tamanho' números aleatórios de 0 até o 'tamanho' solicitado
    if tipo == 'aleatorio':
        return [random.randint(0, tamanho) for _ in range(tamanho)]
    
    # Gera uma lista ordenada de 0 até 'tamanho' - 1
    elif tipo == 'ordenado':
        return list(range(tamanho))
    
    # Gera uma lista ordenada de forma inversa de 'tamanho' - 1 até 0
    elif tipo == 'inverso':
        return list(range(tamanho - 1, -1, -1))

    # Gera uma lista com 'tamanho' números aleatórios de 0 a 10
    elif tipo == 'repetido':
        return [random.randint(0, 10) for _ in range(tamanho)]
