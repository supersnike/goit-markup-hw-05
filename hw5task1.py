def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        # Базові випадки: fibonacci(0) = 0, fibonacci(1) = 1
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # Перевірка, чи вже обчислене число знаходиться у кеші
        if n in cache:
            return cache[n]
        # Обчислення числа Фібоначчі для n та збереження результату у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Приклад використання:
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
