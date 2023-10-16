import pandas as pd
from configparser import ConfigParser

c = pd.read_csv('Cytotoxicity.csv')

config = ConfigParser()

for material in list(set(c['material'].tolist())):
    config.add_section(material)
    config[material]['CID'] = ''
    config[material]['SMILES'] = ''

with open('book.ini', 'w') as config_file:
    config.write(config_file)