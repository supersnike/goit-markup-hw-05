import re
from typing import Callable

def generator_numbers(text: str):
    # Знаходимо всі числа у тексті за допомогою регулярних виразів
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    for number in numbers:
        # Повертаємо кожне знайдене число як генератор
        yield float(number)

def sum_profit(text: str, func: Callable):
    # Знаходимо всі числа у тексті за допомогою генератора func
    numbers_generator = func(text)
    # Підсумовуємо всі числа
    total = sum(numbers_generator)
    return total

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
