import threading
import requests
import time

# Функция для загрузки данных с URL
def fetch(url, results, index):
    response = requests.get(url)
    results[index] = len(response.content)

# Основная функция
def main(urls):
    threads = []
    results = [0] * len(urls)  # Инициализация списка для хранения результатов

    # Запуск потоков
    for i, url in enumerate(urls):
        thread = threading.Thread(target=fetch, args=(url, results, i))
        threads.append(thread)
        thread.start()

    # Дожидаемся завершения всех потоков
    for thread in threads:
        thread.join()

    return results

# Список URL-адресов для загрузки
urls = [
    'https://example.com',
    'https://httpbin.org/get',
    'https://jsonplaceholder.typicode.com/posts',
] * 50

# Измерение времени выполнения
start_time = time.time()
responses = main(urls)
end_time = time.time()

# Вывод результата и времени ожидания
for i, response_length in enumerate(responses):
    print(f"Response from {urls[i]}: {response_length} characters")

print(f"Total waiting time: {end_time - start_time:.2f} seconds")
