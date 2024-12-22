import nltk
import re
from nltk.corpus import stopwords

# Загрузка списка стоп-слов
nltk.download('stopwords')

def clean_text(text):
    # Приведение текста к нижнему регистру
    text = text.lower()
    # Удаление ссылок
    text = re.sub(r'http\S+', '', text)
    # Удаление неалфавитных символов (пунктуации, чисел и т.д.)
    text = re.sub(r'[^a-zа-яё\s]', '', text)
    # Удаление стоп-слов
    stop_words = set(stopwords.words('russian'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Чтение исходного файла с отзывами
with open('reviews.txt', 'r', encoding='utf-8') as file:
    reviews = file.readlines()

# Очистка текста
cleaned_reviews = [clean_text(review) for review in reviews]

# Сохранение очищенных отзывов в новый файл
with open('../PythonProject1/cleaned_reviews.txt', 'w', encoding='utf-8') as file:
    file.writelines('\n'.join(cleaned_reviews))

print("Очищенные отзывы сохранены в файл 'cleaned_reviews.txt'.")
