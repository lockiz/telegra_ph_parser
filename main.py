from transliterate import translit
import requests
import socket


def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        print("Интернет-соединение доступно")
    except OSError:
        print("Интернет-соединение недоступно")





if __name__ == '__main__':
    # domain_url = 'https://telegra.ph/'
    #
    # response = requests.get(domain_url)
    #
    # print(response.content)
    # search_keywords = 'курсы'
    # search_keywords_translit = translit(search_keywords, "ru", reversed=True)
    # print(search_keywords_translit)
    check_internet_connection()
