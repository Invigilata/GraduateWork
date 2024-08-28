import asyncio
import aiohttp
import time


# Функция для асинхронной загрузки данных с URL
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


# Основная асинхронная функция
async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))

        # Запуск всех задач параллельно и ожидание завершения
        responses = await asyncio.gather(*tasks)
        return responses


# Список URL-адресов для загрузки
urls = [
    'https://example.com',
    'https://httpbin.org/get',
    'https://jsonplaceholder.typicode.com/posts',
] * 50

# Измерение времени выполнения
start_time = time.time()
responses = asyncio.run(main(urls))
end_time = time.time()

# Вывод результата и времени ожидания
for i, response in enumerate(responses):
    print(f"Response from {urls[i]}: {len(response)} characters")

print(f"Total waiting time: {end_time - start_time:.2f} seconds")
