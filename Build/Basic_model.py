import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras import layers
from lazypredict.Supervised import LazyRegressor
import matplotlib.pyplot as plt


def predict_model():
    # Загрузка данных
    df = pd.read_csv('cleaned_dataset.csv')

    # Разделение на признаки
    x = df.drop('viability (%)', axis=1)
    y = df['viability (%)']

    # Делим на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Создание модели
    model = keras.Sequential([
        layers.Input(shape=(X_train.shape[1],)),
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(1)  # 1 выходной нейрон для регрессии
    ])

    # Компиляция модели
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Создание и обучение моделей регрессии
    model = LazyRegressor(predictions=True)
    models, predictions = model.fit(X_train, X_test, y_train, y_test)

    # Вывод
    print(models)

    plt.figure(figsize=(10, 6))
    plt.barh(models.index, models['R-Squared'])
    plt.xlabel('R-Squared')
    plt.title('Model performance')
    plt.xlim(-1.0, 0.8)
    plt.gca().invert_yaxis()
    plt.show()
