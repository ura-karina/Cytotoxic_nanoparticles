import pandas as pd


def clean_script():
    df = pd.read_csv('Merge/cytotoxicity_merged.csv')

    new_df = df.drop_duplicates()

    new_df = df[df['viability (%)'] <= 150]
    new_df = df[df['concentration (ug/ml)'] <= 1000]
    new_df = df[df['Zeta potential (mV)'] >= -50]
    new_df = df[df['Hydrodynamic diameter (nm)'] <= 400]

    # Проверка на согласованность данных (проверка уникальных значений)
    unique_values_cells = df['cell type'].unique()
    unique_values_time = df['time (hr)'].unique()
    unique_values_viability = df['viability (%)'].unique()
    unique_values_conc = df['concentration (ug/ml)'].unique()
    unique_values_diameter = df['Hydrodynamic diameter (nm)'].unique()

    # Подсчитаем нули в каждой строке
    zero_counts = new_df[new_df == 0].count(axis=1)

    # Удалите строки, в которых количество нулей превышает пороговое значение
    new_df = new_df[zero_counts >= 7]

    # Колонки, в которых нужно проверить пропуски и заменить их на средние значения
    columns_to_fillna = ['test', 'material', 'time (hr)', 'concentration (ug/ml)', 'viability (%)',
                         'Hydrodynamic diameter (nm)', 'Zeta potential (mV)', 'cell line', 'organism',
                         'cell type', 'morphology', 'tissue', 'disease', 'BSL']

    # Проверяем наличие пропусков в колонках
    missing_data = df[columns_to_fillna].isnull()

    # Заменяем пропуски на средние значения в колонках
    for column in columns_to_fillna:
        if missing_data[column].any():
            mean_value = df[column].mean()
            df[column].fillna(mean_value, inplace=True)

    # Сохранение очищенных данных в новый .csv файл
    new_df.to_csv("cleaned_dataset.csv", index=False)
