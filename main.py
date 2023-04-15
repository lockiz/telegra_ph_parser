from transliterate import translit
import requests
import socket


def check_internet_connection():
    try:
        socket.create_connection(('www.google.com', 80))
        print("Интернет-соединение доступно")
        return True
    except OSError:
        print("Интернет-соединение недоступно")
    return False


def main(input_keywords):
    domain_url = 'https://telegra.ph/'
    search_keywords = translit(input_keywords.lower(), "ru", reversed=True)

    if check_internet_connection():
        response = requests.get(f'{domain_url}{search_keywords}-01-01')
        print(response.content)


if __name__ == '__main__':
    main('курсы')


