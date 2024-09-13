def pertence_fibonacci(num):

    a, b = 0, 1

    if num == 0 or num == 1:
        return f"O número {num} pertence à sequência de Fibonacci."

    while b < num:
        a, b = b, a + b

    if b == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."


numeros_informados = [21, 12, 39]
for numero in numeros_informados:
    print(pertence_fibonacci(numero))
