import sys
import re
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    #Парсинг рядка логу.
    parts = re.split(r'\s+', line.strip(), maxsplit=3)
    return {'date': parts[0], 'time': parts[1], 'level': parts[2], 'message': parts[3]}

def load_logs(file_path: str) -> list:
    #Завантаження логів з файлу.
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    #Фільтрація логів за рівнем.
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    #Підрахунок записів за рівнем логування.
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    """Вивід результатів."""
    print("Рівень логування  | Кількість")
    print("------------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count:<10}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Потрібно вказати шлях до файлу логів.")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)

    if len(sys.argv) == 3:
        log_level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, log_level)
        counts = count_logs_by_level(filtered_logs)
    else:
        counts = count_logs_by_level(logs)

    display_log_counts(counts)
