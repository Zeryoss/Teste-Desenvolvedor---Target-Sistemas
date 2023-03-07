res = int(input("Digite o numero: "))

def fibonacci(n):
    sequence = [0, 1]   
    for i in range(2, n + 1):
        sequence.append(sequence[i-1] + sequence[i-2])
    if n in sequence:
        return print('Esse número pertence a sequência de fibonacci')
    else:
        return print('Esse número não pertence a sequência de fibonacci')

fibonacci(res)