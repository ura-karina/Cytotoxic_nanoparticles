# test system template
import pandas as pd

df = pd.read_csv('')

dublicates = df[df.dublicated ()]

omissions = df[df.isnull().values==True]


writer = pd.ExcelWriter('Итог.xlsx')
df.to_excel(writer, 'Лист1')
writer.save()