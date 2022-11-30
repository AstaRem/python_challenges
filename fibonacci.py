
# Fibonacci

# The Fibonacci sequence is: 1, 1, 2, 3, 5, 8, 13, 21, ...

# It is calculated by making the first two terms 1, and then calculating all new terms by adding the previous two together.

# Write a function that calculates the correct number in the sequence for a given location. For example, fib(0) should be 1, as should fib(1). fib(5) should be 8.

fib_sequence = [1, 1]


def fibonacci_value(num):
    for i in range(0, num-1):
        new_fib = fib_sequence[i] + fib_sequence[i+1]
        fib_sequence.append(new_fib)
    print(fib_sequence)
    print(new_fib)
        
fibonacci_value(3)