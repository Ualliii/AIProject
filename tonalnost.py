from deeppavlov import build_model, configs

# Загрузка предобученной модели для анализа тональности
model = build_model(configs.classifiers.sentiment_twitter, download=True)

# Чтение отзывов из файла
try:
    with open('../PythonProject1/cleaned_reviews.txt', 'r', encoding='utf-8') as file:
        reviews = file.readlines()
except FileNotFoundError:
    print("Файл 'cleaned_reviews.txt' не найден. Убедитесь, что он находится в той же директории, что и скрипт.")
    exit()

# Анализ тональности
results = []
for review in reviews:
    if review.strip():  # Проверяем, что строка не пустая
        sentiment = model([review.strip()])[0]  # Анализ тональности
        results.append(f"Review: {review.strip()}\nSentiment: {sentiment}\n\n")

# Сохранение результатов в файл
with open('../PythonProject1/sentiment_analysis.txt', 'w', encoding='utf-8') as file:
    file.writelines(results)

print("Анализ тональности завершен. Результаты сохранены в 'sentiment_analysis.txt'.")
