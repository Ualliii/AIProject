import requests
from bs4 import BeautifulSoup
import time

# Базовый URL
base_url = "https://www.kinopoisk.ru/film/326/reviews/ord/date/status/all/perpage/10/page/{}/"

# Файл для сохранения отзывов
output_file = "reviews.txt"

# Заголовки для запроса
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; ARM Mac OS X 11_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

# Открываем файл для записи
with open(output_file, "w", encoding="utf-8") as f:
    for page in range(23, 567):  # Страницы от 2 до 566
        url = base_url.format(page)
        print(f"Парсинг страницы: {page}")

        try:
            # Отправляем запрос
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Проверяем на ошибки

            # Парсим HTML
            soup = BeautifulSoup(response.text, "html.parser")

            # Находим отзывы
            reviews = soup.find_all(class_="_reachbanner_")

            if not reviews:
                print(f"На странице {page} нет отзывов.")
                continue

            # Записываем отзывы в файл
            for review in reviews:
                review_text = review.get_text(strip=True)
                if review_text:  # Проверка на пустые строки
                    f.write(review_text + "\n")  # Запись в файл

            # Задержка между запросами, чтобы не заблокировали
            time.sleep(2)

        except Exception as e:
            print(f"Ошибка на странице {page}: {e}")
            continue

print("Парсинг завершён. Отзывы сохранены в файл 'reviews.txt'.")
