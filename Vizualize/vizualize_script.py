import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def vizualize_script():
    df = pd.read_csv('cleaned_dataset.csv')

    # Построение гистограмм
    # Выбрали колонки для визуализации на графике
    columns_to_visualize = ['concentration (ug/ml)', 'viability (%)', 'Hydrodynamic diameter (nm)',
                            'Zeta potential (mV)']

    # Построили гистограмм для выбранных колонок
    df[columns_to_visualize].hist(bins=20, figsize=(12, 8))

    # Построение матрицы корреляции
    correlation_matrix = df[columns_to_visualize].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, linewidths=0.5)

    # Сделать так, чтобы 4 графика отобразились в 1
    plt.figure(figsize=(16, 6))
    # Создание гистограмм
    for i, column_name in enumerate(columns_to_visualize):
        plt.subplot(1, 4, i + 1)
        plt.xlabel(column_name)
        plt.ylabel('Frequency')

    # Отобраение всех графиков
    plt.tight_layout()
    plt.show()
