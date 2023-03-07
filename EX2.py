res = int(input("Digite o numero"))

def fibonacci(n):
    # Inicializar as duas primeiras posições da sequência
    sequence = [0, 1]
    
    # Construir a sequência até o índice n
    for i in range(2, n + 1):
        # Adicionar a soma dos dois últimos números à sequência
        sequence.append(sequence[i-1] + sequence[i-2])
    
    # Retornar a sequência completa
    if n in sequence:
        return print('Esse nuemro pertence a sequencia de fibonacci')
    else:
        return print('Esse nuemro não pertence a sequencia de fibonacci')

fibonacci(res)