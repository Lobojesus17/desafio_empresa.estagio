#questão 01

def fibonacci(p):
    a = 0
    b = 1
    fibonacci_sequence = []

    for i in range(p):
        fibonacci_sequence.append(a)
        a, b = b , a + b
 
    return fibonacci_sequence

p = 8

print(fibonacci(p))


# Função para verificar se o número informado pertence à sequência de Fibonacci

def pertence_fibonacci(o):
    
    if o < 0:
        return f"O número {o} não pertence à sequência de Fibonacci."
    
    a = 0 
    b = 1


    while a <= o:
        if a == o:  
            return f"O número {o} pertence à sequência de Fibonacci."
        a, b = b, a + b 

    
    return f"O número {o} não pertence à sequência de Fibonacci."

# if eu informar o número que tem na sequencia ele irá pertencer a sequencia de fibonacci, else, ele exibirá que não pertence à sequencia de fibonacci
numero_informado = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero_informado)
print(resultado)



