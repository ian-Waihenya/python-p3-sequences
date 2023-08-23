def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibonacci_sequence = [0, 1]

        while len(fibonacci_sequence) < length:
            next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_num)

        print(fibonacci_sequence)

print_fibonacci(0)  # Output: []
print_fibonacci(1)  # Output: [0]
print_fibonacci(9)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
