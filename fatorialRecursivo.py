#recursividade em python

def fatorial_recursivo(n):
    if n==0:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)
    
    print(fatorial_recursivo(4))

#iteracao em python 

def fatorial_iteracao(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        return resultado
    print(fatorial_iteracao(4))