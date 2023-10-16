# test system template
import pandas as pd
import openpyxl

df = pd.read_csv('cytotoxicity_merged.csv')

duplicates = df[df.duplicated()]
# df.groupby (df.columns.tolist (), as_index= False ). size ()


omissions = df[df.isnull().values==True]

print()
# writer = pd.ExcelWriter('Итог.xlsx')
# df.to_excel(writer, 'Лист1')
# writer._save()