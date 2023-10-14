import pandas as pd
import matplotlib.pyplot as plt


data_cell = pd.read_csv('cell_line_descriptors.csv')
data_cytotoxicity = pd.read_csv('Cytotoxicity.csv')
data_descriptors = pd.read_excel('Incomplete_material_descriptors.xlsx')


# if __name__ == '__main__':
#     print('PyCharm')
