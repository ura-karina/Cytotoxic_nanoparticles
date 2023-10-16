# test system
import pandas as pd

df = pd.read_csv('cytotoxicity_merged.csv')

omis = df.isnull().sum()
print('Omissions: \n', omis)

y = df.to_dict()

indexes = {}
for i,v in enumerate(y):
    indexes[v] = indexes.get(v, []) + [i]
for v in indexes.values():
    if len(v) > 1:
        print('Duplicates: \n'*v)