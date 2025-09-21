def max_min_select(arr, start, end):
    """
    Encontra simultaneamente o maior e o menor elemento em um array
    usando a técnica de divisão e conquista.
    
    Args:
        arr: Lista de elementos
        start: Índice inicial do subarray
        end: Índice final do subarray
    
    Returns:
        Tupla (min, max) com os valores mínimo e máximo
    """
    # Caso base: array com um elemento
    if start == end:
        return (arr[start], arr[start])
    
    # Caso base: array com dois elementos
    if end == start + 1:
        # Apenas 1 comparação necessária
        if arr[start] < arr[end]:
            return (arr[start], arr[end])
        else:
            return (arr[end], arr[start])
    
    # Divisão do problema: encontrar o ponto médio
    mid = (start + end) // 2
    
    # Conquista: resolver recursivamente os subproblemas
    left_min, left_max = max_min_select(arr, start, mid)
    right_min, right_max = max_min_select(arr, mid + 1, end)
    
    # Combinação: comparar os resultados dos subproblemas
    # Apenas 2 comparações necessárias
    overall_min = left_min if left_min < right_min else right_min
    overall_max = left_max if left_max > right_max else right_max
    
    return (overall_min, overall_max)

def max_min_select_wrapper(arr):
    """
    Wrapper para a função max_min_select que adapta a entrada e saída
    para ser compatível com a análise de complexidade.
    """
    if len(arr) == 0:
        return (None, None)
    
    result = max_min_select(arr, 0, len(arr) - 1)
    return result

# Exemplos de uso
if __name__ == "__main__":
    # Teste 1: Array com vários elementos
    arr1 = [3, 7, 1, 9, 5, 2, 8, 4, 6]
    min_val1, max_val1 = max_min_select(arr1, 0, len(arr1) - 1)
    print(f"Array 1: {arr1}")
    print(f"Menor elemento: {min_val1}")
    print(f"Maior elemento: {max_val1}")
    print()
    
    # Teste 2: Array com elementos em ordem decrescente
    arr2 = [10, 8, 6, 4, 2, 0]
    min_val2, max_val2 = max_min_select(arr2, 0, len(arr2) - 1)
    print(f"Array 2: {arr2}")
    print(f"Menor elemento: {min_val2}")
    print(f"Maior elemento: {max_val2}")
    print()
    
    # Teste 3: Array com elementos repetidos
    arr3 = [5, 2, 8, 2, 5, 8, 1]
    min_val3, max_val3 = max_min_select(arr3, 0, len(arr3) - 1)
    print(f"Array 3: {arr3}")
    print(f"Menor elemento: {min_val3}")
    print(f"Maior elemento: {max_val3}")
    print()
    
    # Teste 4: Array com um único elemento
    arr4 = [42]
    min_val4, max_val4 = max_min_select(arr4, 0, len(arr4) - 1)
    print(f"Array 4: {arr4}")
    print(f"Menor elemento: {min_val4}")
    print(f"Maior elemento: {max_val4}")
    print()
    
    # Teste 5: Array com dois elementos
    arr5 = [15, 7]
    min_val5, max_val5 = max_min_select(arr5, 0, len(arr5) - 1)
    print(f"Array 5: {arr5}")
    print(f"Menor elemento: {min_val5}")
    print(f"Maior elemento: {max_val5}")
