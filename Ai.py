import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import nltk
from nltk.corpus import stopwords

# Загрузка стоп-слов для русского языка
nltk.download('stopwords')
russian_stopwords = stopwords.words('russian')

# Чтение данных из файла с разделителем " | "
data = []
with open('sentiment_analysis.txt', 'r', encoding='utf-8') as file:
    for line in file:
        text, label = line.strip().split(" | ")
        data.append([text, label])

# Преобразуем данные в DataFrame
df = pd.DataFrame(data, columns=['text', 'label'])

# Разделение на обучающие и тестовые данные
X = df['text']  # Тексты отзывов
y = df['label']  # Метки (тональность)

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Векторизация текста с использованием TF-IDF
vectorizer = TfidfVectorizer(stop_words=russian_stopwords, max_features=1000)  # Преобразуем текст в TF-IDF вектор
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Обучение модели
model = MultinomialNB()  # Наивный байесовский классификатор
model.fit(X_train_tfidf, y_train)

# Оценка модели
y_pred = model.predict(X_test_tfidf)
print(classification_report(y_test, y_pred))  # Вывод точности модели

# Прогнозирование для нового отзыва
new_review = [".."]
new_review_tfidf = vectorizer.transform(new_review)
prediction = model.predict(new_review_tfidf)
print(f"Тональность отзыва: {prediction[0]}")  # Выводим тональность
