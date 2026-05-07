import pandas as pd

homelessness = pd.read_csv('homelessness.csv')

# Filtra 'homelessness' para los casos en que el número de 'individuals' sea superior a diez mil, asignandolos a 'ind_gt_10k'

ind_gt_10k = homelessness[homelessness['individuals'] > 10000]

print(ind_gt_10k)

# Filtra 'homelessness' para los casos en los que el código del censo de EE.UU 'region' es "Mountain", asignandolo a 'mountain_reg'

mountain_reg = homelessness[homelessness['region'] == "Mountain"]

print(mountain_reg)

# Filtra 'homelessness' para los casos en los que el número de 'family_members' sea inferior a mil y el 'region' sea "Pacific", asignandolos a 'fam_lt_1k_pac'

fam_lt_1k_pac = homelessness[(homelessness['family_members'] < 1000) & (homelessness['region'] == "Pacific")]

print(fam_lt_1k_pac)