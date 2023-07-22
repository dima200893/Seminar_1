def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


num_terms = 10
fibonacci_sequence = list(fibonacci_generator(num_terms))
print(fibonacci_sequence)
