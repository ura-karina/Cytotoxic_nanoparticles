import pandas as pd
import matplotlib.pyplot as plt

from Merging_script import merge_script
from Clean.Cleaning_dataset_script import clean_script

data_cell = pd.read_csv('cell_line_descriptors.csv')
data_cytotoxicity = pd.read_csv('Cytotoxicity.csv')
data_descriptors = pd.read_excel('Merge/Incomplete_material_descriptors.xlsx')


if __name__ == '__main__':
    merge_script()
    clean_script()