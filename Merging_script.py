import pandas as pd
from configparser import ConfigParser
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Lipinski
from rdkit.Chem import Crippen

d = pd.read_csv('cell_line_descriptors.csv')
d.insert(loc=0, column='idx', value=range(d.shape[0]))
d.set_index('idx')

c = pd.read_csv('Cytotoxicity.csv')
c.insert(loc=0, column='idx', value=range(c.shape[0]))
c.set_index('idx')

cd_columns = c.columns.tolist() + d.columns.tolist()
cd_merged = pd.DataFrame(columns=cd_columns)

def c_plus_d():
    for c_idx in c['idx']:

        values = c.iloc[c_idx].tolist()
        # print(values)
        cell_type = c.loc[c_idx]['Cell type']
        # print('cell type:', cell_type)
        for d_idx in d['idx']:
            cell_line = d.iloc[d_idx]['cell line']
            if cell_line != cell_type:
                continue
            values += d.iloc[d_idx].tolist()
            # print('cell line:', cell_line)
            break
        # print(cd_merged.columns)
        # print('values:', values, len(values))
        cd_merged.loc[c_idx] = values


m_columns = ['material', 'CID', 'Canonical_smiles',	'Valance_electron', 'amw',
             'lipinskiHBA', 'lipinskiHBD', 'NumRotatableBonds', 'NumHeavyAtoms', 'NumAtoms', 'NumHeteroatoms',
             'NumAmideBonds', 'FractionCSP3', 'NumRings', 'NumAromaticRings', 'NumAliphaticRings',	'NumSaturatedRings',
             'NumHeterocycles', 'NumAromaticHeterocycles', 'NumSaturatedHeterocycles', 'NumAliphaticHeterocycles',
             'NumSpiroAtoms', 'NumBridgeheadAtoms', 'NumAtomStereoCenters', 'NumUnspecifiedAtomStereoCenters',
             'labuteASA', 'tpsa', 'CrippenClogP', 'CrippenMR', 'chi0v', 'chi1v', 'chi2v', 'chi3v', 'chi4v', 'chi0n',
             'chi1n', 'chi2n', 'chi3n', 'chi4n', 'hallKierAlpha', 'kappa1', 'kappa2', 'kappa3', 'Phi']


class Material:
    def __init__(self, brutto):

        self.brutto = brutto

        book = ConfigParser()
        book.read('Material_book_descriptors.ini', encoding='utf-8')

        if brutto not in book.sections():
            print(f'ERROR: material {brutto} not found')
            return

        self.SMILES = book[brutto]['SMILES']
        self.CID = book[brutto]['CID']

        mol = Chem.MolFromSmiles(self.SMILES)

        self.Valance_electron = Descriptors.NumValenceElectrons(mol)
        self.amw = Descriptors.MolWt(mol)
        self.lipinskiHBA = Lipinski.NOCount(mol)
        self.lipinskiHBD = Lipinski.NHOHCount(mol)
        self.NumRotatableBonds = Lipinski.NumRotatableBonds(mol)
        self.HeavyAtomCount = Lipinski.HeavyAtomCount(mol)
        self.full = Descriptors.CalcMolDescriptors(mol)
        self.NumAtoms = len([atom for atom in mol.GetAtoms()])
        self.NumHeteroatoms = Lipinski.NumHeteroatoms(mol)
        self.NumAmideBonds = Chem.rdMolDescriptors.CalcNumAmideBonds(mol)
        self.FractionCSP3 = Lipinski.FractionCSP3(mol)
        self.NumRings = Chem.rdMolDescriptors.CalcNumRings(mol)
        self.NumAromaticRings = Chem.rdMolDescriptors.CalcNumAromaticRings(mol)
        self.NumAliphaticRings = Chem.rdMolDescriptors.CalcNumAliphaticRings(mol)
        self.NumSaturatedRings = Chem.rdMolDescriptors.CalcNumSaturatedRings(mol)
        self.NumHeterocycles = Chem.rdMolDescriptors.CalcNumHeterocycles(mol)
        self.NumAromaticHeterocycles = Chem.rdMolDescriptors.CalcNumAromaticHeterocycles(mol)
        self.NumSaturatedHeterocycles = Chem.rdMolDescriptors.CalcNumSaturatedHeterocycles(mol)
        self.NumAliphaticHeterocycles = Chem.rdMolDescriptors.CalcNumAliphaticHeterocycles(mol)
        self.NumSpiroAtoms = Chem.rdMolDescriptors.CalcNumSpiroAtoms(mol)
        self.NumBridgeheadAtoms = Chem.rdMolDescriptors.CalcNumBridgeheadAtoms(mol)
        self.NumAtomStereoCenters = Chem.rdMolDescriptors.CalcNumAtomStereoCenters(mol)
        self.NumUnspecifiedAtomStereoCenters = Chem.rdMolDescriptors.CalcNumUnspecifiedAtomStereoCenters(mol)
        self.labuteASA = Chem.rdMolDescriptors.CalcLabuteASA(mol)
        self.tpsa = Chem.rdMolDescriptors.CalcTPSA(mol)
        self.CrippenClogP = Crippen.MolLogP(mol)
        self.CrippenMR = Crippen.MolMR(mol)
        self.chi0v = Chem.GraphDescriptors.Chi0v(mol)
        self.chi1v = Chem.GraphDescriptors.Chi1v(mol)
        self.chi2v = Chem.GraphDescriptors.Chi2v(mol)
        self.chi3v = Chem.GraphDescriptors.Chi3v(mol)
        self.chi4v = Chem.GraphDescriptors.Chi4v(mol)
        self.chi0n = Chem.GraphDescriptors.Chi0n(mol)
        self.chi1n = Chem.GraphDescriptors.Chi1n(mol)
        self.chi2n = Chem.GraphDescriptors.Chi2n(mol)
        self.chi3n = Chem.GraphDescriptors.Chi3n(mol)
        self.chi4n = Chem.GraphDescriptors.Chi4n(mol)
        self.hallKierAlpha = Chem.GraphDescriptors.HallKierAlpha(mol)
        self.kappa1 = Chem.GraphDescriptors.Kappa1(mol)
        self.kappa2 = Chem.GraphDescriptors.Kappa2(mol)
        self.kappa3 = Chem.GraphDescriptors.Kappa3(mol)
        self.Phi = Chem.rdMolDescriptors.CalcPhi(mol)


config = ConfigParser()

for material in list(set(c['material'].tolist())):
    config.add_section(material)
    config[material]['CID'] = ''
    config[material]['SMILES'] = ''

with open('book.ini', 'w') as config_file:
    config.write(config_file)











