def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]


def fib(n):
    if n == 0:
        return 0  # Base case
    if n == 1:
        return 1  # Base case
    return fib(n-1) + fib(n-2)  # Recursive case

def countdown(n):
    if n == 0:
        print('Blastoff...')
        return 
    print(n)
    return countdown(n-1)

print(countdown(5))

