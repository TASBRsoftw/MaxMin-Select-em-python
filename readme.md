# Algoritmo de Seleção Simultânea de Máximo e Mínimo

Este projeto apresenta uma implementação eficiente do algoritmo MaxMin Select, que identifica simultaneamente os valores máximo e mínimo em uma sequência numérica utilizando a estratégia de divisão e conquista.

## Visão Geral da Solução

O algoritmo desenvolvido otimiza o processo de encontrar extremos em conjuntos de dados, reduzindo significativamente o número de comparações requeridas quando comparado a abordagens convencionais.

### Estrutura do Algoritmo

A implementação em `main.py` segue a seguinte lógica:

```python
def max_min_select(arr, start, end):
    """
    Identifica de forma simultânea os valores máximo e mínimo em um array
    aplicando a metodologia de divisão e conquista.
    
    Parâmetros:
        arr: Lista de elementos numéricos
        start: Índice inicial da segmentação
        end: Índice final da segmentação
    
    Retorna:
        Tupla contendo (valor_mínimo, valor_máximo)
    """
    # Cenário elementar: array unitário
    if start == end:
        return (arr[start], arr[start])
    
    # Cenário elementar: array com dois elementos
    if end == start + 1:
        # Requer apenas uma operação comparativa
        return (arr[start], arr[end]) if arr[start] < arr[end] else (arr[end], arr[start])
    
    # Segmentação do problema: cálculo do ponto central
    mid = (start + end) // 2
    
    # Solução recursiva dos subproblemas
    esq_min, esq_max = max_min_select(arr, start, mid)
    dir_min, dir_max = max_min_select(arr, mid + 1, end)
    
    # Consolidação dos resultados parciais
    # Apenas duas comparações necessárias
    min_global = esq_min if esq_min < dir_min else dir_min
    max_global = esq_max if esq_max > dir_max else dir_max
    
    return (min_global, max_global)

def max_min_select_wrapper(arr):
    """
    Função adaptadora para facilitar a chamada do algoritmo
    e compatibilizar com análise de complexidade.
    """
    if not arr:
        return (None, None)
    
    return max_min_select(arr, 0, len(arr) - 1)
```

### Detalhamento da Implementação

1. **Caso trivial (elemento único)**: Quando há apenas um elemento (linhas 14-15), este representa ambos os extremos.

2. **Caso básico (dois elementos)**: Com dois elementos (linhas 18-20), uma única comparação define a ordem entre mínimo e máximo.

3. **Estratégia de divisão**: O conjunto é particionado recursivamente no ponto médio (linha 23) até alcançar os casos elementares.

4. **Solução recursiva**: Cada metade é processada independentemente (linhas 26-27), retornando seus respectivos pares de extremos.

5. **Fusão de resultados**: A combinação das soluções parciais demanda apenas duas operações comparativas (linhas 30-31) para determinar os valores globais.

## Instruções de Execução

### Requisitos do Sistema
- Interpretador Python versão 3.6 ou superior

### Processo de Execução
1. Obtenha o arquivo `main.py`
2. Execute através do terminal:
   ```bash
   python main.py
   ```

### Exemplo Prático
```python
# Demonstração de utilização
dados = [3, 7, 1, 9, 5, 2, 8, 4, 6]
minimo, maximo = max_min_select(dados, 0, len(dados) - 1)
print(f"Valor mínimo identificado: {minimo}")
print(f"Valor máximo identificado: {maximo}")
```

## Análise de Desempenho

### Avaliação de Complexidade via Contagem de Operações

A arquitetura do algoritmo baseia-se na decomposição recursiva:

1. **Decomposição**: Problemas de dimensão n são fragmentados em dois subproblemas de tamanho n/2.
2. **Agregação**: A fusão dos resultados consome exatamente 2 comparações.

A relação de recorrência para operações comparativas T(n) é:
```
T(n) = 2T(n/2) + 2
```

Condições de contorno:
- T(1) = 0 (caso trivial sem comparações)
- T(2) = 1 (caso básico com uma comparação)

Desenvolvimento da recorrência:
```
T(n) = 2T(n/2) + 2
     = 2[2T(n/4) + 2] + 2 = 4T(n/4) + 4 + 2
     = 4[2T(n/8) + 2] + 4 + 2 = 8T(n/8) + 8 + 4 + 2
     = ...
```

Após k iterações (quando n/2^k = 1 ⇒ k = log₂n):
```
T(n) = 2^k T(n/2^k) + 2(2^k - 1)
     = n * T(1) + 2(n - 1)
     = 0 + 2n - 2
```

O total de comparações T(n) = 2n - 2 estabelece uma complexidade temporal linear O(n).

### Avaliação de Complexidade Assintótica via Teorema Mestre

A recorrência característica:
```
T(n) = 2T(n/2) + O(1)
```

1. **Parametrização**:
   - a = 2 (quantidade de subproblemas)
   - b = 2 (fator de redução dimensional)
   - f(n) = O(1) (custo de agregação)

2. **Cálculo logarítmico**:
   - log₂(2) = 1
   - Portanto, p = 1

3. **Classificação do caso**:
   - f(n) = O(1) = O(n^0)
   - Como 0 < 1 (log_b(a) = 1), aplica-se o Caso 1 do Teorema Mestre

4. **Conclusão assintótica**:
   - Segundo o Caso 1: T(n) = Θ(n^log_b(a)) = Θ(n¹) = Θ(n)

Ambas as análises confirmam consistentemente que a complexidade assintótica do algoritmo MaxMin Select é Θ(n), demonstrando sua eficiência computacional.
