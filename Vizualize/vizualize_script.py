import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def vizualize_script():
    df = pd.read_csv('cleaned_dataset.csv')

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
    fig, axes = plt.subplots(1, 4, figsize=(16, 6))

    # Построение гистограмм для каждой колонки
    for i, column_name in enumerate(columns_to_visualize):
        ax = axes[i]
        ax.hist(df[column_name], bins=40, color='skyblue', edgecolor='black', linewidth=0.5)
        ax.set_title(f'Correlation histogram of {column_name}')
        ax.set_xlabel(column_name)
        ax.set_ylabel('Frequency')

    # Отобраение всех графиков
    plt.tight_layout()
    plt.show()
