import asyncio
import aiohttp
from transliterate import translit
import socket
from bs4 import BeautifulSoup


def check_internet_connection():
    try:
        socket.create_connection(('www.google.com', 80))
        print("Интернет-соединение доступно")
        return True
    except OSError:
        print("Интернет-соединение недоступно, подключитесь к сети")
    return False


async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            print(f'Парсим {url}')
            return await response.text()
        else:
            print(f'Ошибка {response.status} на {url}')


async def main(input_keywords, search_words_text='', stop_words_text=''):
    domain_url = 'https://telegra.ph/'
    search_keywords = translit(input_keywords.lower(), "ru", reversed=True)

    if check_internet_connection():
        tasks = []
        async with aiohttp.ClientSession() as session:
            for i in range(1, 1 + 1):
                for j in range(4, 4 + 1):
                    monday = str(i).zfill(2)
                    day = str(j).zfill(2)
                    url = f'{domain_url}{search_keywords}-{monday}-{day}'
                    tasks.append(asyncio.create_task(fetch(session, url)))
                    await asyncio.sleep(0.2)
            responses = await asyncio.gather(*tasks)
            for page in responses:
                if page:
                    soup = BeautifulSoup(page, features="html.parser")
                    link_all = len(soup.find_all('a'))
                    img_all = len(soup.find_all('img'))
                    print(f'Кол-во ссылок: {link_all}, кол-во фоток: {img_all}')


if __name__ == '__main__':
    asyncio.run(main('курсы'))
